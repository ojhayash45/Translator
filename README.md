# 🌍 English to Hindi Translator Web App

A Neural Machine Translation web application built using Hugging Face Transformers and Gradio.  
The application translates English text into Hindi in real time using the MarianMT model.

## 🚀 Live Demo

🔗 https://ojhayash45-eng-hi-translator.hf.space/?__theme=system&deep_link=dOemzSUZehE

---

## 🧠 Project Overview

This project implements a sequence-to-sequence Neural Machine Translation model using:

- Helsinki-NLP/opus-mt-en-hi
- Hugging Face Transformers
- PyTorch
- Gradio (for UI)
- Hugging Face Spaces (for deployment)

The application allows users to input English text and receive Hindi translations instantly via a web interface.

---

## 🏗️ Tech Stack

- Python
- PyTorch
- Hugging Face Transformers
- Gradio
- Hugging Face Spaces

---

## ⚙️ Installation & Local Setup

```bash
git clone https://github.com/YOUR_USERNAME/English-Hindi-Translator.git
cd English-Hindi-Translator
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python app.py
http://127.0.0.1:7860
📂 Project Structure
English-Hindi-Translator/
│
├── app.py
├── requirements.txt
└── README.md

🎯 Key Features

Real-time English to Hindi translation

Transformer-based seq2seq model

Clean interactive UI

Cloud deployment via Hugging Face Spaces

Lightweight PyTorch implementation

📌 Model Details

Model: Helsinki-NLP/opus-mt-en-hi

Architecture: MarianMT (Encoder-Decoder)

Framework: PyTorch

Task: Neural Machine Translation

🏆 Deployment

Deployed on Hugging Face Spaces with automatic model loading and real-time inference.
