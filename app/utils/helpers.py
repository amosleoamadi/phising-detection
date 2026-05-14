from urllib.parse import urlparse
import re

def is_url(text: str):
    pattern = r"^(https?://|www\.)"
    return bool(re.match(pattern, text))


def is_ip_address(url):
    try:
        domain = urlparse(url).netloc or url.split('/')[2]
        # IPv4 pattern
        ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
        return 1 if re.match(ip_pattern, domain) else -1
    except:
        return -1

def is_shortened(url):
    shorteners = ['bit.ly', 'tinyurl.com', 'goo.gl', 'ow.ly', 'is.gd', 'buff.ly']
    return 1 if any(shortener in url for shortener in shorteners) else -1

def count_subdomains(url):
    try:
        domain = urlparse(url).netloc
        parts = domain.split('.')
        # subdomains = parts except last two (for .com/.org etc.)
        if len(parts) > 2:
            return len(parts) - 2
        return 0
    except:
        return 0