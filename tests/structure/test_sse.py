# This source code is part of the Biotite package and is distributed
# under the 3-Clause BSD License. Please see 'LICENSE.rst' for further
# information.

import biotite.structure as struc
import biotite.structure.io as strucio
import numpy as np
from os.path import join
from ..util import data_dir
import pytest


def test_sse():
    array = strucio.load_structure(join(data_dir("structure"), "3o5r.mmtf"))
    test_sse = struc.annotate_sse(array, "A")
    ref_sse = (
        "caaaaaacccccccccccccbbbbbccccccbbbbccccccccccccccc"
        "ccccccccccccbbbbbbcccccccaaaaaaaaaccccccbbbbbccccc"
        "ccccccccccccbbbbbbbccccccccc"
    )
    assert "".join(test_sse.tolist()) == ref_sse
