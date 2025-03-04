import streamlit as st
from kindle_mailer import send_pdf_to_kindle
from email_config import EMAIL_PROVIDERS
"""
This module sets up a basic Streamlit web interface for sending PDFs to Kindle devices.

Users can upload a PDF file, input their Kindle and email details, and select their email provider.
Upon submitting, the PDF is emailed to the specified Kindle address using the selected email provider's SMTP settings.
The interface provides a simple and user-friendly way to send documents directly to Kindle devices.

Run this module with the command: `streamlit run main.py` to launch the web interface in your browser.
"""
def main():
    """
    Main function to render the Streamlit interface and handle file uploads and sending logic.

    This function creates a Streamlit page with the following components:
    - A file uploader for PDFs.
    - Input fields for the user's Kindle email, personal email, and email password.
    - A selection box for choosing the email provider.
    - A button to initiate the sending of the PDF to the Kindle email address.

    Upon clicking the 'Send to Kindle' button, the PDF file is sent using the selected provider's SMTP settings.
    A success message is displayed if the file is uploaded successfully.
    """
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