import gradio as gr
import requests
from bs4 import BeautifulSoup
import os
import nltk
from summarizer_abstractive import load_summarizer, abstractive_summarize

# Setup NLTK
nltk_data_dir = os.path.join(os.path.dirname(__file__), "nltk_data")
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.data.path.append(nltk_data_dir)
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt", download_dir=nltk_data_dir)

# Load the summarizer model
SUMMARIZER = load_summarizer()  # Uses CPU by default, set device=0 for GPU if available

# -------------------------
# Helper Functions
# -------------------------
def fetch_article_text(url):
    """Fetch text content from an article URL using BeautifulSoup."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        for tag in soup(["script", "style", "noscript"]):
            tag.extract()
        paragraphs = soup.find_all("p")
        text = " ".join([p.get_text() for p in paragraphs])
        return text if len(text.strip()) > 200 else None
    except Exception:
        return None

def summarize_text_interface(text, sentences_slider=3, chunk_size=500):
    """Summarize input text using the abstractive summarizer."""
    if not text or len(text.strip()) < 50:
        return "⚠️ Please enter a longer article (50+ words)."

    max_length = 40 + int(sentences_slider) * 30
    min_length = max(20, max_length // 4)

    try:
        summary = abstractive_summarize(
            text,
            SUMMARIZER,
            chunk_size_words=int(chunk_size),
            overlap_words=int(chunk_size * 0.1),
            max_length=max_length,
            min_length=min_length
        )
        return summary
    except Exception as e:
        return f"⚠️ Summarization error: {str(e)}"

def summarize_url_interface(url, sentences_slider=3, chunk_size=500):
    """Summarize article from a URL."""
    txt = fetch_article_text(url)
    if not txt:
        return "⚠️ Could not fetch article text from the provided URL."
    return summarize_text_interface(txt, sentences_slider, chunk_size)

# -------------------------
# Custom UI Theme
# -------------------------
custom_theme = gr.themes.Soft(
    primary_hue="violet",
    secondary_hue="blue"
).set(
    button_primary_background_fill="#6c63ff",
    button_primary_background_fill_hover="#857cff",
    button_primary_text_color="white"
)

# -------------------------
# Gradio UI
# -------------------------
with gr.Blocks(theme=custom_theme, css=".tab-button {font-size: 16px; font-weight: bold;}") as demo:
    gr.Markdown(
        """
        <div style="text-align:left;">
            <h1 style="color:#FFFFFF;">📰 Abstractive Summarizer</h1>
            <p style="color:#4e4e4e; font-size:16px;">Generate human-like summaries using Transformer models</p>
        </div>
        """
    )

    # 📄 Paste Text Tab
    with gr.Tab("📄 Paste Text"):
        text_input = gr.Textbox(
            placeholder="Paste your article here...",
            lines=15,
            label="Enter Article Text"
        )
        sentence_slider = gr.Slider(1, 7, value=3, step=1, label="Summary Length")
        chunk_size = gr.Number(value=500, label="Chunk Size (words)")
        text_button = gr.Button("📝 Summarize Text")
        text_output = gr.Textbox(label="Summary", lines=8)
        text_button.click(fn=summarize_text_interface, inputs=[text_input, sentence_slider, chunk_size], outputs=text_output)

    # 🔗 Summarize URL Tab
    with gr.Tab("🔗 Summarize URL"):
        url_input = gr.Textbox(
            placeholder="Paste article URL here...",
            label="Enter URL"
        )
        url_slider = gr.Slider(1, 7, value=3, step=1, label="Summary Length")
        chunk_size_u = gr.Number(value=500, label="Chunk Size (words)")
        url_button = gr.Button("🌐 Summarize URL")
        url_output = gr.Textbox(label="Summary", lines=8)
        url_button.click(fn=summarize_url_interface, inputs=[url_input, url_slider, chunk_size_u], outputs=url_output)

    # Footer
    gr.Markdown("---")
    gr.Markdown("<p style='text-align:center; color:#bbb;'>👩‍💻 Built by <b>Harini</b> | Step 2 of Long Article Summarizer 🚀</p>")

# -------------------------
# Launch App
# -------------------------
if __name__ == "__main__":
    demo.launch(share=True)
