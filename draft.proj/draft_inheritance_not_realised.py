from abc import abstractmethod

class A:
    def print_data(self):
        print('data')


class B:
    def print_data(self, data : int):
        print(f'data:{data}')


class C(B, A):
    def print_data(self, a : int, b : int):
        print(f'data:{a}, {b}')


if __name__ == '__main__':
    ob : A = C()

    ob.print_data()