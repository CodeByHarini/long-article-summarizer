import gradio as gr
import requests
from bs4 import BeautifulSoup
from summarizer import extractive_summary
import nltk
import json
import os

# Set up local nltk data directory
nltk_data_dir = os.path.join(os.path.dirname(__file__), "nltk_data")
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.data.path.append(nltk_data_dir)

# Download required tokenizer if missing
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt", download_dir=nltk_data_dir)

# ----------------------
# Load sample articles
# ----------------------
try:
    with open("sample_articles.json", "r", encoding="utf-8") as f:
        sample_articles = json.load(f)
except FileNotFoundError:
    sample_articles = []

# ----------------------
# Functions
# ----------------------
def fetch_article_text(url):
    """Fetch main text content from a webpage using BeautifulSoup."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        # Remove unwanted tags
        for tag in soup(["script", "style", "noscript"]):
            tag.extract()

        # Extract paragraphs
        paragraphs = soup.find_all("p")
        text = " ".join([p.get_text() for p in paragraphs])
        return text if len(text.strip()) > 300 else None
    except Exception:
        return None

def summarize_text(text, sentences=3):
    if not text or len(text.strip()) < 50:
        return "⚠️ Please enter a longer article."
    try:
        return extractive_summary(text, sentence_count=sentences)
    except Exception:
        return "⚠️ Summarization failed. Please try again."

def summarize_url(url, sentences=3):
    text = fetch_article_text(url)
    if not text:
        return "⚠️ Could not fetch content from this URL. Please try another."
    return summarize_text(text, sentences)

def summarize_example(title, sentences=3):
    try:
        article = next(a for a in sample_articles if a["title"] == title)
        return extractive_summary(article["text"], sentence_count=sentences)
    except StopIteration:
        return "⚠️ Example not found."

# ----------------------
# Gradio UI
# ----------------------
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 📰 Extractive Summarizer (TextRank)")
    gr.Markdown("Summarize long news articles or research papers instantly using **LexRank**.")

    with gr.Tab("📄 Paste Text"):
        text_input = gr.Textbox(placeholder="Paste your article here...", lines=15)
        sentence_slider = gr.Slider(1, 7, value=3, step=1, label="Number of Sentences")
        text_button = gr.Button("Summarize Text")
        text_output = gr.Textbox(label="Summary", lines=8)
        text_button.click(fn=summarize_text, inputs=[text_input, sentence_slider], outputs=text_output)

    with gr.Tab("🔗 Summarize URL"):
        url_input = gr.Textbox(placeholder="Paste article URL here...")
        url_slider = gr.Slider(1, 7, value=3, step=1, label="Number of Sentences")
        url_button = gr.Button("Summarize URL")
        url_output = gr.Textbox(label="Summary", lines=8)
        url_button.click(fn=summarize_url, inputs=[url_input, url_slider], outputs=url_output)

    if sample_articles:
        with gr.Tab("📌 Try Example"):
            example_titles = [article["title"] for article in sample_articles]
            example_dropdown = gr.Dropdown(choices=example_titles, label="Choose an Example")
            example_slider = gr.Slider(1, 7, value=3, step=1, label="Number of Sentences")
            example_button = gr.Button("Summarize Example")
            example_output = gr.Textbox(label="Summary", lines=8)
            example_button.click(fn=summarize_example, inputs=[example_dropdown, example_slider], outputs=example_output)

    gr.Markdown("---")
    gr.Markdown("👩‍💻 **Built by Harini** | Step 1 of Long Article Summarizer 🚀")

# Launch app
demo.launch(share=True)
