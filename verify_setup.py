"""
Quick check that pandas, numpy, matplotlib, and jupyter are installed
and importable, and prints each package's version number.

Run with: python3 verify_setup.py
"""

import pandas
import numpy
import matplotlib
import jupyter_core  # jupyter itself has no __version__; jupyter_core does

print("pandas:", pandas.__version__)
print("numpy:", numpy.__version__)
print("matplotlib:", matplotlib.__version__)
print("jupyter_core:", jupyter_core.__version__)
