import numpy as np

def clip_gradients(g, max_norm):
    g = np.asarray(g)
    norm = np.linalg.norm(g)

    res = g.copy() * (max_norm) / norm if norm > max_norm else g
    return res
    """
    Clip gradients using global norm clipping.
    """
    # Write code here
    pass