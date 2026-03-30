import streamlit as st
from weasyprint import HTML

st.title("Test WeasyPrint")
st.write("Pulsa el botón para generar un PDF de prueba.")

if st.button("Generar PDF"):
    with st.spinner("Generando PDF..."):
        try:
            with open("test_html", "r", encoding="utf-8") as f:
                html_string = f.read()
            pdf_bytes = HTML(string=html_string).write_pdf()
            st.success("PDF generado correctamente.")
            st.download_button(
                label="Descargar PDF",
                data=pdf_bytes,
                file_name="test_weasyprint.pdf",
                mime="application/pdf"
            )
        except Exception as e:
            st.error(f"Error: {e}")
