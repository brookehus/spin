import numpy as np
from system import System
from operators import Operators
from ensemble import Ensemble

class Model(object):
    """
    Create, equilibrate, measure, and build network of model
    """
    def __init__(self):
        self._system = None
        self._observables = None
        self._ensemble = None

    def generate_system(self, T=1, spin=1, geometry=(1,), configuration=None):
        self._system = System(T, spin, geometry, configuration)

    def measure_system(self, J=-1.0):
        self._observables = Operators(self._system._configuration, J)

    def generate_ensemble(self, n_samples=1):
        self._ensemble = Ensemble(self, n_samples)