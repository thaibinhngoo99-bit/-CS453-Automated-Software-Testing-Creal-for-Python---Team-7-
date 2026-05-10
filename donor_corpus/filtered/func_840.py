def create_quarantined_msg(rcpt, sender, rs, body, **kwargs):
    """Create a quarantined msg."""
    msgrcpt = MsgrcptFactory(rs=rs, rid__email=rcpt, rid__domain='com.test', mail__sid__email=smart_bytes(sender), mail__sid__domain='', **kwargs)
    QuarantineFactory(mail=msgrcpt.mail, mail_text=smart_bytes(SPAM_BODY.format(rcpt=rcpt, sender=sender)))
    return msgrcpt