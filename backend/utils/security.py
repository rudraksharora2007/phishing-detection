import re
from urllib.parse import urlparse


def sanitize_input(value: str) -> str:
    value = value.strip()
    return re.sub(r"[\x00-\x1f\x7f]", "", value)


def normalize_url(url: str) -> str:
    if not url.startswith(("http://", "https://")):
        url = f"http://{url}"
    parsed = urlparse(url)
    return parsed.geturl()
