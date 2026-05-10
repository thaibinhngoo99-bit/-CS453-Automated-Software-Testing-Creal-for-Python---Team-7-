def _get_testable_interactive_backends():
    backends = []
    for deps, backend in [(['cairo', 'gi'], 'gtk3agg'), (['cairo', 'gi'], 'gtk3cairo'), (['PyQt5'], 'qt5agg'), (['PyQt5', 'cairocffi'], 'qt5cairo'), (['PySide2'], 'qt5agg'), (['PySide2', 'cairocffi'], 'qt5cairo'), (['tkinter'], 'tkagg'), (['wx'], 'wx'), (['wx'], 'wxagg'), (['matplotlib.backends._macosx'], 'macosx')]:
        reason = None
        missing = [dep for dep in deps if not importlib.util.find_spec(dep)]
        if sys.platform == 'linux' and (not os.environ.get('DISPLAY')):
            reason = '$DISPLAY is unset'
        elif missing:
            reason = '{} cannot be imported'.format(', '.join(missing))
        elif backend == 'macosx' and os.environ.get('TF_BUILD'):
            reason = 'macosx backend fails on Azure'
        if reason:
            backend = pytest.param(backend, marks=pytest.mark.skip(reason=f'Skipping {backend} because {reason}'))
        elif backend.startswith('wx') and sys.platform == 'darwin':
            backend = pytest.param(backend, marks=pytest.mark.xfail(reason='github #16849'))
        backends.append(backend)
    return backends