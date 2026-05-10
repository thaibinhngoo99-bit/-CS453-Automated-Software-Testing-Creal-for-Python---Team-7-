def preprocess_f(text, fix_unicode=True, lowercase=True, no_urls=True, no_emails=True, no_phone_numbers=True, no_numbers=True, no_currency_symbols=True, no_punct=True, no_accents=True):
    """Preprocess text."""
    clean_text = preprocess_text(text, fix_unicode=fix_unicode, lowercase=lowercase, no_urls=no_urls, no_emails=no_emails, no_phone_numbers=no_phone_numbers, no_numbers=no_numbers, no_currency_symbols=no_currency_symbols, no_punct=no_punct, no_accents=no_accents)
    return clean_text