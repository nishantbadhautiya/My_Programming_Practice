print("Hii, I am in sub package 1")
from .sub_module1 import sum
def initfunc(): 
    print("Init function called") 

__all__ = ['sub_module2', 'initfunc', 'sum']