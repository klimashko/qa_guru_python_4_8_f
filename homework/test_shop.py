"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def copybook():
    return Product("copybook", 50, "This is a copybook", 3000)

@pytest.fixture
def pencil():
    return Product("pencil", 25, "This is a pencil", 1000)

@pytest.fixture
def cart():
    cart = Cart()
    return cart


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity

        less_quantity = product.quantity - 1
        equal_quantity = product.quantity
        more_quantity = product.quantity + 1

        assert product.check_quantity(less_quantity) is True, 'check_quantity() working not correct with less_quantity'
        assert product.check_quantity(equal_quantity) is True, 'check_quantity() working not correct with equal_quantity'
        assert product.check_quantity(more_quantity) is False, 'check_quantity() working not correct with more_quantity'

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        less_quantity = product.quantity - 1
        equal_quantity = product.quantity
        assert product.buy(less_quantity) == 1
        assert product.buy(equal_quantity) == 0

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        more_quantity = product.quantity + 1
        with pytest.raises(ValueError):
            assert product.buy(more_quantity) is ValueError


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product, cart):
        # cart = Cart()
        assert cart.add_product(product, quantity=5) == ['book', 5]
        assert cart.add_product(product, quantity=100) == ['book', 105]


    def test_remove_product(self, product: Product, cart, quantity=None):
        # cart = Cart()

        assert cart.remove_product(product) == 'nothing removed from cart'

        cart.add_product(product, 5)
        assert cart.remove_product(product) == 'product removed from cart, quantity to buy not received'

        cart.add_product(product, 1)
        assert cart.remove_product(product, 5000) == 'product removed from cart, quantity to buy more than stock'


    def test_clear(self, product, copybook, pencil, cart):
        # cart = Cart()
        cart.add_product(copybook, 150)
        cart.add_product(pencil, 300)
        cart.clear()

        assert cart.products == {}


    def test_get_total_price(self, product, copybook, pencil, cart):
        # cart = Cart()
        cart.add_product(product, 1)
        cart.add_product(copybook, 2)
        cart.add_product(pencil, 4)
        print(cart.products)
        print(cart.get_total_price())
        assert cart.get_total_price() == 300, 'Total price not correct'


    def test_buy(self, product, copybook, pencil, cart):
        cart.add_product(product, 1)
        cart.add_product(copybook, 2)
        cart.add_product(pencil, 4)

        assert cart.buy() == (300, None), 'buy() method did not work correctly'