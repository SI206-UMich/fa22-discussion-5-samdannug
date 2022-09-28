import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	if type(sentence) == str:
		for i in sentence:
			if i.lower() == 'a':
				total += 1
	else:
		return "input must be string"
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		max_stock = self.items[0]
		last_stock = self.items[0].stock
		for item in self.items:
			if item.stock > last_stock:
				max_stock = item
				last_stock = item.stock
		return max_stock
	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		x = self.items[0]
		for y in self.items:
			if y.price > x.price:
				x = y
		return x



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		# Check to see if count_a properly counts the letter "a"
		self.assertEqual(count_a("anaconda"), 3, "Tested count_a on input anaconda")
		# Making sure it counts "a" if it is uppercase or lowercase
		self.assertEqual(count_a("Anaconda"), 3, "Tested count_a on input Anaconda")
		# If anything other then a string is passed return "input must be a string"
		self.assertEqual(count_a([]), "input must be string", "Tested count_a on input []")


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		# Try to add item
		self.w1 = Warehouse()
		self.w1.add_item(self.item1)

		# Check that it is added to the warehouse
		# self.assertEqual(self.w1.items[0].name, "Beer", "Test of add_items")
		self.assertEqual(self.w1.items[0].__str__(), "Item = Beer, Price = 6, Stock = 20", "Test of add_items")



	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		# set up warehouse
		self.w1 = Warehouse([self.item1, self.item2, self.item3])

		# check if the item returned has the most stock
		self.assertEqual(self.w1.get_max_stock().stock, 100, "test get_max_stock")


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		self.w1 = Warehouse([self.item1, self.item2, self.item3])
		self.assertEqual(self.w1.get_max_price(), self.item1)
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()