
def buildMenuBook():
    MENU = dict()
    while True:
        dish_name = input("Enter a dish name:")
        if (0 == len(dish_name)):
            break
        prompt = "Enter price of "+dish_name+": "
        price = int(input(prompt))
        MENU[dish_name] = MENU.get(dish_name,0)+price
    return MENU

def main():
    Menu = buildMenuBook()
    print(Menu)
    return None

if __name__ == "__main__":
    main()