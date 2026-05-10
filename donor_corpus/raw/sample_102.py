from lk_logger import lk

from examples import t01_simple_examples as t01
from examples import t02_referencing as t02
from examples import t03_fibonacci as t03
from examples import t04_catch_exceptions as t04
from examples import t05_qt_button_click_event as t05
from examples import t06_lambdex_kwargs as t06

""" Rules.zh:

1. 所有模块的待测函数, 都必须以 test_ 开头
2. 所有模块的待测函数, 都必须是无参函数
"""

if __name__ == '__main__':
    with lk.counting(6):
        for mod in [t01, t02, t03, t04, t05, t06]:
            lk.logdx(mod.__name__)
            
            with lk.counting():
                for name in dir(mod):
                    if name.startswith('test_'):
                        func = getattr(mod, name)
                        lk.logax('testing', func.__name__)
                        
                        try:
                            func()
                        except Exception as e:
                            lk.logt('[I1117]', e)
                            continue
