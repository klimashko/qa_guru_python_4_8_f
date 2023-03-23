"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


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

    def test_add_product(self, product):
        cart = Cart()
        assert cart.add_product(product, quantity=5) == ['book', 5]
        assert cart.add_product(product, quantity=100) == ['book', 105]


    def test_remove_product(self, product: Product, quantity=None):
        cart = Cart()

        assert cart.remove_product(product) == 'Nothing removed from cart'  #продукт не добавлен в корзину, нечего удалять

        cart.add_product(product, 5)
        assert cart.remove_product(product) == 'book was removed from cart. Reason: product quantity to buy not received'  #продукт удаляется, тк не указано количество

        cart.add_product(product, 1)
        assert cart.remove_product(product, 2000) == 'book was removed from cart. Reason: product quantity to buy is more than stock'  #продукт удаляется, тк указано количество больше чем на складе
