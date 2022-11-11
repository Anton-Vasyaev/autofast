import dependencies
# python
from dataclasses import dataclass
from typing import Any, Set, Dict, List, TypeVar, Generic, cast
from abc import ABC, abstractmethod
# project
from fastdi.reflection.data import ClassMetaInfo
from fastdi.reflection.meta import get_class_meta_info

from auxiliary import print_class_meta_info

T = TypeVar('T')
V = TypeVar('V')
K = TypeVar('K')


@dataclass
class InheritanceGraphNode:
    meta : ClassMetaInfo
    
    parents : Set[Any]

    children : Set[Any]

    visit : bool

    def __hash__(self):
        return hash(self.meta)


@dataclass
class InheritanceGraph:
    edges : Dict[ClassMetaInfo, InheritanceGraphNode]


    def clear_visits(self):
        for meta, edge in self.edges.items():
            edge.visit = False


def build_visit_node(meta : ClassMetaInfo, graph : InheritanceGraph):
    if not meta in graph.edges:
        for parent_any in meta.parents:
            parent = cast(ClassMetaInfo, parent_any)
            build_visit_node(parent, graph)

        node = InheritanceGraphNode(
            meta,
            set(),
            set(),
            dict()
        )

        for parent_any in meta.parents:
            parent = cast(ClassMetaInfo, parent_any)
            parent_node = graph.edges[parent]

            node.parents.add(parent_node)

            parent_node.children.add(node)

        graph.edges[meta] = node
        


def build_graph(meta : ClassMetaInfo) -> InheritanceGraph:
    graph = InheritanceGraph(dict())

    build_visit_node(meta, graph)

    return graph


def __validate_node_transitive_inheritance_way(node : InheritanceGraphNode, ancestor : InheritanceGraphNode):
    for parent in node.parents:
        if parent == ancestor:
            raise Exception(
                f'Error. Transitive inheritance from ancestor.'
                f'{node.meta} <- {ancestor.meta}'
            )

        for ancestor_parent in ancestor.parents:
            __validate_node_transitive_inheritance_way(node, ancestor_parent)


def __validate_node_transitive_inheritance(node : InheritanceGraphNode):
    for parent_any in node.parents:
        parent = cast(InheritanceGraphNode, parent_any)
        for ancestor_any in parent.parents:
            ancestor = cast(InheritanceGraphNode, ancestor_any)

            __validate_node_transitive_inheritance_way(node, ancestor)

        __validate_node_transitive_inheritance(parent)


def validate_transitive_inheritance(graph : InheritanceGraph):
    for meta, edge in graph.edges.items():
        __validate_node_transitive_inheritance(edge)




class DataPrinter(Generic[T]):
    @abstractmethod
    def print_data(self):
        raise NotImplementedError()


class DataProvider(DataPrinter[T], ABC):
    @abstractmethod
    def provide_data(self) -> T:
        raise NotImplementedError()


    def print_data(self):
        print(self.provide_data())


class DataAccumulator(DataProvider[T], ABC):
    @abstractmethod
    def accumulate_data(self, data : T):
        raise NotImplementedError()



class StringHandler(DataAccumulator[str], DataPrinter[str]):
    data : str

    def __init__(self, data : str):
        self.data = data


    def provide_data(self) -> str:
        return self.data

    
    def accumulate_data(self, data : str):
        self.data += data



if __name__ == '__main__':
    cls_info = get_class_meta_info(StringHandler)

    graph = build_graph(cls_info)

    for meta, edge in graph.edges.items():
        print(f'{edge.meta.type}:')
        print('\tparents:', end='')
        for parent_any in edge.parents:
            parent = cast(InheritanceGraphNode, parent_any)

            print(f'{parent.meta.type} ', end='')
        print()

        print('\tchildrens:', end='')
        for parent_any in edge.children:
            parent = cast(InheritanceGraphNode, parent_any)

            print(f'{parent.meta.type} ', end='')
        print()
