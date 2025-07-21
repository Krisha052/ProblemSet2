"""Program planning
- only accepting 25, 10 & 5 cents
- counting the total until count reaches 50 or is above 50
- returning any change
"""

def main():
    price = 50
    paid = 0

    while paid < price:
        print(f"Amount Due: {price - paid}")
        coin = int(input("Insert Coin: "))
        if coin in [25, 10, 5]:
            paid += coin

    change = paid - price
    print(f"Change Owed: {change}")



if __name__ == "__main__":
    main()
