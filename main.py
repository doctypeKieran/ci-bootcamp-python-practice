""" Sharing Ingredients and Special Orders: *args and **kwargs """

# In our busy cafe, customers might shout out what they want or give us special instructions.

# Using *args: Customers shout out ingredients, and we can use as many as we like to make a dish!
def make_salad(*ingredients):
  print("Making a salad with,", ", ".join(ingredients))

make_salad("lettuce", "tomato", "cucumber", "peppers", "chicken")

print("\n")

# Using **kwargs: Customers give special instructions, and we follow them closely to make their dish perfect!
def make_sandwich(**instructions):
  print("Making a sandwich with:")
  for ingredient, amount in instructions.items():
    print(f"{amount} of {ingredient}")
    
make_sandwich(tomato="a lot", lettuce="a little", cheese="tons")

print("\n")

""" Safety Checks in the Kitchen: Decorators """

# We have safety checks in place to ensure everything is done properly in the cafe.

# CleanHandsCheck: Before cooking, this check ensures our hands are washed.
def CleanHandsCheck(cooking_func):
    print("Checking if hands are washed...")
    hands_are_washed = True
    if hands_are_washed:
        print("Hands are clean! Safe to cook.")
        cooking_func()
    else:
        print("Oops! Hands are not clean. Please wash them first.")

def make_pizza():
    print("Making a yummy pizza!")

CleanHandsCheck(make_pizza)

print("\n")

""" Special Cooking Sets: Mixins """

# In our cafe, we have special sets to make our cooking even more fun.

# SmoothieSet: This set lets us make all kinds of smoothies.
class SmoothieSet:
    ingredients = ["fruits", "yoghurt", "ice"]
    appliance = "blender"

class MakeADrink(SmoothieSet):
    drink_type = "juice"
    
    def create(self):
        print(f"Making a {self.drink_type} drink using a {self.appliance} with {", ".join(self.ingredients)}")

my_drink = MakeADrink()
my_drink.create()

print("\n")

print("Here we go...")
print("\n")

""" The Ultimate Cafe Experience: Combine Everything """

# Finally, let's combine all our tools for the best cafe experience 
@CleanHandsCheck
def make_special_smoothie():
    smoothie = MakeADrink()
    smoothie.drink_type = "smoothie"
    smoothie.create()

make_special_smoothie()