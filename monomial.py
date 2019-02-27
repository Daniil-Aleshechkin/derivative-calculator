class Monomial():
    def __init__(self,coefficent,degree):
        self.coefficent = coefficent
        self.variable = "x"
        self.degree = degree
    
    def toStr(self, addSign):
        string = ""

        if self.coefficent==0:
            return string
        elif self.degree == 0:
            string = str(self.coefficent)
        elif self.degree == 1:
            string = str(self.coefficent)+self.variable
        else:
            string = str(self.coefficent)+self.variable+"^"+str(self.degree)
        
        if addSign == True:
            if self.coefficent>0:
                string = "+"+string
            else:
                string = "-"+string
        else:
            if self.coefficent<0:
                string = "-"+string

        return string
    
    def powerRule(self):
        derivative = Monomial(self.coefficent*self.degree,self.degree-1)
        
        return derivative