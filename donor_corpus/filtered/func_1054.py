def _render_and_save_template(path, dest, context):
    template_path = os.path.join(TEMPLATES_PATH, path + '.tpl')
    destination_path = os.path.join(BASE_PATH, dest + '.md')
    with open(destination_path, 'wt') as dest_file:
        dest_file.write(Template(open(template_path).read()).render(context))