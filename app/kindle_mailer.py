"""
This module implements the functionality to send PDF files as emails intended for Kindle devices.

The main functionality provided by this module is to take a PDF file, package it into an email, and send it to
a specified Kindle email address using the SMTP protocol. The module supports multiple email providers with
configurable SMTP settings.

Attributes:
    EMAIL_PROVIDERS (dict): A dictionary of email provider SMTP configurations.
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename
from email_config import EMAIL_PROVIDERS
def send_pdf_to_kindle(file, filename, kindle_email, sender_email, sender_password,provider):
    """
    Send a PDF file to a specified Kindle email address using the SMTP protocol.

    This function configures and sends an email containing the specified PDF file to the Kindle email
    address provided. The email server and port settings are determined by the provider specified. Gmail
    is used as the default provider if an unrecognized provider is specified.

    Parameters:
        file (bytes): The PDF file content to send.
        filename (str): The name of the PDF file.
        kindle_email (str): The email address associated with the recipient's Kindle device.
        sender_email (str): The email address from which the email will be sent.
        sender_password (str): The password for the sender's email account.
        provider (str): The name of the email provider to use for SMTP settings.

    Returns:
        None

    Raises:
        smtplib.SMTPException: An error occurred during the SMTP transaction.
    """
    config = EMAIL_PROVIDERS.get(provider.lower(), EMAIL_PROVIDERS['gmail']) # made gmail for default provider.

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = kindle_email
    msg['Subject'] = 'Send to Kindle'

    part = MIMEApplication(file, Name=basename(filename))
    part['Content-Disposition'] = f'attachment; filename="{basename(filename)}"'
    msg.attach(part)

    try:
        server = smtplib.SMTP(config['server'], config['port'])
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, [kindle_email], msg.as_string())
    finally:
        server.quit()