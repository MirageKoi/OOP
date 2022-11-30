class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def total_cost(self, quant: int) -> float:
        return round(self.price * quant, 2)

    def __repr__(self) -> str:
        return f'{self.name}: {self.price}'

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

    def __float__(self) -> float:
        return float(self.price)

    def __str__(self) -> str:
        return str(self.name)


class ShoppingCart:
    def __init__(self, *goods: list):
        self.goods = list(goods)

    def add_goods(self, prod: Product, quant: int = 1):
        for count, (x, y) in enumerate(self.goods):
            if x == prod:
                self.goods[count][1] += quant
                return
        self.goods.append([prod, quant])

    def pay(self) -> float:
        temp = 0
        for x, y in self.goods:
            temp += x.total_cost(y)
        return round(temp, 2)

    def __repr__(self) -> str:
        return f'{self.goods}'

    def __float__(self):
        return self.pay()


apple = Product('apple', 1.8)
cheese = Product('cheese', 5.55555555)
milk = Product('milk', 3.5)
bread = Product('bread', 3.2)
chiken = Product('chiken', 6.2)
pc = Product('apple', 20000)
apple2 = Product('apple', 1.8)


c1 = ShoppingCart()
c1.add_goods(apple, 5)
c1.add_goods(cheese, 3)
c1.add_goods(milk, 2)
c1.add_goods(milk, 3)
c2 = ShoppingCart([bread, 3], [pc, 1], [chiken, 9])
c2.add_goods(pc, 1)
c2.add_goods(pc, 1)
c2.add_goods(pc, 1)
# c1.add_goods(c2)
print(c1.pay())
# print(c2.pay())



print(c1)
print(c2)
# print(apple==pc)
# print(apple==apple2)
print(float(c1))
print(float(c2))
