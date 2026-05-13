import re
from urllib.parse import urlparse


def extract_url_features(url):

    features = {}

    # URL length
    features["url_length"] = len(url)

    # HTTPS check
    features["has_https"] = 1 if "https" in url else 0

    # Count dots
    features["dot_count"] = url.count(".")

    # Count hyphens
    features["hyphen_count"] = url.count("-")

    # Count @ symbols
    features["at_symbol"] = 1 if "@" in url else 0

    # Count digits
    features["digit_count"] = sum(char.isdigit() for char in url)

    # Check for IP address
    ip_pattern = r"(\d{1,3}\.){3}\d{1,3}"

    features["has_ip"] = 1 if re.search(ip_pattern, url) else 0

    return features