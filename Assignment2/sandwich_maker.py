
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, amount_required in ingredients.items():
            if self.machine_resources.get(item,0) < amount_required:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item, amount_used in order_ingredients.items():
            self.machine_resources[item] -= amount_used
        print(f"Here is your {sandwich_size} sandwich.")
