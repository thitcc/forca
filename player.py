class Player:
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.turn = False

    def __str__(self) -> str:
        return super().__str__()