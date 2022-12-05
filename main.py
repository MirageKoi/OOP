class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def total_cost(self, quant: int) -> float:
        return round(self.price * quant, 2)

    def __repr__(self) -> str:
        return f'{self.name} cost {self.price}'

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

    def __float__(self) -> float:
        return self.price

    def __str__(self) -> str:
        return self.name


class ShoppingCart:
    def __init__(self) -> None:
        self.goods = []
        self.quant = []

    def add_goods(self, prod: Product, quant: int):
        if prod in self.goods:
            self.quant[self.goods.index(prod)] += quant
            return
        self.goods.append(prod)
        self.quant.append(quant)

    def get_total(self) -> float:
        temp = 0
        for prod, quant in self:
            temp += prod.total_cost(quant)
        return round(temp, 2)

    def __repr__(self) -> str:
        return f'{list(zip(self.goods, self.quant))} '

    def __float__(self):
        return self.get_total()

    def __iter__(self) -> iter:
        return zip(self.goods, self.quant)

    def __add__(self, other):
        new_cart = ShoppingCart()
        new_cart.goods = self.goods.copy()
        new_cart.quant = self.quant.copy()
        if isinstance(other, ShoppingCart):
            for x, y in other:
                new_cart.add_goods(x, y)
        if isinstance(other, Product):
            new_cart.add_goods(other, 1)
        return new_cart


apple = Product('apple', 1.8)
cheese = Product('cheese', 5.55555555)
milk = Product('milk', 3.5)
bread = Product('bread', 3.2)
chiken = Product('chiken', 6.2)
pc = Product('apple', 20000)
apple2 = Product('apple', 1.8)

# testing

c1 = ShoppingCart()
c1.add_goods(apple, 5)
c1.add_goods(cheese, 3)
c1.add_goods(milk, 2)
c1.add_goods(milk, 3)

c1 + milk

c2 = ShoppingCart()
c2.add_goods(pc, 1)
c2.add_goods(pc, 1)
c2.add_goods(pc, 1)
c2.add_goods(milk, 3)

print(c1, 'c1')
print(c2, 'c2')

c3 = c1 + c2
c1.add_goods(milk, 3)
c5 = c1 + milk
c4 = c1 + c3
print(c1, '???')
print(c3, 'c3')
print(c4, 'c4')
print(c5, 'c5')
print(c1.get_total())
print(c2.get_total())
print(c1)

print(c1)
print(c2)
print(apple == pc)
print(apple == apple2)
print(float(c1))
print(float(c2))
