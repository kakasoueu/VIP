#! /usr/bin/env python

"""
"""

from __future__ import division

__author__ = 'C. Gomez @ ULg'
__all__ = ['thresholding']

import numpy as np


def thresholding(array, threshold, mode):
    x = array.copy()
    if mode=='soft':
        j = np.abs(x) <= threshold
        x[j] = 0
        j = np.abs(x) > threshold
        x[j] = x[j] - np.sign(x[j])*threshold
    elif mode=='hard':
        j = np.abs(x) < threshold
        x[j] = 0
    elif mode=='greater':
        j = x < threshold
        x[j] = 0
    elif mode=='less':
        j = x > threshold
        x[j] = 0
    return x