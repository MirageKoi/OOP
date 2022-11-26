class Product:
    def __init__(self, name: str, price:float):
        self.name = name
        self.price = price
    #
    def total_cost(self, quant:int) -> float:
        return self.price * quant


class ShoppingCart:
    def __init__(self,*goods):
        self.goods = goods

    def pay(self) -> float:
        return f'Total cost is {sum(self.goods):.2f} leafs.'


apple = Product('apple', 1.8)
cheese = Product('cheese', 5.55555555)
milk = Product('milk', 3.5)
bread = Product('bread', 3.2)
chiken = Product('chiken', 6.2)

c1 = ShoppingCart(apple.total_cost(3), cheese.total_cost(2))
c2 = ShoppingCart(milk.total_cost(2), bread.total_cost(3), chiken.total_cost(2), apple.total_cost(5))

print(c1.pay())
print(c2.pay())