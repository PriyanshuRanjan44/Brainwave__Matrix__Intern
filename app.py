import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from io import BytesIO

@st.cache_resource
def load_model():
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16
    )
    pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    return pipe

def image_to_bytes(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

st.title("🎨 Text-to-Image Generator")
prompt = st.text_input("Enter your prompt:", "A fantasy forest with glowing mushrooms")

if st.button("Generate"):
    st.info("Generating image...")
    pipe = load_model()
    image = pipe(prompt).images[0]
    st.image(image)
    st.download_button("Download Image", image_to_bytes(image), "generated.png")

