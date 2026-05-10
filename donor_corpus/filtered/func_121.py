def main():
    gens = [('ToPython Exception Helper', gen_topython_helper), ('Exception Factories', factory_gen), ('Python New-Style Exceptions', newstyle_gen), ('builtin exceptions', builtin_gen)]
    for e in pythonExcs:
        gens.append((get_clr_name(e), gen_one_exception_maker(e)))
    return generate(*gens)