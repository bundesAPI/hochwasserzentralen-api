# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from deutschland.hochwasserzentralen.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from deutschland.hochwasserzentralen.model.lage_pegel import LagePegel
from deutschland.hochwasserzentralen.model.lage_pegel_inner import LagePegelInner
