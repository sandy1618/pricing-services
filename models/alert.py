import uuid
from typing import Dict
from models.item import Item
from models.model import Model


class Alert(Model):
    # when ever i create alert object , I also create the item object associated with the id
    collection = 'alerts'
    def __init__(self, item_id: str, price_limit: float, _id: str = None):
        super().__init__()
        self.item_id = item_id
        self.item = Item.get_by_id(item_id)
        self.price_limit = price_limit
        self.collection = 'alerts'
        self._id = _id or uuid.uuid4().hex

    def json(self) -> Dict:
        return {
            '_id': self._id,
            'price_limit': self.price_limit,
            'item_id': self.item_id
        }


    def load_item_price(self) -> float:
        self.item.load_price()
        return self.item.price  # price gets updated to item objec only when we do load_price

    def notify_if_price_reached(self):
        if self.item.price < self.price_limit:
            print("Item {} has reached a price under {} . Latest price : {}".format(self.item, self.price_limit,
                                                                                    self.item.price))


