# 3. Implemente una clase bajo el patrón observer donde una serie de clases están subscriptas, cada clase espera que su propio ID (una secuencia arbitraria de 4 caracteres) sea expuesta y emitirá un mensaje cuando el ID emitido y el propio coinciden. Implemente 4 clases de tal manera que cada una tenga un ID especifico. Emita 8 ID asegurándose que al menos cuatro de ellos coincidan con ID para el que tenga una clase implementada. 

from __future__ import annotations
from abc import ABC, abstractmethod
from random import choice
from typing import List


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state: int = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("\nSubject: I'm doing something important.")
        self._state = choice(range(10))  # Random state for simplicity

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass


"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""


class ConcreteObserverA(Observer):
    def __init__(self, id: str):
        self.id = id

    def update(self, subject: Subject) -> None:
        if self.id == subject._state:
            print(f"ConcreteObserverA: Reacted to the event with ID: {self.id}")


class ConcreteObserverB(Observer):
    def __init__(self, id: str):
        self.id = id

    def update(self, subject: Subject) -> None:
        if self.id == subject._state:
            print(f"ConcreteObserverB: Reacted to the event with ID: {self.id}")


class IDObserver(Observer):
    """
    IDObserver checks if the emitted ID matches its own ID and reacts accordingly.
    """

    def __init__(self, id: str):
        self.id = id

    def update(self, subject: Subject) -> None:
        if self.id == subject._state:
            print(f"IDObserver: Reacted to the event with ID: {self.id}")


if __name__ == "__main__":
    # The client code.

    subject = ConcreteSubject()

    observer_a = ConcreteObserverA("1234")  # ID for observer A
    subject.attach(observer_a)

    observer_b = ConcreteObserverB("5678")  # ID for observer B
    subject.attach(observer_b)

    id_observers = [IDObserver("2468"), IDObserver("1357"), IDObserver("0000"), IDObserver("7777")]
    # IDs for IDObserver instances

    for observer in id_observers:
        subject.attach(observer)

    # Emitting 8 IDs, ensuring at least four match with IDs for which we have implemented classes.
    for _ in range(8):
        subject.some_business_logic()
