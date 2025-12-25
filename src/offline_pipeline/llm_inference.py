# llm_inference.py
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"

def load_generator(model_name=MODEL_NAME):
    # Load tokenizer + model onto GPU (auto device_map + fp16)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        torch_dtype=torch.float16
    )
    gen = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0)
    return gen

def run_generation(gen, prompt, max_new_tokens=300):
    return gen(prompt, max_new_tokens=max_new_tokens, do_sample=False)[0]["generated_text"]
