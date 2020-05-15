from enum import Enum


class Enum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
