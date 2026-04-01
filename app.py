import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Test Kaleido + WeasyPrint")

if st.button("Generar PNG de prueba"):
    with st.spinner("Generando..."):
        try:
            df = pd.DataFrame({"mes": ["ene","feb","mar"], "valor": [100, 200, 150]})
            fig = px.bar(df, x="mes", y="valor", title="Test")
            png_bytes = fig.to_image(format="png", width=700, height=400)
            st.success("PNG generado correctamente")
            st.image(png_bytes)
        except Exception as e:
            st.error(f"Error: {e}")
