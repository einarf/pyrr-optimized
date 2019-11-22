# pyrr-optimized

*WORK IN PROGRESS AND PURELY EXPERIMENTAL*

An optimized subset of Pyrr's features. Pyrr is a fantastic library,
but for us doing realtime OpenGL rendering it can be unnecessarily slow
causing frame rate issues.

Pyrr is a 3D mathematical functions using the power of NumPy.
https://github.com/adamlwgriffiths/Pyrr

# Some differences in this fork

* All types will use 32bit floats by default unless a different
  `dtype` is passed in.
* We currently only support a small subset of the Pyrr library
* Expect less sanity checking in input variables and initializers

# Performance comparison

Some initial numbers to compare. These might be outdated fairly quick

```
function                            Pyrr         optimized    improvement %
---------------------------------------------------------------------------
Matrix33.from_list                  4.7609       5.047        -5.67 %
Matrix33.identity                   5.489        3.3605       63.34 %
Matrix44.mult                       13.5246      2.7105       398.97 %
Matrix44.perspective_projection     9.6313       7.9409       21.29 %
```