from math import gcd 

class kasr:
    def __init__(self,n=None, m=None): 
        self.n = n   
        self.m = m


    def simple(self , second):
        simple=gcd(second.n , second.y)
        second.n = second.n // simple  
        second.m = second.m //  simple
        return second


    def sum(self, second):        
        result = kasr()       
        result.n = self.n*second.m + self.m*second.n
        result.m = self.m*second.m
        return self.simple(kasr(result.n,result.m))


    def sub(self, second):
        result = kasr()
        result.n = self.n*second.m - self.m*second.n
        result.m = self.m*second.m
        return self.simple(kasr(result.n,result.m))


    def multiple(self, second):
        result = kasr()    
        result.n = self.n*second.n
        result.m = self.m*second.m
        return self.simple(kasr(result.x,result.m))


    def divide(self, second):
        result = kasr()
        result.n = self.n*second.m
        result.m = self.m*second.n
        return self.simple(kasr(result.n,result.m))



    def show(self):
        return str(self.n) + '/' + str(self.m)

nn= list(map(int, input('enter fraction1: e.g. n/m\n').split('/')))
mm= list(map(int, input('enter fraction2: e.g. n/m\n').split('/')))
a = kasr(nn[0], nn[1])
b = kasr(mm[0], mm[1])
print('sum: %s\tsub: %s\tmul: %s\tdiv: %s'%((a.sum(b)).show(), (a.sub(b)).show(), (a.multiple(b)).show(), (a.divide(b)).show()))