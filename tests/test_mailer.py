# from app.email_config import EMAIL_PROVIDERS

# email_dict = EMAIL_PROVIDERS
from app.kindle_mailer import get_creds

credentials = get_creds()
print(credentials)