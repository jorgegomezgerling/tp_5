# 1. Cree una clase bajo el patrón cadena de responsabilidad donde los números del 1 al 100 sean pasados a las clases subscriptas en secuencia, aquella que identifique la necesidad de consumir el número lo hará y caso contrario lo pasará al siguiente en la cadena. Implemente una clase que consuma números primos y otra números pares. Puede ocurrir que un número no sea consumido por ninguna clase en cuyo caso se marcará como no consumido.

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chain.
"""


class PrimeHandler(AbstractHandler):
    def handle(self, request) -> Optional[str]:
        number = int(request)
        if self.is_prime(number):
            return f"Prime handler consumed number {number}"
        else:
            return super().handle(request)

    def is_prime(self, number) -> bool:
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True


class EvenHandler(AbstractHandler):
    def handle(self, request) -> Optional[str]:
        number = int(request)
        if self.is_even(number):
            return f"Even handler consumed number {number}"
        else:
            return super().handle(request)

    def is_even(self, number) -> bool:
        return number % 2 == 0


def client_code(handler: Handler) -> None:
    """
    The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    """

    for number in range(1, 101):
        result = handler.handle(number)
        if result:
            print(result)
        else:
            print(f"Number {number} was not consumed.")


if __name__ == "__main__":
    prime_handler = PrimeHandler()
    even_handler = EvenHandler()

    prime_handler.set_next(even_handler)

    print("Chain: Prime Handler > Even Handler\n")
    client_code(prime_handler)
    print("\n")
