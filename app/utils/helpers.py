import re

def is_url(text: str):
    pattern = r"^(https?://|www\.)"
    return bool(re.match(pattern, text))