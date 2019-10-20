class MagicState:

    def __init__(self, mp : int, mp_limit : int):
        self.mp = mp
        self.mp_limit = mp_limit

    def spend_mana(self, mp):
        self.mp -= mp
        if self.mp < 0:
            self.mp = 0
