# 2. Implemente una clase bajo el patrón iterator que almacene una cadena de caracteres y permita recorrerla en sentido directo y reverso. 

from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any


class BidirectionalIterator(Iterator):
    """
    Concrete Iterator class that allows iterating over a string in both forward
    and reverse directions.
    """

    def __init__(self, collection: str) -> None:
        self._collection = collection
        self._index = 0
        self._reverse = False

    def __iter__(self) -> BidirectionalIterator:
        return self

    def __next__(self) -> Any:
        if self._index < len(self._collection):
            if not self._reverse:
                result = self._collection[self._index]
                self._index += 1
            else:
                result = self._collection[-(self._index + 1)]
                self._index += 1
            return result
        else:
            raise StopIteration

    def reverse(self) -> None:
        """
        Method to reverse the direction of iteration.
        """
        self._reverse = not self._reverse


class IterableString(Iterable):
    """
    Concrete Iterable class that holds a string and provides methods to create
    iterators for forward and reverse iteration.
    """

    def __init__(self, string: str) -> None:
        self._string = string

    def __iter__(self) -> BidirectionalIterator:
        """
        Method to create a forward iterator.
        """
        return BidirectionalIterator(self._string)

    def reverse_iterator(self) -> BidirectionalIterator:
        """
        Method to create a reverse iterator.
        """
        iterator = BidirectionalIterator(self._string)
        iterator.reverse()
        return iterator


def main():
    string = "Hello, world!"
    iterable_string = IterableString(string)

    print("Forward iteration:")
    forward_iterator = iter(iterable_string)
    for char in forward_iterator:
        print(char, end=" ")
    print()

    print("Reverse iteration:")
    reverse_iterator = iterable_string.reverse_iterator()
    for char in reverse_iterator:
        print(char, end=" ")
    print()


if __name__ == "__main__":
    main()
