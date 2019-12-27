from models.alert import Alert
from models.item import Item

URL = "https://www.johnlewis.com/2018-apple-ipad-pro-12-9-inch-a12x-bionic-ios-wi-fi-celluular-512gb/space-grey/p3834614"
TAG_NAME = 'p'
QUERY = {"class":"price price--large"}

# ipad = Item(URL,TAG_NAME,QUERY)
# # ipad.save_to_mongo()
#
# items_loaded = Item.all()
# print(items_loaded)
# print(items_loaded[0].load_price())

alert = Alert('d6e81d65e3d445efb9a8152664944b85',1500)
alert.save_to_mongo()
