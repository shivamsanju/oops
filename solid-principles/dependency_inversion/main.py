'''
1. High-level modules should not depend on low-level modules.
Both should depend on abstractions.

2. Abstractions should not depend on details. 
Details should depend on abstractions.
'''

from abc import ABC, abstractmethod
from enum import Enum

class Relationship(Enum):
    CHILD = 0
    PARENT = 1
    SIBLING = 2

class Person:
    def __init__(self, name: str) -> None:
        self.name = name


class Relationships:
    def __init__(self) -> None:
        self.relations: list[tuple[Person, Relationship, Person]] = []

    def add_child_to_parent(self, parent: Person, child: Person) -> None:
        self.relations.append((parent, Relationship.CHILD, child))

class Research:
    def __init__(self, relationships: Relationships) -> None:
        relations = relationships.relations
        for r in relations:
            if r[0].name == 'John' and r[1] == Relationship.CHILD:
                print(f"John has a child {r[2].name}")
                


'''
The problem above is that the high level module Research depends on the 
implementation of relations inside Relationships. If we change it from a list
to any other data structure, the code will break.

The solution is to move the implementation of finding child to an abstraction.
'''

class RelationshipBrowser(ABC):
    @abstractmethod
    def get_all_childrens_of(self, name: str) -> list[Person]:
        pass


class Relationships2(RelationshipBrowser):
    def __init__(self) -> None:
        self.relations: list[tuple[Person, Relationship, Person]] = []

    def add_child_to_parent(self, parent: Person, child: Person) -> None:
        self.relations.append((parent, Relationship.CHILD, child))

    def get_all_childrens_of(self, name: str) -> list[Person]:
        childrens = []
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.CHILD:
                childrens.append(r[2])
        return childrens
    

class Research:
    def __init__(self, relationships: RelationshipBrowser) -> None:
        childrens = relationships.get_all_childrens_of("John")
        for child in childrens:
            print(f"John has a child {child.name}")