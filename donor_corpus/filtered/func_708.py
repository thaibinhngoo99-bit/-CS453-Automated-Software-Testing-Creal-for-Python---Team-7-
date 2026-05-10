def main(opts):
    import logging
    from gio import config
    from gio import file_mag
    from gio import global_task
    import os
    _d_inp = config.get('conf', 'input')
    _d_ref = config.get('conf', 'refer', _d_inp)
    _f_mak = file_mag.get(os.path.join(_d_inp, 'tasks.txt'))
    _ts = global_task.load(_f_mak)
    from gio import multi_task
    _rs = multi_task.run(_task, [(_t, os.path.join(_d_inp, 'data'), os.path.join(_d_ref, 'data'), opts) for _t in multi_task.load(_ts, opts)], opts)
    print('processed', len([_r for _r in _rs if _r]), 'tiles')