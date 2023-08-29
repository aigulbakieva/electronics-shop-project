from src.item import Item

item1 = Item("Смартфон", 1000, 20)
item2 = Item("Ноутбоук", 20000, 5)


def test_init():
    assert item1.price == 1000
    assert item2.price == 20000
def test_calculate_total_price():
    assert item2.calculate_total_price() == 100000
    assert item1.calculate_total_price() == 20000


