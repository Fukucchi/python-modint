MOD = 10**9 + 7
class ModInt:

    def __init__(self, x):
        self.x = x.x if isinstance(x, ModInt) else x % MOD

    __str__ = lambda self:str(self.x)
    __repr__ = __str__
    __int__ = lambda self: self.x
    __index__ = __int__

    __add__ = lambda self, other: ModInt(self.x + ModInt(other).x)
    __sub__ = lambda self, other: ModInt(self.x - ModInt(other).x)
    __mul__ = lambda self, other: ModInt(self.x * ModInt(other).x)
    __pow__ = lambda self, other: ModInt(pow(self.x, ModInt(other).x, MOD))
    __truediv__ = lambda self, other: ModInt(self.x * pow(ModInt(other).x, MOD - 2, MOD))
    __floordiv__ = lambda self, other: ModInt(self.x // ModInt(other).x)
    __radd__ = lambda self, other: ModInt(other + self.x)
    __rsub__ = lambda self, other: ModInt(other - self.x)
    __rpow__ = lambda self, other: ModInt(pow(other, self.x, MOD))
    __rmul__ = lambda self, other: ModInt(other * self.x)
    __rtruediv__ = lambda self, other: ModInt(other * pow(self.x, MOD - 2, MOD))
    __rfloordiv__ = lambda self, other: ModInt(other // self.x)

    __lt__ = lambda self, other: self.x < ModInt(other).x
    __gt__ = lambda self, other: self.x > ModInt(other).x
    __le__ = lambda self, other: self.x <= ModInt(other).x
    __ge__ = lambda self, other: self.x >= ModInt(other).x
    __eq__ = lambda self, other: self.x == ModInt(other).x
    __ne__ = lambda self, other: self.x != ModInt(other).x

def cmb(n,r):  #nCr = n!/(n-r)!r!
    retVal = 1
    for i in range(n-r+1,n+1):
        retVal *= i
    for i in range(2,r+1):
        retVal //= i
    return retVal
