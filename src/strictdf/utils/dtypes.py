"""
Author: Cristian Contrera <cristiancontrera95@gmail.com>
Date: 10/12/2020
License: MIT
"""

import re


__str_check_functions = {
    # check boolean in this forms: [0, 1, .0, .1, 0., 1., true, false, t, f]
    'bool': re.compile('^([.]?0|[.]?1|true|false|f|t){1}[.]?[0]*$'),
    # check int in this forms: [11, -1, 1., -2., .000]
    'int': re.compile('^[-]?([0-9]+[.]?0*|[.]0+)$'),
    # check floats in this forms: [-11.12, -1.2, .1, -.2]
    'float': re.compile('^[-]?([0-9]+[.][0-9]*|[0-9]*[.][0-9]+)$'),
}


def str_check_bool(string: str = ''):
    return __str_check_functions['bool'].match(string.lower())


def str_check_int(string: str = ''):
    return __str_check_functions['int'].match(string)


def str_check_float(string: str = ''):
    return __str_check_functions['float'].match(string)
