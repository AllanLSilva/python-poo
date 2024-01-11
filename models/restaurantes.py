class Restaurantes:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurantes.restaurantes.append(self)

    def __str__(self) -> str:
        return f'{self._nome} | {self._categoria}'


    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'.ljust(20)}')
        for restaurante in Restaurantes.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.ativo.ljust(20)}')

    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
    
restaurante_praca = Restaurantes(nome= 'Praça', categoria= 'Gourmet')

restaurante_pizza = Restaurantes(nome= 'Pizza Express', categoria='Italiana')

Restaurantes.listar_restaurantes()