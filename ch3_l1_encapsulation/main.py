class Wizard:
    def __init__(self, name: str, stamina: int, intelligence: int) -> None:
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.health = 100 * self.__stamina
        self.mana = 10 * self.__intelligence
