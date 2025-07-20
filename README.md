# 🖼️ Text-to-Image Generator | Stable Diffusion v1.5

A powerful and intuitive **Text-to-Image Generator** leveraging **Stable Diffusion v1.5** to turn natural language prompts into vivid AI-generated visuals. Developed using both **Streamlit** for deployment and **Gradio** for GPU-powered inference via **Google Colab**.

> ✅ Developed as part of the AI/ML Internship at **Brainwave Matrix Solutions**

---

## 🚀 Live on Google Colab (GPU Powered)

Experience fast and accurate image generation via Google Colab + Gradio UI:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PriyanshuRanjan44/Brainwave__Matrix__Intern/blob/main/app_colab.py)

---

## 📌 Features

- 🔮 Natural Language → AI Image Generation
- ⚡ GPU acceleration with Google Colab
- 🧠 Powered by Hugging Face `diffusers`
- 🎛️ Clean and responsive Gradio UI
- 🌐 Lightweight Streamlit app for quick CPU-based deployment

---

## 🧠 Sample Prompts

- "A futuristic city in the sky at golden hour"
- "A majestic lion wearing sunglasses"
- "Cyberpunk Tokyo street, rainy night, neon lights"
- "An astronaut relaxing on Mars with a drink"

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|------------|
| Model | Stable Diffusion v1.5 (via Hugging Face Diffusers) |
| Frameworks | Gradio, Streamlit |
| Backend | Python 3.10+, PyTorch |
| Runtime | Google Colab (GPU), Local (CPU) |

---

## 💻 Local Installation Guide

> For CPU-based image generation using Streamlit.

## 1. Clone the Repository

- git clone https://github.com/PriyanshuRanjan44/Brainwave__Matrix__Intern.git
- cd Brainwave__Matrix__Intern/text-to-image-app

---

## 2. Create a Virtual Environment

- python -m venv venv

---

## 3. Activate the Virtual Environment

### On Windows:

- venv\Scripts\activate

### On Mac/Linux:

- source venv/bin/activate

---

## 4. Install Dependencies

- pip install -r requirements.txt

---

## 5. Run the App

- streamlit run app.py

---

## 📀 Google Colab (GPU)

> For faster generation using CUDA acceleration and Gradio interface.

## 🔧 Setup Instructions in Colab

- !pip install diffusers transformers accelerate safetensors gradio
- !python app_colab.py

- You’ll receive a Gradio-hosted link to use the UI right from your browser.

---

## ☁️ Deployments

## 🚀 Streamlit Cloud (CPU)

- Upload to GitHub

- Connect with streamlit.io/cloud

- Set app.py as the entry point

---

## 📁 Project Structure

- text-to-image-app/
- ├── app.py # Streamlit version (CPU)
- ├── app_colab.py # Gradio + Colab (GPU)
- ├── requirements.txt # Python dependencies
- ├── README.md # Project documentation
- └── .gitignore # Git exclusions

---

## ✅ Task Completion

- This project was successfully completed under the AI/ML Internship at Brainwave Matrix Solutions, as a demonstration of real-world application of generative models using Hugging Face Diffusers.

- 🏢 Brainwave Matrix Solutions

- 📅 July 2025

- 🎯 Deliverable: Text-to-Image Generator with dual deployment (CPU + GPU)

---

## 🙌 Acknowledgements

- 🤗 Hugging Face Diffusers

- 🧠 PyTorch + Transformers

- 🎨 Stability.AI for Stable Diffusion model

- 🖼️ Gradio and Streamlit for deployment

---

## 📃 License

- MIT License — feel free to use, modify, and distribute for personal and educational purposes.
---

## 👤 Author
### Priyanshu Ranjan
- 🔗 https://www.linkedin.com/in/priyanshu-ranjan-424087366?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app
- 📧 priyanshuranjan343@gmail.com


