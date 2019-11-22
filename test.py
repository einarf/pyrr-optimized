import timeit
import numpy as np
from pyrr import Matrix44 as _Matrix44
from pyrr_optimized import Matrix44

m1_pyrr = _Matrix44.identity(dtype='f4')
m2_pyrr = _Matrix44.identity(dtype='f4')
m1_opt = Matrix44.identity(dtype='f4')
m2_opt = Matrix44.identity(dtype='f4')


def pyrr_matrix44_from_list():
    _Matrix44([[1.0, 0.0, 0.0, 0.0],
              [0.0, 1.0, 0.0, 0.0],
              [0.0, 0.0, 1.0, 0.0],
              [0.0, 0.0, 0.0, 1.0]], dtype='f4')

def opt_matrix44_from_list():
    Matrix44([[1.0, 0.0, 0.0, 0.0],
              [0.0, 1.0, 0.0, 0.0],
              [0.0, 0.0, 1.0, 0.0],
              [0.0, 0.0, 0.0, 1.0]], dtype='f4')

def pyrr_matrix44_identity():
    _Matrix44.identity(dtype='f4')

def opt_matrix44_identity():
    Matrix44.identity(dtype='f4')

def pyrr_matrix44_mult():
    m1_pyrr * m1_pyrr

def opt_matrix44_mult():
    m1_opt @ m2_opt

def pyrr_matrix44_perspective_projection():
    _Matrix44.perspective_projection(60, 16/9, -1, 1)

def opt_matrix44_perspective_projection():
    Matrix44.perspective_projection(60, 16/9, -1, 1)

opt_matrix44_perspective_projection()

def perf_compare(func_orig, func_opt, number=1_000_000, name='unknown'):
    secs_orig = timeit.timeit(func_orig, number=number)
    secs_opt = timeit.timeit(func_opt, number=number)
    a = round(secs_orig, 4)
    b = round(secs_opt, 4)
    c = round(secs_orig / secs_opt * 100 - 100, 2)
    print(f'{name:<35} {a:<12} {b:<12} {c} %')

print()
print(f"{'function':<35} {'Pyrr':<12} {'optimized':<12} {'improvement %':<12}")
print('-' * 75)

perf_compare(pyrr_matrix44_from_list, opt_matrix44_from_list, name="Matrix33.from_list")
perf_compare(pyrr_matrix44_identity, opt_matrix44_identity, name="Matrix33.identity")
perf_compare(pyrr_matrix44_mult, opt_matrix44_mult, name="Matrix44.mult")
perf_compare(pyrr_matrix44_perspective_projection, opt_matrix44_perspective_projection, name="Matrix44.perspective_projection")
