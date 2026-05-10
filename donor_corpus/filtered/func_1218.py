async def log_error(ctx: InteractionContext | ComponentContext, error: Exception, situation: str) -> None:
    """Respond to the context and log error"""
    if not ctx.responded:
        await ctx.send(embeds=embed_message('Error', f'Sorry, something went wrong\nThe Error has been logged and will be worked on', str(error)))
    logger = logging.getLogger(situation)
    logger.exception(f"InteractionID '{ctx.interaction_id}' - Error {error} - Traceback: \n{''.join(traceback.format_tb(error.__traceback__))}")
    raise error