"""
This module implements the functionality to send PDF files as emails intended for Kindle devices.

The main functionality provided by this module is to take a PDF file, package it into an email, and send it to
a specified Kindle email address using the SMTP protocol. The module supports multiple email providers with
configurable SMTP settings.

Attributes:
    EMAIL_PROVIDERS (dict): A dictionary of email provider SMTP configurations.
"""

from dotenv import load_dotenv  # added import
load_dotenv()  # load variables from .env

import smtplib
import socket
import os
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename
from email_config import EMAIL_PROVIDERS
from utils import get_creds  # added import

def send_pdf_to_kindle(file, filename, kindle_email, sender_email = None, sender_password = None, provider = 'outlook'):
    """
    Send a PDF file to a specified Kindle email address using the SMTP protocol.

    This function configures and sends an email containing the specified PDF file to the Kindle email
    address provided. The email server and port settings are determined by the provider specified. Gmail
    is used as the default provider if an unrecognized provider is specified.

    Parameters:
        file (bytes): The PDF file content to send.
        filename (str): The name of the PDF file.
        kindle_email (str): The email address associated with the recipient's Kindle device.
        sender_email (str): The email address from which the email will be sent. (removed this line as it is not needed)
        sender_password (str): The password for the sender's email account. (removed this line as it is not needed)
        provider (str): The name of the email provider to use for SMTP settings.

    Returns:
        None

    Raises:
        smtplib.SMTPException: An error occurred during the SMTP transaction.
    """
    config = EMAIL_PROVIDERS.get(provider.lower(), EMAIL_PROVIDERS[provider]) # made gmail for default provider.
    print(f'Config: {config}')
    msg = MIMEMultipart()
    # msg['From'] = sender_email - removed this line as it is not needed.
    print(f'Kindle email: {kindle_email}')
    msg['To'] = kindle_email
    msg['Subject'] = 'Send to Kindle'

    part = MIMEApplication(file, Name=basename(filename))
    part['Content-Disposition'] = f'attachment; filename="{basename(filename)}"'
    msg.attach(part)

    if sender_email is None or sender_password is None:
        sender_email_env, sender_password_env = get_creds()
        print(f'sender creds post get creds function: {sender_email_env, sender_password_env}')  # use get_creds() from utils.py
        sender_email = sender_email or sender_email_env
        sender_password = sender_password or sender_password_env
        if not sender_email:
            raise ValueError("BASE_EMAIL must be set in environment variables")
        if not sender_password:
            raise ValueError("BASE_PW must be set in environment variables")

    try: # TODO: An automated kindle drop user email and password where the user would only have to send their kindle email address. (Don't see the point of having this to be user inpurt int he first place....)
        server = smtplib.SMTP(config['server'], config['port'])
        fqdn = socket.getfqdn()  # get a valid FQDN
        server.ehlo(fqdn)  # use valid FQDN instead of "localhost"
        server.starttls()
        server.ehlo(fqdn)  # re-identify after TLS
        print(f'Server: {server}')
        server.login(sender_email, sender_password)  # enable SMTP authentication
        server.sendmail(sender_email, [kindle_email], msg.as_string())
    finally:
        server.quit()
