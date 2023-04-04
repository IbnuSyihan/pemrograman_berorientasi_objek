class celcius:
    def __init__(self, C):
        self.celcius=C
    def to_fahrenheit(self):
        F=(9/5)*self.celcius+32
        return F
    def to_reamur(self):
        R=(4/5)*self.celcius
        return R
    def to_kelvin(self):
        K=self.celcius+273
        return K
C1=75
Ca=celcius(C1)
print("konversi ", C1, " derajat celcius adalah ", Ca.to_fahrenheit(), " derajat fahrenheit.")
C2=60
Cb=celcius(C2)
print("konversi ",C2, " derajat celcius adalah", Cb.to_reamur(), " derajat reamur")
C3=90
Cc=celcius(C3)
print("konversi ", C3, " derajat celcius adalah ", Cc.to_kelvin(), " derajat kelvin")