from models.restaurantes import Restaurantes

restaurante_praca = Restaurantes('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 5)




def main():
    Restaurantes.listar_restaurantes()

if __name__ == '__main__':
    main()