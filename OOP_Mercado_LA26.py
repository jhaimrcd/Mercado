from abc import ABC, abstractmethod

class NinjaTurtle(ABC):
    @abstractmethod
    def __init__(self, real_name, alias):
        self.__real_name = real_name
        self.__alias = alias

    @property
    @abstractmethod
    def name(self):
        pass

class Leonardo(NinjaTurtle):
    def __init__(self, real_name, alias):
        super().__init__(real_name, alias)

    @property
    def name(self):
        return self._NinjaTurtle__alias

class Michelangelo(NinjaTurtle):
    def __init__(self, real_name, alias):
        super().__init__(real_name, alias)

    @property
    def name(self):
        return self._NinjaTurtle__alias

class Donatello(NinjaTurtle):
    def __init__(self, real_name, alias):
        super().__init__(real_name, alias)

    @property
    def name(self):
        return self._NinjaTurtle__alias

class Raphael(NinjaTurtle):
    def __init__(self, real_name, alias):
        super().__init__(real_name, alias)

    @property
    def name(self):
        return self._NinjaTurtle__alias

leonardo = Leonardo("Leonardo", "Leo")
michelangelo = Michelangelo("Michelangelo", "Mikey")
donatello = Donatello("Donatello", "Donnie")
raphael = Raphael("Raphael", "Raph")

print(f"Leonardo's alias: {leonardo.name}")
print(f"Michelangelo's alias: {michelangelo.name}")
print(f"Donatello's alias: {donatello.name}")
print(f"Raphael's alias: {raphael.name}")