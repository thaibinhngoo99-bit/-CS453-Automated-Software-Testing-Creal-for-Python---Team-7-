def delete_disconnected_nodes(gd):
    empty_nodes = []
    for k, v in gd.items():
        if len(gd[k].inputs) == 0 and len(gd[k].outputs) == 0 and (len(gd[k].control_inputs) == 0) and (len(gd[k].control_outputs) == 0) and (gd[k].op != 'Placeholder'):
            empty_nodes.append(k)
    for k in empty_nodes:
        del gd[k]