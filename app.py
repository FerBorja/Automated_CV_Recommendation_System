import streamlit as st
from recommend import recommend_cvs
import pandas as pd

# Cargar datos
df = pd.read_csv("data/Resume.csv")

# Interfaz
st.title("🔍 HR-AI Match: Recomendador de CVs")
job_description = st.text_area("Descripción del puesto:")

if st.button("Recomendar CVs"):
    if job_description:
        recommended_df = recommend_cvs(job_description, df, top_n=3)
        st.subheader("📄 CVs Recomendados:")
        
        for i, row in recommended_df.iterrows():
            st.write(f"### CV #{i+1} - Categoría: {row['Category']}")
            st.text(row['Resume_str'][:500] + "...")
    else:
        st.warning("Por favor ingresa una descripción del puesto.")