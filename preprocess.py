import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer

# Cargar datos
df = pd.read_csv("data/Resume.csv")  # Ajusta la ruta según tu estructura

# Procesamiento con spaCy
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

# Aplicar preprocesamiento
df["processed_text"] = df["Resume_str"].apply(preprocess_text)

# Vectorización con TF-IDF
vectorizer = TfidfVectorizer(max_features=1000)
cv_vectors = vectorizer.fit_transform(df["processed_text"])

# Guardar vectores y datos procesados
import pickle
pickle.dump(vectorizer, open("models/tfidf_vectorizer.pkl", "wb"))
pickle.dump(cv_vectors, open("data/cv_vectors.pkl", "wb"))