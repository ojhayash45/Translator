import gradio as gr
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


#Load Model

MODEL_NAME = "Helsinki-NLP/opus-mt-en-hi"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


# Translation Function


def translate_text(text):
    if text.strip() == "":
        return "Please enter some text."

    inputs = tokenizer(text, return_tensors="pt", padding=True)

    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=128)

    translated_text = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return translated_text

# Gradio Interface

interface = gr.Interface(
    fn=translate_text,
    inputs=gr.Textbox(lines=4, placeholder="Enter English text here"),
    outputs="text",
    title="English to Hindi Translator",
    description="Neural Machine Translation using MarianMT"
)

if __name__ == "__main__":
    interface.launch()
