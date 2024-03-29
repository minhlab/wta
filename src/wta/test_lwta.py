__author__ = "Ian Goodfellow"

import numpy as np

from pylearn2.utils import sharedX

from wta.lwta import lwta

def test_lwta():
    example_input = np.zeros((2, 6))

    # begin block
    example_input[0, 0] = -2.5
    example_input[0, 1] = 1.3 # max
    example_input[0, 2] = 0.9
    # begin block
    example_input[0, 3] = -0.1 # tied for max
    example_input[0, 4] = -0.2
    example_input[0, 5] = -0.1 # tied for max
    # begin block
    example_input[1, 0] = 5.0 #max
    example_input[1, 1] = 4.0
    example_input[1, 2] = 3.0
    # begin block
    example_input[1, 3] = 0.0
    example_input[1, 4] = 1.0
    example_input[1, 5] = 2.0 # max

    output = lwta(sharedX(example_input), block_size=3).eval()

    num_zeros = (output == 0).sum()
    assert num_zeros == 8

    assert np.allclose(output[0, 1], 1.3), output[0, 1]
    assert np.allclose(output[0,3], -0.1) or np.allclose(output[0,5], -0.1)
    assert np.allclose(output[1, 0], 5.0)
    assert np.allclose(output[1, 5], 2.0)
    
    print "Success!"
    
    
if __name__ == "__main__":
    test_lwta()
