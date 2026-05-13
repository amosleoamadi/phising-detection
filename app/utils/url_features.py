import re


def extract_url_features(url):

    features = {}

    features["url_length"] = len(url)

    features["has_https"] = 1 if "https" in url else 0

    features["dot_count"] = url.count(".")

    features["hyphen_count"] = url.count("-")

    features["at_symbol"] = 1 if "@" in url else 0

    features["digit_count"] = sum(char.isdigit() for char in url)

    ip_pattern = r"(\d{1,3}\.){3}\d{1,3}"

    features["has_ip"] = 1 if re.search(ip_pattern, url) else 0

    return features