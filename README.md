# Long Article Summarizer

This repository demonstrates a **two-stage summarization system** for long articles, blogs, and research papers:

1. **Extractive Summarizer** – Quickly identifies and extracts the most important sentences using **TextRank**.
   [Learn more →]()

2. **Abstractive Summarizer** – Generates **human-like summaries** using transformer-based models (BART, T5, LED).
   [Learn more →]()


## Project Overview

Digesting long documents can be time-consuming. This system provides:

* **Fast extractive summaries** for immediate insights.
* **Abstractive summaries** for fluent, condensed, and coherent summaries.
* A modular structure for experimentation with different NLP models.



## Folder Structure

```
long-article-summarizer/
│
├── Abstractive/                              # Abstractive summarizer module
│   ├── app_abstractive.py                    # Main app for abstractive summarization
│   ├── summarizer_abstractive.py            # Core logic for abstractive summarization
│   ├── requirements_abstractive.txt         # Required dependencies for abstractive app
│   ├── README_abstractive.md               # Documentation for abstractive summarizer
│   ├── Demo Video Abstractive.mp4          # Demo video for abstractive summarizer
│   ├── Input Abstractive.jpg               # Sample input example for abstractive
│   ├── Output Abstractive.jpg              # Sample output example for abstractive
│
├── Extractive/                              # Extractive summarizer module
│   ├── app_extractive.py                    # Main app for extractive summarization
│   ├── summarizer_extractive.py            # Core logic for extractive summarization
│   ├── requirements_extractive.txt         # Required dependencies for extractive app
│   ├── runtime_extractive.txt              # Runtime configuration for extractive app
│   ├── sample_articles_extractive.json     # Sample data for extractive testing
│   ├── README_extractive.md               # Documentation for extractive summarizer
│   ├── Demo Video Extractive.mp4          # Demo video for extractive summarizer
│   ├── Input Extractive.jpg               # Sample input example for extractive
│   ├── Output Extractive.jpg              # Sample output example for extractive
│
├── LICENSE                                # Open-source MIT license
├── README.md                             # Main documentation for the project
├── .gitignore                            # Files and folders ignored by Git

```

## Live Demo

* **Extractive Summarizer:** [Try it on Hugging Face Spaces](https://huggingface.co/spaces/CodeByHarini/long-article-summarizer-extractive)
* **Abstractive Summarizer:** [Try it on Hugging Face Spaces](https://huggingface.co/spaces/CodeByHarini/long-article-summarizer-abstractive)


## Installation (Local Testing)

```bash
# Clone the repo
git clone https://github.com/CodeByHarini/long-article-summarizer.git
cd long-article-summarizer

# Create virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Mac/Linux

# Install dependencies for extractive
cd extractive
pip install -r requirements.txt
python app.py

# Or install dependencies for abstractive
cd ../abstractive
pip install -r requirements_abstractive.txt
python app_abstractive.py
```

## Technologies & Libraries

* Python 3.12
* **Extractive:** TextRank via Sumy, BeautifulSoup, Requests
* **Abstractive:** Hugging Face Transformers (BART / T5 / LED), PyTorch, Gradio
* Optional: NLTK / SpaCy for preprocessing


## Next Steps / Improvements

* Fine-tune transformer models for domain-specific summarization
* Support very long documents using chunking or long-context models
* Compare extractive vs. abstractive outputs using **ROUGE**, **BERTScore**, or other metrics
* Expand web interface for interactive summarization


## Portfolio Soundbite

> “Built a two-stage summarization system: a fast extractive baseline using TextRank, extended to transformer-based abstractive summaries, showcasing both NLP engineering and deployment skills.”


## Acknowledgements

* Hugging Face Transformers — pretrained models & pipelines
* Gradio — web interface
* Sumy — TextRank implementation
* BeautifulSoup4 — HTML parsing
* OpenAI & ChatGPT — guidance on portfolio structuring


## License

This project is licensed under the MIT License — see LICENSE for details.

