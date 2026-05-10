@transactional
def create_broadcast_provider_message(broadcast_event, provider):
    broadcast_provider_message_id = uuid.uuid4()
    provider_message = BroadcastProviderMessage(id=broadcast_provider_message_id, broadcast_event=broadcast_event, provider=provider, status=BroadcastProviderMessageStatus.SENDING)
    db.session.add(provider_message)
    db.session.commit()
    provider_message_number = None
    if provider == BroadcastProvider.VODAFONE:
        provider_message_number = BroadcastProviderMessageNumber(broadcast_provider_message_id=broadcast_provider_message_id)
        db.session.add(provider_message_number)
        db.session.commit()
    return provider_message