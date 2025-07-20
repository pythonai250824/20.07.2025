
from duck_typeb import B

class A:
    def __init__(self, age):
        self.age = age

a = A(22)

a.size = "XL"

print(a.__dict__)

b = B()
b.foo(a)