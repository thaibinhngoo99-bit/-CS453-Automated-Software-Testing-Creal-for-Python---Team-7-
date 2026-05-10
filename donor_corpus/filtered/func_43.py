def load_teacher(device):
    teacher_config = AutoConfig.from_pretrained('sentence-transformers/LaBSE')
    teacher_config.output_hidden_states = True
    teacher_config.output_attentions = True
    teacher_config.use_cache = True
    teacher_config.is_decoder = True
    teacher_model = AutoModel.from_pretrained('sentence-transformers/LaBSE', config=teacher_config)
    teacher_model.float()
    teacher_model.to(device=device)
    return teacher_model