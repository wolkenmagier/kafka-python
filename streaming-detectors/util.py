import datetime
import dateutil
import math
import os
import pandas
import pprint
import sys

try:
  import simplejson as json
except ImportError:
  import json



def getProbationPeriod(probationPercent, fileLength):
  """Return the probationary period index."""
  return min(
    math.floor(probationPercent * fileLength),
    probationPercent * 5000)
