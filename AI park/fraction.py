#27
class Fraction():
    def __init__(self, m, n):
        self.numerator = m #분자
        self.denominator = n #분모
    
    def reduce(self):
        gcd = self.GCD(m,n) 
        self.numerator /= gcd    
        self.denominator /= gcd
        
    
    def GCD(self,m,n):
        while n !=0:
            t = n
            n = m % n
            m = t
        return m
        
    