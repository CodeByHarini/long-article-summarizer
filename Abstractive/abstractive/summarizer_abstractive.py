from transformers import pipeline
import math

# Choose a smaller/faster summarization model for Spaces (change if you want)
DEFAULT_MODEL = "sshleifer/distilbart-cnn-12-6"

def load_summarizer(model_name: str = DEFAULT_MODEL, device: int = -1):
    """
    Load and return a transformers summarization pipeline.
    device=-1 => CPU, device=0 => GPU (if available).
    """
    summarizer = pipeline("summarization", model=model_name, device=device)
    return summarizer

def chunk_text_by_words(text: str, chunk_size_words: int = 500, overlap_words: int = 50):
    """
    Naive chunking by words with overlapping windows.
    Returns list of text chunks.
    """
    words = text.split()
    if len(words) <= chunk_size_words:
        return [" ".join(words)]
    chunks = []
    i = 0
    while i < len(words):
        chunk = words[i:i + chunk_size_words]
        chunks.append(" ".join(chunk))
        i += (chunk_size_words - overlap_words)
    return chunks

def abstractive_summarize(text: str, summarizer, chunk_size_words: int = 500,
                          overlap_words: int = 50, max_length: int = 130, min_length: int = 30):
    """
    Hierarchical summarization:
     - Split text into overlapping chunks
     - Summarize each chunk
     - Concatenate chunk summaries and summarize them
    """
    text = text.strip()
    if not text:
        return "⚠️ No text provided."

    # If short, summarize directly
    if len(text.split()) <= chunk_size_words:
        out = summarizer(text, max_length=max_length, min_length=min_length, truncation=True)
        return out[0]["summary_text"].strip()

    # Chunking
    chunks = chunk_text_by_words(text, chunk_size_words=chunk_size_words, overlap_words=overlap_words)

    # Summarize each chunk (map)
    chunk_summaries = []
    for c in chunks:
        try:
            s = summarizer(c, max_length=max_length, min_length=min_length, truncation=True)
            chunk_summaries.append(s[0]["summary_text"].strip())
        except Exception as e:
            # Fallback: partial reduce by truncation
            snippet = " ".join(c.split()[:chunk_size_words//2])
            s = summarizer(snippet, max_length=max_length, min_length=min_length, truncation=True)
            chunk_summaries.append(s[0]["summary_text"].strip())

    # Combine chunk summaries (reduce)
    combined = " ".join(chunk_summaries)
    # If combined is still long, we may need another round; do one final summarization
    final = summarizer(combined, max_length=max_length, min_length=min_length, truncation=True)
    return final[0]["summary_text"].strip()
