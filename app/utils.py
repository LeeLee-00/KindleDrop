import os
from dotenv import load_dotenv

load_dotenv()

def get_creds():
    base_email = os.getenv('BASE_EMAIL')
    base_pw = os.getenv('BASE_PW')
    return base_email, base_pw