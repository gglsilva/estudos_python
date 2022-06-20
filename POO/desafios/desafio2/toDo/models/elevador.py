class Elevador:

    def __init__(self, id: int) -> None:
        self.__id = id
        self.__andar = 1

    def get_id(self) -> int:
        return self.__id
    
    def set_id(self, id) -> None:
        self.__id = id

    def get_andar(self) -> int:
        return self.__andar
    
    def set_andar(self, andar) -> None:
        self.__andar = andar