class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(B):
    pass

c1 = C()
c1.show()