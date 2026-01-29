#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        """
            Return the animal's sound as a text string.
         """
        pass


class Dog(Animal):
    """
    Docstring for Dog
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Docstring for Cat
    """

    def sound(self):
        return "Meow"
