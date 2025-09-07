# Long Article Summarizer

This repository demonstrates a **two-stage summarization system** for long articles, blogs, and research papers:

1. **Extractive Summarizer** – Quickly identifies and extracts the most important sentences using **TextRank**.
   [Learn more →](extractive/README.md)

2. **Abstractive Summarizer** – Generates **human-like summaries** using transformer-based models (BART, T5, LED).
   [Learn more →](abstractive/README.md)


## Project Overview

Digesting long documents can be time-consuming. This system provides:

* **Fast extractive summaries** for immediate insights.
* **Abstractive summaries** for fluent, condensed, and coherent summaries.
* A modular structure for experimentation with different NLP models.



## Folder Structure

```
long-article-summarizer/
│
├─ README.md                     # Master README (overview of the repo)
├─ extractive/
│   ├─ README.md                 # Extractive-specific README
│   ├─ app.py
│   ├─ summarizer.py
│   ├─ datasets/
│   │   └─ sample_articles.json
│   ├─ screenshots/
│   ├─ demo/
│   └─ requirements.txt
│
├─ abstractive/
│   ├─ README.md                 # Abstractive-specific README
│   ├─ app_abstractive.py
│   ├─ summarizer_abstractive.py
│   ├─ datasets/
│   │   └─ sample_articles.json
│   ├─ screenshots/
│   ├─ demo/
│   └─ requirements_abstractive.txt
│
├─ LICENSE
└─ .gitignore
```

## Live Demo

* **Extractive Summarizer:** [Try it on Hugging Face Spaces](#)
* **Abstractive Summarizer:** [Try it on Hugging Face Spaces](#)


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

