import validators
from email_validator import validate_email, EmailNotValidError


def validate_email_input(email: str) -> bool:
    try:
        validate_email(email, check_deliverability=False)
        return True
    except EmailNotValidError:
        return False


def validate_url_input(url: str) -> bool:
    return validators.url(url)
