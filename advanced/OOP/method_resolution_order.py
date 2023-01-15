# MRO = Method Resolution Order

class A:
    num = 10

# inherit from class A
class B(A):
    pass

# inherit from class A
class C(A):
    num = 1

# inherit from class B and C
class D(B, C):
    pass

# mro() = check the order of inherited class
print(D.mro())