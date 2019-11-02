from abc import ABC


class Observable(ABC):

    def notify(self, observers):
        for obs in observers:
            obs.update()