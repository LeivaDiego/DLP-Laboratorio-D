class Simbolo():
    def __init__(self, symbol):
        self.label = symbol
        self.isOperator = False
        self.isSpecialChar = False
        self.token = None
        self.isFinalSymbol = False
    
    def setType(self, isOperator):
        self.isOperator = isOperator
        
    def setSpecialType(self, isSpecial):
        self.isSpecialChar = isSpecial

    def setToken(self, newToken):
        self.token = newToken
        
    def setFinalSymbol(self, isFinal):
        self.isFinalSymbol = isFinal
    
    def __str__(self):
        if(self.isSpecialChar):
            return repr(self.label).replace("'", "")
        
        return self.label
    
    def __repr__(self):
        return str(self)