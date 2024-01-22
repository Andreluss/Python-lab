import random
from math import gcd
from sys import argv


class Ułamek:
    # Wersja2 __slots__ = ('licz', 'mian')

    def __init__(self, licz: int, mian: int):
        assert mian != 0, "Mianownik nie może być 0."
        self.licz = licz
        self.mian = mian
        self._red()

    def _red(self):
        if self.mian < 0:
            self.licz *= -1
            self.mian *= -1
        d = gcd(self.licz, self.mian)
        self.licz //= d
        self.mian //= d

    def __str__(self):
        return f"{self.licz}/{self.mian}"

    def __repr__(self):
        return f"Ułamek({self.licz}, {self.mian})"

    def __add__(self, other):
        licz = self.licz * other.mian + self.mian * other.licz
        mian = self.mian * other.mian
        return Ułamek(licz, mian)

    def __sub__(self, other):
        licz = self.licz * other.mian - self.mian * other.licz
        mian = self.mian * other.mian
        return Ułamek(licz, mian)

    def __mul__(self, other):
        licz = self.licz * other.licz
        mian = self.mian * other.mian
        return Ułamek(licz, mian)

    def __truediv__(self, other):
        licz = self.licz * other.mian
        mian = self.mian * other.licz
        return Ułamek(licz, mian)

    def __eq__(self, other):
        return self.licz == other.licz and self.mian == other.mian

    def __lt__(self, other):
        return self.licz / self.mian < other.licz / other.mian

    def __le__(self, other):
        return self.licz / self.mian <= other.licz / other.mian


if __name__ == '__main__':
    n, k = int(argv[1]), int(argv[2])
    print(n, k)

    ulamki = [Ułamek(random.randint(1, 100), random.randint(1, 100)) for i in range(n)]
    for i in range(k):
        ulamki[i % n] += ulamki[(i+1) % n]

    print("Koniec")