import numpy as np


class Matrix44(np.ndarray):
    """float32 4x4 matrix"""

    def __new__(cls, value=None, dtype='f4'):
        if value is not None:
            if not isinstance(value, np.ndarray):
                obj = np.array(value, dtype=dtype)
                return super().__new__(cls, shape=(4, 4), buffer=obj, dtype=dtype)

        # Otherwise simply create an empty 4 x 4 matrix
        return np.zeros((4, 4), dtype=dtype).view(cls)

    @classmethod
    def identity(cls, dtype='f4'):
        return np.identity(4, dtype=dtype).view(cls)

    @classmethod
    def perspective_projection(cls, fovy, aspect, near, far, dtype='f4'):
        ymax = near * np.tan(fovy * np.pi / 360.0)
        xmax = ymax * aspect

        A = (xmax + -xmax) / (xmax - -xmax)
        B = (ymax + -ymax) / (ymax - -ymax)
        C = -(far + near) / (far - near)
        D = -2. * far * near / (far - near)
        E = 2. * near / (xmax - -xmax)
        F = 2. * near / (ymax - -ymax)

        return np.array((
            (  E, 0., 0., 0.),
            ( 0.,  F, 0., 0.),
            (  A,  B,  C,-1.),
            ( 0., 0.,  D, 0.),
        ), dtype=dtype).view(cls)
