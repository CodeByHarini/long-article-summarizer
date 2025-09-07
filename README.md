# Long Article Summarizer (Extractive)

[![Open in Hugging Face](https://img.shields.io/badge/Hugging%20Face-Try%20Demo-blue)](https://huggingface.co/spaces/CodeByHarini/long-article-summarizer-extractive)

## **Project Overview**

Digesting long articles like news, blogs, and research papers can be time-consuming.  
This project demonstrates a **two-step summarization approach**, starting with **extractive summarization** as a fast baseline.

> **Note:** This README focuses on the extractive stage. The abstractive (transformer-based) version will be added later.


## **Extractive Summarization**

**Method:** TextRank (graph-based ranking of sentences)

- Selects the most important sentences from the input text.
- Provides a **quick, accurate baseline summary**.
- Implemented in Python using `BeautifulSoup`, `requests`, and `sumy`.

### **Live Demo**

Try the live demo on Hugging Face Spaces:  
[**Click here to try it now**](https://huggingface.co/spaces/CodeByHarini/long-article-summarizer-extractive)


### **Screenshots**

**Input Text Example:**

![Input Screenshot](screenshots/input_example.png)

**Extractive Summary Output:**

![Output Screenshot](screenshots/output_example.png)

### **Demo Video**

Watch the extractive summarizer in action:

[![Demo Video](demo/demo_video_thumbnail.png)](demo/demo_video.mp4)


## **Installation (Local Testing)**

```bash
# Clone the repo
git clone https://github.com/CodeByHarini/long-article-summarizer.git
cd long-article-summarizer

# Create virtual environment
python -m venv venv
venv\Scripts\activate    # Windows
# source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
````

---

## **Folder Structure**

```
long-article-summarizer/
│
├─ app.py                     # Main extractive summarizer app
├─ summarizer.py              # TextRank / extractive logic
├─ datasets/
│   └─ sample_articles.json
├─ screenshots/
│   ├─ input_example.png
│   └─ output_example.png
├─ demo/
│   └─ demo_video.mp4
├─ requirements.txt
├─ README.md
├─ LICENSE
└─ .gitignore
```

## **Technologies & Libraries**

* Python 3.12
* BeautifulSoup4
* Requests
* Sumy (TextRank)
* Gradio (for local web interface)

## **Next Steps / Abstractive Version**

* Replace TextRank with transformer-based models like **BART / T5 / LED**.
* Handle long documents using **chunking or long-context models**.
* Compare extractive vs. abstractive outputs using **ROUGE / BERTScore**.


## **Portfolio Soundbite**

> “Built a two-stage summarization system: starting with a fast extractive baseline using TextRank, then extending to transformer-based abstractive summaries. This demonstrates both **engineering discipline** and hands-on experience with **modern NLP models**.”


## **Acknowledgements**

* [Sumy](https://github.com/miso-belica/sumy) — for TextRank implementation
* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) — for HTML parsing
* [Hugging Face Spaces](https://huggingface.co/spaces) — for hosting the live demo
* [OpenAI & ChatGPT](https://openai.com) — guidance on portfolio structuring


## **License**

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

