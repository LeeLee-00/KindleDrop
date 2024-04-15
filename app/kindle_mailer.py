"""
Implementing email sending funcitonality

Goal of this area is to send emails of kindle pdfs to kindle app.
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename
from email_config import EMAIL_PROVIDERS
def send_pdf_to_kindle(file, filename, kindle_email, sender_email, sender_password,provider):

    config = EMAIL_PROVIDERS.get(provider.lower(), EMAIL_PROVIDERS['gmail']) # made gmail for default provider.

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = kindle_email
    msg['Subject'] = 'Send to Kindle'

    part = MIMEApplication(file, Name=basename(filename))
    part['Content-Disposition'] = f'attachment; filename="{basename(filename)}"'
    msg.attach(part)

    server = smtplib.SMTP(config['server'], config['port'])
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, [kindle_email], msg.as_string())
    server.quit()