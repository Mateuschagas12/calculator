class calculator:
    def _check_type(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Os argumentos devem ser números")
        
    def divisao(self, a, b):
        self._check_type(a, b)
        if b == 0:
            raise ZeroDivisionError()
        return a / b
    def add(self,a,b):
        self._check_type(a,b)
        return a + b
    
    def subtracao(self,a,b):
        self._check_type(a,b)
        return a - b
