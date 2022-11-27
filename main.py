class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def total_cost(self, quant: int) -> float:
        return round(self.price * quant, 2)


class ShoppingCart:
    def __init__(self, *goods):
        self.goods = goods

    def pay(self) -> str:
        check = 0
        f_goods = []
        for unit in self.goods:
            check += unit[0].total_cost(unit[1])
            f_goods.append((unit[0].name, unit[1]))

        return f'Total cost is {round(check, 2)} leafs. Now you have {f_goods}'


apple = Product('apple', 1.8)
cheese = Product('cheese', 5.55555555)
milk = Product('milk', 3.5)
bread = Product('bread', 3.2)
chiken = Product('chiken', 6.2)


c1 = ShoppingCart((apple, 5), (cheese, 3), (milk, 2))

print(c1.pay())

