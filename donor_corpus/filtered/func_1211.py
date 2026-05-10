def prototype(proto: Callable[Parameters, ReturnType], /, *, runtime: bool=True) -> Callable[Parameters, ReturnType]:
    """
    Prototype decorator acts like a type protection shield
    that validates the parameters specification and return
    type annotation of the function against given prototype.

    If `runtime` parameter is set to True, decorator performs
    prototype validation during runtime using the :class:`Signature`
    class from :module:`inspect` module by comparing function and
    prototype signatures against each other.

    :param proto: prototype function
    :param runtime: when set to True, performs prototype validation during runtime

    :raises PrototypeError:
        When function has incompatible signature for given prototype.
        Exception is raised only when `runtime` argument is set to True.
    """

    def decorator(func: Callable[Parameters, ReturnType], /) -> Callable[Parameters, ReturnType]:
        if runtime is True:
            func_signature = signature(func)
            proto_signature = signature(proto)
            if func_signature.parameters != proto_signature.parameters:
                raise PrototypeError(func, func_signature, proto, proto_signature)
            if func_signature.return_annotation != proto_signature.return_annotation:
                raise PrototypeError(func, func_signature, proto, proto_signature)
        return func
    return decorator