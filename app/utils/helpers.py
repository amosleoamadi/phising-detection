import re


def is_url(text: str):

    url_pattern = r"(https?://|www\.)"

    return bool(re.search(url_pattern, text))