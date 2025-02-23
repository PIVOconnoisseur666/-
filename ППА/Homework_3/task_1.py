class BaseTeaException(Exception):
    pass

class Sugar:
    def __init__(self, kind):
        self._validate_kind(kind)
        self.kind = kind

    @staticmethod
    def _validate_kind(kind):
        if kind not in ("brown", "white"):
            raise ValueError("Invalid sugar type")

class Tea:
    def __init__(self, kind):
        self._validate_kind(kind)
        self.kind = kind

    @staticmethod
    def _validate_kind(kind):
        if kind not in ("black", "green"):
            raise ValueError("Invalid tea type")

class TeaCup:
    def __init__(self):
        self.sweetness = 0
        self.fullness = 0
        self.tea = None

    def pour_water(self, amount=None):
        if amount is None:
            amount = 1

        if not isinstance(amount, (float, type(None))):
            raise TypeError("Amount must be a float or NoneType")
        if not (0 <= amount <= 1):
            raise ValueError("Amount must be in range [0, 1]")
        if self.fullness + amount > 1:
            raise BaseTeaException("Attempt to pour too much water")

        self.fullness += amount

    def drink(self, amount=None):
        if amount is None:
            amount = self.fullness

        if not isinstance(amount, (float, type(None))):
            raise TypeError("Amount must be a float or NoneType")
        if not (0 <= amount <= 1):
            raise ValueError("Amount must be in range [0, 1]")
        if self.fullness - amount < 0:
            raise BaseTeaException("Attempt to drink beyond available amount")

        self.fullness -= amount
        if self.fullness == 0:
            self.sweetness = 0
            self.tea = None

    def is_full(self):
        return self.fullness == 1

    def __add__(self, other):
        if isinstance(other, Sugar):
            self.sweetness += 1
        elif isinstance(other, Tea):
            self.tea = other.kind
        else:
            raise TypeError("Can only add Sugar or Tea to a TeaCup")
        return self

    def __sub__(self, other):
        if isinstance(other, Sugar):
            if self.sweetness - 1 < 0:
                raise ValueError("Amount of sugar can't be negative")
            self.sweetness -= 1
        else:
            raise TypeError("Can only subtract Sugar from TeaCup")
        return self
