def get_earlier_events_for_broadcast_event(broadcast_event_id):
    """
    This is used to build up the references list.
    """
    this_event = BroadcastEvent.query.get(broadcast_event_id)
    return BroadcastEvent.query.filter(BroadcastEvent.broadcast_message_id == this_event.broadcast_message_id, BroadcastEvent.sent_at < this_event.sent_at).order_by(BroadcastEvent.sent_at.asc()).all()