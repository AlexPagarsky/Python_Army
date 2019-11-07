class AttacksItself(Exception):
    pass


class CantTurn(Exception):

    def __init__(self, name, target):
        print("Entity " + target.name + " cant be turned into " + name)