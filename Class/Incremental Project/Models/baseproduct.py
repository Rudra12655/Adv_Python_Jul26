from abc import ABC, abstractmethod
from .metaclass import ProductMeta


class BaseProduct(ABC, metaclass=ProductMeta):

    @abstractmethod
    def display_details(self):
        pass