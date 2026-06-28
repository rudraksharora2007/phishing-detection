import math
import re
from urllib.parse import urlparse
import whois

SUSPICIOUS_KEYWORDS = [
    "login",
    "verify",
    "account",
    "secure",
    "bank",
    "update",
    "password",
    "confirm",
    "paypal",
    "free",
]


def shannon_entropy(text: str) -> float:
    if not text:
        return 0.0
    probabilities = [text.count(c) / len(text) for c in set(text)]
    return -sum(p * math.log2(p) for p in probabilities)


def has_ip_address(url: str) -> int:
    return int(bool(re.search(r"https?://(?:\d{1,3}\.){3}\d{1,3}", url)))


def domain_age_days(url: str) -> int:
    try:
        hostname = urlparse(url).netloc
        data = whois.whois(hostname)
        created = data.creation_date
        if isinstance(created, list):
            created = created[0]
        if not created:
            return -1
        return max((__import__("datetime").datetime.utcnow() - created).days, 0)
    except Exception:
        return -1


def extract_features(url: str) -> dict:
    parsed = urlparse(url)
    hostname = parsed.netloc.lower()
    keyword_count = sum(1 for k in SUSPICIOUS_KEYWORDS if k in url.lower())
    special_count = len(re.findall(r"[@_!#$%^&*()<>?/|}{~:]", url))
    redirects = url.count("//") - 1

    return {
        "url_length": len(url),
        "subdomain_count": max(hostname.count(".") - 1, 0),
        "uses_https": int(parsed.scheme == "https"),
        "has_ip": has_ip_address(url),
        "special_char_count": special_count,
        "hyphen_count": url.count("-"),
        "digit_count": sum(ch.isdigit() for ch in url),
        "suspicious_keyword_count": keyword_count,
        "entropy": shannon_entropy(url),
        "redirect_count": max(redirects, 0),
        "domain_age_days": domain_age_days(url),
    }


FEATURE_COLUMNS = [
    "url_length",
    "subdomain_count",
    "uses_https",
    "has_ip",
    "special_char_count",
    "hyphen_count",
    "digit_count",
    "suspicious_keyword_count",
    "entropy",
    "redirect_count",
    "domain_age_days",
]
