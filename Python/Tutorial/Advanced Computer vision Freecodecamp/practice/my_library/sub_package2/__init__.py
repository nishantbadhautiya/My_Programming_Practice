print("Hii, I am in sub package 2")
from sub_package2.sub_module4 import divide
def my_func(): 
    print("This is a temp my function") 
__all__ = ['sub_module3', 'divide', 'my_func']
