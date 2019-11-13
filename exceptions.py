class AttacksItself(Exception):
    pass


class TargetIsDead(Exception):
    pass


class OutOfMana(Exception):
    pass


class CantDoCauseDead(Exception):

    def __init__(self, ent):
        print("Entity " + ent.name + " can't perform actions")


class CantTurn(Exception):

    def __init__(self, name, target):
        print("Entity " + target.name + " cant be turned into " + name)
