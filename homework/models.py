class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity


    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        return self.quantity >= quantity


    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity) is True:
            self.quantity -= quantity
        else:
            raise ValueError

        return self.quantity



    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, quantity=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product not in self.products:
            self.products[product] = quantity
        else:
            self.products[product] += quantity

        return [product.name, self.products[product]]


    def remove_product(self, product: Product, quantity=None):
        """
        Метод удаления продукта из корзины.
        Если quantity не передан, то удаляется вся позиция
        Если quantity больше, чем количество продуктов в позиции, то удаляется вся позиция
        """

        if product in self.products and quantity is None:
            self.products.pop(product)
            text = 'product removed from cart, quantity to buy not received'
        elif product in self.products and quantity > product.quantity:
            self.products.pop(product)
            text = 'product removed from cart, quantity to buy more than stock'
        else:
            text = 'nothing removed from cart'

        return text


    def clear(self):
        self.products.clear()
        return self.products


    def get_total_price(self) -> float:
        return sum(self.products[product] * product.price for product in self.products)


    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """

        for product in self.products:
            if self.products[product] > product.quantity:
                raise ValueError

        total_price = sum(value * key.price for key, value in self.products.items())
        self.products.clear()

        return total_price, self.products.clear()
