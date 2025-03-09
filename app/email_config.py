"""
SMTP - (Simple Mail Transfer Protocol)
"""

EMAIL_PROVIDERS = {
    'gmail': {
        'server': 'smtp.gmail.com',
        'port': 587
    },
    'outlook': {
        'server': 'smtp.office365.com',  # updated server address
        'port': 587
    },
    'yahoo': {
        'server':'smtp-mail.yahoo.com',
        'port': 587
    }
}