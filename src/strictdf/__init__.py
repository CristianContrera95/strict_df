"""
Author: Cristian Contrera <cristiancontrera95@gmail.com>
Date: 10/12/2020
License: MIT
"""

from .StrictDataFrame import StrictDataFrame
try:
    import findspark
    findspark.init()
except:
    pass
