# app/utils/url_features.py
import re
from urllib.parse import urlparse

def extract_url_features(url: str) -> dict:
    # """
    # Extract 27 features from a URL, matching the training dataset columns.
    # Features that require external APIs return -1 (you can implement them later).
    # """
    features = {}
    
    # Helper to parse domain
    try:
        parsed = urlparse(url)
        domain = parsed.netloc or url.split('/')[2] if '//' in url else url.split('/')[0]
    except:
        domain = url
    
    # 1. Using the IP Address
    ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    features['Using the IP Address'] = 1 if re.match(ip_pattern, domain) else -1
    
    # 2. Long URL (> 75 characters)
    features['Long URL'] = 1 if len(url) > 75 else -1
    
    # 3. URL Shortening Services
    shorteners = ['bit.ly', 'tinyurl', 'goo.gl', 'ow.ly', 'is.gd', 'buff.ly', 't.co', 'short.url']
    features['URL Shortening Services'] = 1 if any(s in url for s in shorteners) else -1
    
    # 4. URL having @ Symbol
    features['URL having @ Symbol'] = 1 if '@' in url else -1
    
    # 5. Redirecting using // (double slash after protocol)
    parts = url.split('://', 1)
    if len(parts) > 1 and parts[1].count('//') > 0:
        features['Redirecting using //'] = 1
    else:
        features['Redirecting using //'] = -1
    
    # 6. Prefix/Suffix with - in Domain
    domain_parts = domain.split('.')
    has_hyphen = any('-' in part for part in domain_parts if part)
    features['Prefix/Suffix with - in Domain'] = 1 if has_hyphen else -1
    
    # 7. Sub Domain and Multi Sub Domains (count)
    if len(domain_parts) > 2:
        features['Sub Domain and Multi Sub Domains'] = len(domain_parts) - 2
    else:
        features['Sub Domain and Multi Sub Domains'] = 0
    
    # 8. HTTPS
    features['HTTPS'] = 1 if url.startswith('https://') else -1
    
    # 9–27: Features that need external data – set to -1 (you can later connect to WHOIS, PageRank APIs)
    other_features = [
        'Domain Registration Length', 'Favicon', 'HTTPS Token in Domain', 'Request URL',
        'URL of Anchor', 'Links in Meta/Script/Link Tags', 'Server Form Handler (SFH)',
        'Submitting to Email', 'Abnormal URL', 'Website Forwarding', 'Status Bar Customization',
        'Using Pop-up Window', 'Age of Domain', 'DNS Record', 'Website Traffic',
        'PageRank', 'Google Index', 'Number of Links Pointing to Page',
        'Statistical-Reports Based Feature'
    ]
    for f in other_features:
        features[f] = -1
    
    return features