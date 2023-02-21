class IntFloatValueError(Exception):
    def __init__(self,value):
        self.value = value
        
    def __str__(self):
        return f'wartość: {self.value} jest błędna. Słownik akceptuje jedynie wartości: int,float'
    
    
class KeyValueConstructError(Exception):
    def __init__(self,key,value):
        self.key=key
        self.value = value
        
    def __str__(self):
        return f'klucze i wartości powinny być opisane za pomocą krotek lub list,' \
               f'klucze {self.key} są typu {type(self.key)},' \
               f'wartości {self.value} są typu {type(self.value)}\n'
