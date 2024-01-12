from models.layout.item_cardapio import ItemCardapio
class Promocao(ItemCardapio):
    def __init__(self, nome, preco, desconto):
        super().__init__(nome, preco)
        self._desconto = desconto