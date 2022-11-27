class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def total_cost(self, quant: int) -> float:
        return round(self.price * quant, 2)


class ShoppingCart:
    def __init__(self):
        self.goods = []

    def add_goods(self, prod: Product, quant: int):
        self.goods.append((prod, quant))

    def pay(self) -> float:
        item, count = zip(*self.goods)
        return round(sum((x.total_cost(y) for x, y in zip(item, count))), 2)


apple = Product('apple', 1.8)
cheese = Product('cheese', 5.55555555)
milk = Product('milk', 3.5)
bread = Product('bread', 3.2)
chiken = Product('chiken', 6.2)


c1 = ShoppingCart()
c1.add_goods(apple, 5)
c1.add_goods(cheese, 3)
c1.add_goods(milk, 2)

print(c1.pay())
