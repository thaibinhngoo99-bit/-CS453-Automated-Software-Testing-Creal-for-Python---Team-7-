def switch_student_adaptor(batch, model_outputs):
    layers, len, len, batch_size, heads = model_outputs['attention'].shape
    attention = model_outputs['attention'].reshape(layers, batch_size, heads, len, len)
    len, batch_size, d_model = model_outputs['logits'].shape
    logits = model_outputs['logits'].reshape(batch_size, len, d_model)
    layers, len, batch_size, heads, embedding_per_head = model_outputs['values'].shape
    values = model_outputs['values'].reshape(layers, batch_size, heads, len, embedding_per_head)
    return {'logits': model_outputs['pooler_output'], 'counts': model_outputs['counts'], 'attention': attention, 'inputs_mask': batch['attention_mask'], 'route_prob': model_outputs['route_prob'], 'n_dropped': model_outputs['n_dropped'], 'value_relation': values}