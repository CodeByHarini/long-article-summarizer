# Long Article Summarizer (Abstractive)
[![Open in Hugging Face](https://img.shields.io/badge/Hugging%20Face-Try%20Demo-blue)](https://huggingface.co/spaces/CodeByHarini/long-article-summarizer-abstractive)

## Project Overview

The abstractive summarizer generates **human-like summaries** of long articles, blogs, and research papers using **transformer-based models**. Unlike extractive summarization, it can **rephrase and condense content**, producing fluent, coherent summaries.

This project builds on the extractive baseline and demonstrates a **two-stage summarization pipeline**.

## Abstractive Summarization

**Method:** Transformer-based sequence-to-sequence models (BART / T5 / LED)

* Handles long documents with **chunking** and **context-aware summarization**.
* Produces concise, natural-sounding summaries, not just extracted sentences.
* Implemented in Python using Hugging Face Transformers and Gradio for the web interface.

### **Live Demo**

Try the live demo on Hugging Face Spaces:  
[**Click here to try it now**](https://huggingface.co/spaces/CodeByHarini/long-article-summarizer-abstractive)


### **Screenshots**

**Input Text Example:**

![Input Screenshot](https://github.com/CodeByHarini/long-article-summarizer/blob/3baf91faddcb9dfca242870d835b64cb2df51641/Input%20Extractive.jpg)

**Extractive Summary Output:**

![Output Screenshot](https://github.com/CodeByHarini/long-article-summarizer/blob/af6e5925821f241b601bcf92647c53e851339b70/Output%20Extractive.jpg)

### **Demo Video**

Watch the extractive summarizer in action:

![Demo Video](https://github.com/CodeByHarini/long-article-summarizer/blob/e826f1628f71fc79eb98ba1acbe3f83e64dd8c13/Demo%20Video.mp4)



## Installation (Local Testing)

```bash
# Clone the repo
git clone https://github.com/CodeByHarini/long-article-summarizer.git
cd long-article-summarizer/abstractive

# Create virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements_abstractive.txt

# Run the app
python app_abstractive.py
```

## Folder Structure

```
long-article-summarizer/
│
├─ abstractive/
│   ├─ app_abstractive.py             # Main abstractive summarizer app
│   ├─ summarizer_abstractive.py      # Transformer-based summarization logic
│   ├─ screenshots/
│   │   ├─ input_example.png
│   │   └─ output_example.png
│   ├─ demo/
│   │   └─ demo_video.mp4
│   ├─ requirements_abstractive.txt
│   └─ README.md
```

## Technologies & Libraries

* Python 3.12
* Hugging Face Transformers (BART / T5 / LED)
* Gradio (for web interface)
* PyTorch or TensorFlow backend
* Optional: `nltk` / `spacy` for text preprocessing

## Portfolio Soundbite

> “Extended a two-stage summarization system by adding an abstractive pipeline using modern transformer-based models, demonstrating both NLP expertise and practical deployment skills.”

## Acknowledgements

* Hugging Face Transformers — for pretrained models and pipelines
* Gradio — for web interface
* OpenAI & ChatGPT — for guidance and code design insights

## License

This project is licensed under the MIT License — see LICENSE for details.

