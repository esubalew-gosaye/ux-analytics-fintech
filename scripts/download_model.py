from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

# Download and save DistilBERT sentiment model
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.save_pretrained("./sentiment_model")
tokenizer.save_pretrained("./sentiment_model")


import nltk
nltk.download('punkt')
nltk.download('stopwords')