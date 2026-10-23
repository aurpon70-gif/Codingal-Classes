from abc import ABC, abstractmethod
from modulefinder import test

class Absclass(ABC):

    def print(self,x):
        print("Passed value: ", x)

    @abstractmethod
    def task(self):
        print("We're in the Abstract class")

class test_class(Absclass):

    def task(self):
        print("We're in the test class")

test_obj = test_class()
test_obj.task()
test_obj.print(100)