import dependencies

# python
from abc    import ABC, abstractmethod
from typing import Generic, TypeVar
# project
from autofast.reflection.meta import get_class_meta_info
from auxiliary import print_class_meta_info

T = TypeVar('T')
V = TypeVar('V')
K = TypeVar('K')
X = TypeVar('X')
Y = TypeVar('Y')
Z = TypeVar('Z')



class IDataProvider(ABC, Generic[T]):
    @abstractmethod
    def provider_data(self, idx : int) -> T:
        raise NotImplementedError()


class IDatasetProvider(ABC, Generic[T, V]):
    @abstractmethod
    def get_data_provider(self) -> IDataProvider[T]:
        pass


class FooAncestor(IDatasetProvider[int, float]):
    int_value : float

    def __init__(
        self,
        int_value : int
    ):
        self.int_value = int_value


class FooFather(FooAncestor):
    float_value : float

    def __init__(
        self,
        int_value   : int,
        float_value : float
    ):
        FooAncestor.__init__(self, int_value)
        self.float_value = float_value



class Foo(FooFather, Generic[T, V]):
    t : T
    v : V

    def __init__(
        self,
        int_value   : int,
        float_value : float, 
        t           : T, 
        v           : V
    ):
        FooFather.__init__(self, int_value, float_value)
        self.t = t
        self.v = v


    def provide_t(self, idx : T) -> T:
        return self.t


    def provide_v(self, idx : V) -> V:
        return self.v


class Bar(Generic[K]):
    k : K

    def __init__(self, k : K):
        self.k = k


    def provide_k(self, idx : K) -> K:
        return self.k


    def accumulate_k(self, idx : K):
        pass

    def accumulate_any_k(self, idx):
        pass


class Pin(Foo[X, Y], Bar[Z], Generic[X, Y, Z]):
    def __init__(
        self,
        int_value   : int,
        float_value : float, 
        t           : X, 
        v           : Y, 
        k           : Z
    ):
        Foo.__init__(self, int_value, float_value, t, v)
        Bar.__init__(self, k)


    def return_value_k(self, val : Z) -> Z:
        return self.k


    def get_x_provider(self) -> IDataProvider[IDataProvider[X]]:
        pass


    def get_y_provider(self) -> IDataProvider[Y]:
        pass


class PinExtension(Pin[int, float, str], Generic[X]):
    pass


class PinInstance(PinExtension[bool]):
    def provide_data(self) -> int:
        pass


class AlgTuple2(Generic[T]):
    v1 : T
    v2 : T

    def __init__(
        self,
        v1 : T,
        v2 : T
    ):
        self.v1 = v1
        self.v2 = v2


class Point2f(AlgTuple2[float], FooFather):
    def __init__(self, x : float, y : float):
        pass




if __name__ == '__main__':
    print('------------------------------')
    print(PinInstance.__dict__)
    meta_info_p = get_class_meta_info(PinInstance)

    
    print_class_meta_info(meta_info_p)
