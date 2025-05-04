from sklearn.metrics.pairwise import cosine_similarity
import pickle

def recommend_cvs(job_description, df, top_n=5):
    # Cargar vectores y vectorizador
    vectorizer = pickle.load(open("models/tfidf_vectorizer.pkl", "rb"))
    cv_vectors = pickle.load(open("data/cv_vectors.pkl", "rb"))
    
    # Vectorizar la descripción del puesto
    job_vector = vectorizer.transform([job_description])
    
    # Calcular similitud
    similarities = cosine_similarity(job_vector, cv_vectors)
    top_indices = similarities.argsort()[0][-top_n:][::-1]
    
    return df.iloc[top_indices]  # Devuelve el DataFrame completo, no solo la columna