class calculator:
    def _check_type(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Os argumentos devem ser números")
        
    def divisao(self, a, b):
        self._check_type(a, b)
        if b == 0:
            raise ZeroDivisionError()
        return a / b
    
#TODO: Criar os metodos para adição, subtração e multiplicação passando antes pelo check_type para garantir que e um tipo numerico
