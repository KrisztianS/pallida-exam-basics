# We run a Candy shop where we sell candies and lollipops
# One lollipop's price is 10$
# And it made from 5gr of sugar
# One candie's price is 20$
# And it made from 10gr of sugar
# we can raise their prices with a given percentage
#
# Create a CandyShop class
# It can store sugar and money as income. The constructor should take the amount of sugar in gramms.
# we can create lollipops and candies store them in the CandyShop's storage
# If we create a candie or lollipop the CandyShop's sugar amount gets reduced by the amount needed to create the sweets
# We can raise the prices of all candies and lollipops with a given percentage
# We can sell candie or lollipop with a given number as amount
# If we sell sweets the income will be increased by the price of the sweets and we delete it from the inventory
# We can buy sugar with a given number as amount. The price of 1000gr sugar is 100$
# If we buy sugar we can raise the CandyShop's amount of sugar and reduce the income by the price of it.
# The CandyShop should be represented as string in this format:
# "Inventory: 3 candies, 2 lollipops, Income: 100, Sugar: 400gr"
class CandyShop():
    
    def __init__(self, sugar):
        self.sugar_stored = sugar
        self.income = 0
        self.candies = 0
        self.lollipops = 0
        self.price_of_candy = 20
        self.price_of_lollipop = 10
        #self.inventory = "Inventory:" , self.candies , "candies, " , self.lollipops , "lollipops, " , "Income:" , self.income , ", " , "Sugar: " , self.sugar_stored , "gr"

    def create_sweets(self, sweet):
        self.sweet = sweet
        if self.sweet == "candy":
            self.candies += 1
            self.sugar_stored -= 10
        elif self.sweet == "lollipop":
            self.lollipops += 1
            self.sugar_stored -= 5

    def raise_prices(self, percentage):
        self.percentage = percentage
        self.price_of_candy *= percentage * 0.01
        self.price_of_lollipop *= percentage * 0.01

    def sell(self, sweet, amount):
        self.sweet = sweet
        self.amount = amount
        if sweet == "lollipop":
            self.lollipops -= amount
            self.income += amount * self.price_of_lollipop
        elif sweet == "candy":
            self.candies -= 1
            self.income += amount * self.price_of_candy

    def buy_sugar(self, sugar_amount):
        self.sugar_amount = sugar_amount
        self.sugar_stored += sugar_amount
        self.income -= sugar_amount * 0.1

candy_shop = CandyShop(300)

candy_shop.create_sweets("candy")
candy_shop.create_sweets("candy")
candy_shop.create_sweets("lollipop")
candy_shop.create_sweets("lollipop")

candy_shop.sell("candy", 1)


candy_shop.raise_prices(5)
candy_shop.sell("lollipop", 1)


candy_shop.buy_sugar(400)

