import monomial

class Polynomial():
    
    def __init__(self,equation):
        terms = Polynomial.splitTerms(equation)
        termObjects = []

        print(terms)

        for term in terms:
            pos = 0
            for c in term:
                if len(term)==pos+1 and c=="x":
                    termObjects.append(monomial.Monomial(int(term[:pos]),1))
                    break
                elif c=="x":
                    termObjects.append(monomial.Monomial(int(term[:pos]),int(term[pos+2:])))
                    break
                pos += 1
            else:
                if term!="":
                    termObjects.append(monomial.Monomial(int(term),0))

        
        self.terms = termObjects
    
    def splitTerms(equation):
        terms = []

        pos = 0
        previousPos = 0
        for c in equation:
            if c == "-" and pos != 0:
                terms.append(equation[previousPos:pos])
                previousPos = pos
            elif c == "+":
                terms.append(equation[previousPos:pos])
                previousPos = pos+1
            pos += 1
        
        terms.append(equation[previousPos:])

        return terms
   
    def toStr(self):
        equation = ""
        
        sign = False
        for term in self.terms:
            equation += term.toStr(sign)
            if sign == False:
                sign = True
        
        if len(equation) != 0:
            return equation[:len(equation)]
        else:
            return equation
    


    def derive(self):
        equation = ""
        
        sign = False
        for term in self.terms:
            equation += term.powerRule().toStr(sign)
            if sign == False:
                sign = True
        
        print(equation)
        derivativeObject = Polynomial(equation)
        return derivativeObject
