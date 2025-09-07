
# 💬 Harini Portfolio Chatbot

An **interactive AI assistant** built with **Gradio** and **Hugging Face Transformers** that answers questions about Harini’s skills, projects, and contact info.  
Features a modern **Instagram-DM-inspired UI** with animated gradient blobs.

---

## 🚀 Live Demo

Try the chatbot live here:  
👉 [Harini AI Portfolio Chatbot](https://huggingface.co/spaces/CodeByHarini/harini-portfolio-chatbot)

---

## ⚡ Quick Setup (One-Click for Recruiters)

### **Option 1: Using pip**
```bash
# Clone the repository
git clone https://github.com/CodeByHarini/Harini_Portfolio_Chatbot.git
cd Harini_Portfolio_Chatbot

# Create & activate virtual environment
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the chatbot
python app.py
````

### **Option 2: Using Conda**

```bash
# Clone the repository
git clone https://github.com/CodeByHarini/Harini_Portfolio_Chatbot.git
cd Harini_Portfolio_Chatbot

# Create Conda environment
conda env create -f environment.yml
conda activate harini_chatbot_env

# Run the chatbot
python app.py
```

> The chatbot will open at `http://127.0.0.1:7860` locally.
> Optional: Use `python app.py --share` to get a public Hugging Face link.

---

## 📸 Demo Screenshot / Video

### Screenshot

![Chatbot Screenshot](assets/chatbot_screenshot.png)

### Video

[![Watch Video](assets/chatbot_demo_thumbnail.png)](assets/chatbot_demo.mp4)

---

## 🖥 Features

* AI-powered Q\&A using **DistilBERT (SQuAD)**
* Instagram-DM-inspired **animated UI**
* Recognizes portfolio-related queries: Bio, Skills, Projects, Contact
* Typing simulation & clear chat button
* Exit command support (`exit`, `quit`, `bye`)

---

## 🛠 Tech Stack

* Python 3.10+
* Gradio – Web interface
* Hugging Face Transformers – DistilBERT (SQuAD)
* PyTorch – Backend for Transformers
* HTML & CSS – Custom UI & animations

---

## 📂 Folder Structure

```
Harini_Portfolio_Chatbot/
│
├─ app.py
├─ context_builder.py
├─ faq_data.py
├─ LICENSE
├─ README.md
├─ requirements.txt
├─ environment.yml
└─ assets/  # Screenshots, video, icons
```

---

## 📜 License

MIT License. See [LICENSE](LICENSE) for details.

---
🙏 Acknowledgements

Hugging Face Transformers for NLP models.

Gradio documentation for interactive web UI.

Inspiration from Instagram DM UI for modern chatbot design.
```



