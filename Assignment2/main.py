import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    is_on = True
    while is_on:
        choice = input("What size sandwich would you like?  (small/medium/large)")

        if choice == "off":
            is_on = False
            print("Turning off sandwich machine")
        elif choice == "report":
            for item, amount in resources.items():
                print(f"{item.capitalize()}: {amount}")
        elif choice in recipes:
            selected_recipe = recipes[choice]
            ingredients = selected_recipe["ingredients"]
            cost = selected_recipe["cost"]

            if sandwich_maker_instance.check_resources(ingredients):
                inserted_money = cashier_instance.process_coins()
                if cashier_instance.transaction_result(inserted_money, cost):
                    sandwich_maker_instance.make_sandwich(choice, ingredients)
        else :
            print("Sorry, that is an invalid selection.")
            print("Please choose small, medium, large, report, or off.")



if __name__=="__main__":
    main()
