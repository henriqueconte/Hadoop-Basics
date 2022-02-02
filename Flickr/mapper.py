#!/usr/bin/python3

import sys
from country import *


country.init_pays()

for line in sys.stdin:
    line = line.strip()
