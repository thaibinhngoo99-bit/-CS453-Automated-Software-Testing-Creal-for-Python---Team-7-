def generate_steps_reference():
    steps_by_types = []
    for step_module in STEPS_MODULES:
        name = step_module.__name__.split('.')[-1]
        steps_by_types.append({'name': name, 'module': step_module.__name__, 'base_steps': step_module.base_steps})
    steps_dir = os.path.join(BASE_PATH, 'steps/')
    if not os.path.exists(steps_dir):
        os.makedirs(steps_dir)
    for step_type in steps_by_types:
        _render_and_save_template('steps', 'steps/' + step_type['name'], {'step_type': step_type, 'prepare_docstring': _prepare_docstring})