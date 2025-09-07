# **Long Article Summarizer (Extractive)**

[![Open in Hugging Face](https://img.shields.io/badge/Hugging%20Face-Try%20Demo-blue)](https://huggingface.co/spaces/CodeByHarini/long-article-summarizer-extractive)

## **Project Overview**

Digesting long articles like news, blogs, or research papers can be time-consuming.
This project demonstrates an **extractive summarization approach**, which quickly identifies the most important sentences from the text to provide a concise summary.

> **Note:** This is the **extractive stage**. The abstractive transformer-based version is available separately in the Abstractive module.


## **Extractive Summarization**

**Method:** TextRank (graph-based ranking of sentences)

* Selects the most important sentences from the input text.
* Provides a quick, accurate baseline summary.
* Implemented in Python using **BeautifulSoup**, **requests**, and **sumy**.


## **Live Demo**

Try the live demo on Hugging Face Spaces:  
[**Click here to try it now**](https://huggingface.co/spaces/CodeByHarini/long-article-summarizer-extractive)


### **Screenshots**

**Input Text Example:**

![Input Screenshot](https://github.com/CodeByHarini/long-article-summarizer/blob/main/Extractive/Input%20Extractive.jpg)

**Extractive Summary Output:**

![Output Screenshot](https://github.com/CodeByHarini/long-article-summarizer/blob/main/Extractive/Output%20Extractive.jpg)

### **Demo Video**

Watch the extractive summarizer in action:

![Demo Video](https://github.com/CodeByHarini/long-article-summarizer/blob/main/Extractive/Demo%20Video%20Extractive.mp4)


## **Installation (Local Testing)**

```bash
# Clone the repo
git clone https://github.com/CodeByHarini/long-article-summarizer.git
cd long-article-summarizer/Extractive

# Create virtual environment
python -m venv venv
venv\Scripts\activate    # Windows
# source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements_extractive.txt

# Run the app
python app_extractive.py
```


## **Folder Structure (Extractive)**

```
Extractive/
├── app_extractive.py                  # Main extractive summarizer app
├── summarizer_extractive.py           # TextRank / extractive logic
├── sample_articles_extractive.json    # Sample articles for testing
├── Demo Video Extractive.mp4          # Demo video
├── Input Extractive.jpg               # Input example screenshot
├── Output Extractive.jpg              # Output example screenshot
├── requirements_extractive.txt        # Required Python packages
├── runtime_extractive.txt             # Runtime configuration
├── README_extractive.md               # Documentation
```


## **Technologies & Libraries**

* Python 3.12
* BeautifulSoup4 — HTML parsing
* Requests — HTTP requests
* Sumy (TextRank) — Extractive summarization
* Gradio — Local web interface


## **Next Steps / Abstractive Version**

* Replace TextRank with **transformer-based models** like BART, T5, or LED.
* Handle long documents using **chunking** or **long-context models**.
* Compare extractive vs. abstractive outputs using **ROUGE** or **BERTScore**.


## **Portfolio Soundbite**

> “Built a two-stage summarization system: starting with a fast extractive baseline using TextRank, then extending to transformer-based abstractive summaries. This demonstrates both engineering discipline and hands-on experience with modern NLP models.”


## **Acknowledgements**

* Sumy — for TextRank implementation
* BeautifulSoup4 — for HTML parsing
* Hugging Face Spaces — for hosting the live demo
* OpenAI & ChatGPT — guidance on portfolio structuring


## **License**

This project is licensed under the [MIT License](https://github.com/CodeByHarini/long-article-summarizer/blob/main/LICENSE) — see the LICENSE file for details.

