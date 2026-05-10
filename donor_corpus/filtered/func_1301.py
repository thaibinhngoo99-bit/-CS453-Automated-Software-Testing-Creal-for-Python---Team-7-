def tk_loop(root, ex):
    """
    Checks for messages every half a second
    """
    if ex.msg_list is not None:
        ex.updateConversation()
    root.after(2000, tk_loop, root, ex)