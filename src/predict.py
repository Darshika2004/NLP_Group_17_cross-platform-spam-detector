import torch
import re
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Path to the fine-tuned model saved in Drive
MODEL_PATH = "../models/bert_model"

# Load tokenizer and pre-trained model
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
model.eval()

# Predefined suspicious keywords and URL patterns
SUSPICIOUS_KEYWORDS = ["FREE", "Winner", "Crypto", "Lottery", "Click Here", "Urgent", "Claim"]
URL_PATTERN = r"(https?://[^\s]+|www\.[^\s]+|bit\.ly[^\s]+)"

def predict_spam(text):
    highlighted_text = text
    # Highlight keywords found in the input text
    for kw in SUSPICIOUS_KEYWORDS:
        if re.search(re.escape(kw), highlighted_text, re.IGNORECASE):
            highlighted_text = re.sub(f"({re.escape(kw)})", r"<mark style='background-color: #fef08a;'>\1</mark>", highlighted_text, flags=re.IGNORECASE)
    
    # Tokenize input text for the model
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
        probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1).squeeze()
    
    # Calculate ham and spam probabilities
    ham_prob = float(probabilities[0]) * 100
    spam_prob = float(probabilities[1]) * 100
    is_spam = spam_prob > ham_prob
    confidence = spam_prob if is_spam else ham_prob
    
    return is_spam, confidence, ham_prob, spam_prob, highlighted_text
