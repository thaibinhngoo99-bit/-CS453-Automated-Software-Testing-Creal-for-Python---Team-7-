def init_other():
    import numbers
    type_map.update({'other.ExtendsNoImplicitConversion': Missing('other.ExtendsNoImplicitConversion'), 'other.Number': numbers.Number})
    return locals()