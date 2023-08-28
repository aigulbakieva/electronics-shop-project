from src.item import Item

item_1= ("Смартфон", 1000, 20)
item_2 = ("Ноутбоук", 20000, 5)

def test_calculate_total_price():
    assert calculate_total_price(item_2) == 100000
    assert calculate_total_price(item_1) == 200000


def test_apply_discount(item):
    Item.pay_rate = 0.8
    assert apply_discount(item_2) == 10000
