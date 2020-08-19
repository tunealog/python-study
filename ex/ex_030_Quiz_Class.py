# Basic of Python

# Title : Quiz(Class)
# Date : 2020-07-04
# Creator : tunealog

# Quiz) Create the real estate program

# Example (Result):
# Total : 3
# Korea Apartment Buy 10M 2010Y
# Japan Office Rental 1M 2007Y
# America Gym Monthly 100/10 2000Y

class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(
            f"{self.location} {self.house_type} {self.deal_type} {self.price} {self.completion_year}")


re = []

re0 = House("Korea", "Apartment", "Buy", "10M", "2010Y")
re1 = House("Japan", "Office", "Rental", "1M", "2007Y")
re2 = House("America", "Gym", "Monthly", "100/10", "2000Y")

re.append(re0)
re.append(re1)
re.append(re2)

print(f"Total : {len(re)}")
for i in re:
    i.show_detail()
