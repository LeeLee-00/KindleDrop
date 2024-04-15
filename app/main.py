import streamlit as st
from kindle_mailer import send_pdf_to_kindle
from email_config import EMAIL_PROVIDERS
"""
Basic Streamlit Interface

This code sets up a basic Streamlit page with a file uploader. Run this using the command streamlit run main.py to see the interface in your browser.
"""
def main():
    st.title("Send PDF to Kindle")
    uploaded_file = st.file_uploader("Choose a PDF file to upload to your kindle :)", type="pdf")
    kindle_email = st.text_input("Kindle Email")
    sender_email = st.text_input("Your email")
    sender_password = st.text_input("Your Email Password", type="password")
    provider = st.selectbox("Email Provider", options=list(EMAIL_PROVIDERS.keys()))

    if st.button("Send to Kindle") and uploaded_file is not None:
        send_pdf_to_kindle(uploaded_file.getvalue(), uploaded_file.name,kindle_email, sender_email, sender_password, provider) 
        st.success("File has been uploaded succesfully!")

if __name__ == "__main__":
    main()