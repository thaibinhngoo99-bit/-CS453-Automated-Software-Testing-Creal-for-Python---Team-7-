def create_spam(rcpt, sender='spam@evil.corp', rs=' '):
    """Create a spam."""
    body = SPAM_BODY.format(rcpt=rcpt, sender=sender)
    body += 'fóó bár'
    return create_quarantined_msg(rcpt, sender, rs, body, bspam_level=999.0, content='S')