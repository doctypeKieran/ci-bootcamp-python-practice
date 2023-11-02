""" 1. *args and **kwargs: Sharing Toys """

# Imagine you have a magic toy box.

# When you use *args, it’s like saying, “I want to play with any number of toys, and I don’t want to tell you all their names right now.” So, you can take out one, two, three, or even more toys, and start playing!
def play_with_toys(*toys):
    for toy in toys:
        print(f"Playing with a {toy}")

play_with_toys("Teddy Bear", "Train", "Painting Set")
# This means you're playing with the Teddy Bear, Train and Painting Set

print("\n")

""" When you use **kwargs, it’s like saying, “I want to play with some special toys, and I will tell you some cool things about them.”  """

def play_with_special_toys(**toys):
    for toy, detail in toys.items():
        print(f"Playing with a {toy} which is {detail}")
    print("the kwargs toys is type:", type(toys))

play_with_special_toys(Teddy="soft and cuddly", Puzzle="fun and tricky", Yoyo="a pain in the arse")