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

        equal_quantity = product.quantity
        assert product.check_quantity(
            equal_quantity) is True, 'not correct with quantity equal product.quantity'

        less_quantity = product.quantity - 1
        assert product.check_quantity(
            less_quantity) is True, 'not correct with quantity less than product.quantity'

        more_quantity = product.quantity + 1
        assert product.check_quantity(
            more_quantity) is False, 'not correct with quantity more than product.quantity'

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        equal_quantity = product.quantity
        product.buy(equal_quantity)
        assert product.quantity == 0, 'failed with equal quantity'

        less_quantity = product.quantity - 1
        product.buy(less_quantity)
        assert product.quantity == 1, 'failed with less quantity'

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        more_quantity = product.quantity + 1
        with pytest.raises(ValueError):
            assert product.buy(
                more_quantity) is ValueError, 'failed whith quantity more then stock'


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, pencil, cart):
        cart.add_product(pencil, quantity=5)
        assert cart.products[pencil] == 5, 'failed with adding to empty cart'

        cart.add_product(pencil, quantity=100)
        assert cart.products[pencil] == 105, 'failed with adding to product in cart'

    def test_remove_product(self, product: Product, cart, quantity=None):
        cart.clear()
        cart.add_product(product, 5)
        cart.remove_product(product)
        assert product not in cart.products, 'not correct with quantity not received'

        cart.clear()
        cart.add_product(product, 1)
        cart.remove_product(product, 5000)
        assert product not in cart.products, 'not correct with quantity more than stock'

    def test_clear(self, product, copybook, pencil, cart):
        cart.add_product(copybook, 150)
        cart.add_product(pencil, 300)
        cart.clear()

        assert cart.products == {}, 'cart not empty'

    def test_get_total_price(self, product, copybook, pencil, cart):
        cart.clear()
        cart.add_product(product, 1)
        cart.add_product(copybook, 2)
        cart.add_product(pencil, 4)

        assert cart.get_total_price() == 300, 'Total price not correct'

    def test_buy(self, product, copybook, pencil, cart):
        cart.clear()
        cart.add_product(product, 1)
        cart.add_product(copybook, 2)
        cart.add_product(pencil, 4)
        cart.buy()

        assert cart.get_total_price() == float(300), 'buy() method give out not correct total_price'
        assert pencil.quantity == 996, 'product quantity not correct after buying cart'
        assert copybook.quantity == 2998, 'product quantity not correct after buying cart'

    def test_buy_more_than_stock(self, product, cart):
        cart.add_product(product, product.quantity + 1)
        with pytest.raises(ValueError):
            assert cart.buy() is ValueError, 'failed with quantity more then stock'
