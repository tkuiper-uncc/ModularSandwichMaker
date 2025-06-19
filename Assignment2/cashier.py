class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        total = 0
        total += self._get_coin_input("How many quarters?: ", 0.25)
        total += self._get_coin_input("How many dimes?: ", 0.10)
        total += self._get_coin_input("How many nickels?: ", 0.05)
        total += self._get_coin_input("How many pennies?: ", 0.01)
        return total

    def _get_coin_input(self, prompt, value):
        while True:
            try:
                entry = input(prompt)
                if entry == '':
                    return 0
                return int(entry) * value
            except ValueError:
                print("Please insert a valid whole number or press enter for 0.")



    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, that is not enough money.")
            return False

