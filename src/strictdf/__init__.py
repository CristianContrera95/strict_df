"""
Author: Cristian Contrera <cristiancontrera95@gmail.com>
Date: 10/12/2020
License: MIT
"""

from .StrictDataFrame import StrictDataFrame
from .utils.helpers import is_spark

if is_spark():
    import findspark

    findspark.init()
