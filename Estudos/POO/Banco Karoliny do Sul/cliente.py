class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome.title()

#property serve para demarcar uma propriedade, e também quando formos chamar o nosso
#metodo, podemos chamar sem parênteses e outro ponto importante é que ele tem o mesmo
#comportamento que um get, conforme acima e fica mais limpo no codigo, não preciso colocar 
#o get na frente de cada metodo, pois o property tem a mesma função.

    @property
    def nome(self):
        return self.__nome.tittle()
    
