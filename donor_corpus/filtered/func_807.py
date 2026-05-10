def init_smart():
    global SharedPtr

    class SharedPtr(Generic[_S]):
        __module__ = 'smart'
    smart.SharedPtr = SharedPtr
    type_map.update({'smart.Smart.Integer2': int})
    return locals()