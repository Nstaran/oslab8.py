class complex:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def show(self):
        if self.y>0:
            print(self.x, '+', self.y, 'i')
        else:
            print(self.x, self.y, 'i')

    def sum(self,other):
        res=complex()
        res.x=self.x + other.x
        res.y=self.y + other.y
        return res

    def sub(self,other):
        res = complex()
        res.x = self.x - other.x
        res.y = self.y - other.y
        return res

    def mul(self,other):
        res = complex()
        res.x = ((self.x * other.x)-(self.y * other.y))
        res.y = ((self.x * other.y)+(self.y + other.x))
        return res



while True:
    print('enter number1 :')
    x1 = int(input())
    y1 = int(input())
    n1 = complex(x1 ,y1)
    n1.show()
    print('enter number2 :')
    x2 = int(input())
    y2 = int(input())
    n2 = complex(x2, y2)
    n2.show()
    while True:
        print('choose:\n1.add\n2.sub\n3.mul\n4.exit\n')
        c = int(input())
        if c==1:
            N=n1.sum(n2)
            N.show()
        if c==2:
            N=n1.sub(n2)
            N.show()
        if c==3:
            N=n1.mul(n2)
            N.show()
        if c==4:
            break
    e = input('Do you want to continue with other complex numbers? [yes or no]')
    if e == 'no':
        break 