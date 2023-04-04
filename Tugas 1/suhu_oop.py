class Fahrenheit:
    def __init__(self, F):
        self.fahrenheit=F
    def to_celcius(self):
        C=(self.fahrenheit-32)*(5/9)
        return C
    def to_reamur(self):
        R=(self.fahrenheit-32)*(4/9)
        return R
    def to_kelvin(self):
        K=(5/9)*(self.fahrenheit-32)+273
        return K

print("-"*100)
F=int(input("Masukkan Fahrenheit: "))
FahrenheitA=Fahrenheit(F)
print("")
print("konversi ", F, " derajat fahrenheit adalah ", FahrenheitA.to_celcius(), " derajat celcius.")
print("konversi ",F, " derajat fahrenheit adalah", FahrenheitA.to_reamur(), " derajat reamur.")
print("konversi ", F, " derajat fahrenheit adalah ", FahrenheitA.to_kelvin(), " derajat kelvin.")
print("-"*100)

class Reamur:
    def __init__(self, R):
        self.reamur=R
    def to_celcius(self):
        C=self.reamur*5/4
        return C
    def to_fahrenheit(self):
        F=(self.reamur*9/4)+32
        return F
    def to_kelvin(self):
        K=(self.reamur*5/4)+273
        return K
    
R=int(input("Masukkan Reamur: "))
ReamurA=Reamur(R)
print("")
print("konversi ", R, " derajat reamur adalah ", ReamurA.to_celcius(), " derajat celcius.")
print("konversi ",R, " derajat reamur adalah", ReamurA.to_fahrenheit(), " derajat fahrenheit.")
print("konversi ", R, " derajat reamur adalah ", ReamurA.to_kelvin(), " derajat kelvin.")
print("-"*100)

class Kelvin:
    def __init__(self, K):
        self.kelvin=K
    def to_celcius(self):
        C=self.kelvin-273
        return C
    def to_fahrenheit(self):
        F=9/5*(self.kelvin-273)+32
        return F
    def to_reamur(self):
        R=(self.kelvin-273)*4/5
        return R
    
K=int(input("Masukkan Kelvin: "))
KelvinA=Kelvin(K)
print("")
print("konversi ", K, " derajat kelvin adalah ", KelvinA.to_celcius(), " derajat celcius.")
print("konversi ",K, " derajat kelvin adalah", KelvinA.to_fahrenheit(), " derajat fahrenheit.")
print("konversi ", K, " derajat kelvin adalah ", KelvinA.to_reamur(), " derajat kelvin.")
print("-"*100)