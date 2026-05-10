import pytest
import copy
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).absolute().parent.parent))
from swimmer_abm.model import Model

def test_init():
    model = Model(nswimmers=3)
    assert len(model.swimmers) == 3
    
def test_step():
    model = Model(nswimmers=1)
    swimmer = copy.deepcopy(model.swimmers[0])
    dt = 1
    swimmer.swim(dt)
    model.step(dt)
    assert swimmer.pos == model.swimmers[0].pos

def test_repr():
    model = Model(nswimmers=1)
    assert isinstance(str(model), str)
