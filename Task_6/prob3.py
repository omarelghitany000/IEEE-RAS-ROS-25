class Num:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b != 0:
          return a / b
        if b==0:
          print("Cannot divide by zero")

process= Num()

print("add: 6+3 = ",process.add(6,3))
print("sub: 6-3 = ",process.sub(6,3))
print("mul: 6*3 = ",process.mul(6,3))
print("div: 6/4 = ",process.div(6,3))
