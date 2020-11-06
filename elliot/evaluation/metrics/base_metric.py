"""
This is the implementation of the Precision metric.
It proceeds from a user-wise computation, and average the values over the users.
"""

__version__ = '0.1'
__author__ = 'XXX'

import typing as t
from abc import ABC, abstractmethod


class BaseMetric(ABC):
    """
    This class represents the implementation of the Precision recommendation metric.
    Passing 'Precision' to the metrics list will enable the computation of the metric.
    """

    def __init__(self, recommendations, config, params, evaluation_objects):
        """
        Constructor
        :param recommendations: list of recommendations in the form {user: [(item1,value1),...]}
        :param cutoff: numerical threshold to limit the recommendation list
        :param relevant_items: list of relevant items (binary) per user in the form {user: [item1,...]}
        """
        self._recommendations: t.List[t.Tuple[int, float]] = recommendations
        self._config = config
        self._params = params
        self._evaluation_objects = evaluation_objects

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def eval(self):
        pass
