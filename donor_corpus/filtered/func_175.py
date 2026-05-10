@contextmanager
def auth_ctx(username, orgname=None):
    _request_ctx_stack.top.current_user = User(id=1, username=username)
    if orgname:
        _request_ctx_stack.top.current_org = Org(id=1, orgname=orgname)
    yield