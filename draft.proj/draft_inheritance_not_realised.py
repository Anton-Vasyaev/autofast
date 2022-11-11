from abc import abstractmethod

class A:
    @abstractmethod
    def print_data(self):
        raise NotImplementedError()



class B(A):
    pass


class C(A):
    def print_data(self):
        print('[C] print_data')


class D(B, C):
    pass


if __name__ == '__main__':
    ob = D()
    ob.print_data()