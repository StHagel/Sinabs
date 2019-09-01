def main():
    print("Welcome to Sinabs!")

    # Read the number of people splitting the bill.
    n_people = 0
    while True:
        raw_string = input("How many people want to split the bill?\n")
        try:
            n_people = int(raw_string)
            break
        except ValueError:
            print("ValueError: " + raw_string + " is not a number.")
            print("Please enter a valid number.")

    start_accounts = get_start_accounts(n_people)

    print("The initial balance after all spendings are:")
    for name in start_accounts.keys():
        print(name + ": " + str(start_accounts[name]))




def get_start_accounts(n):
    start_accounts = {}
    for i in range(n):
        new_name = input("Please enter the name of person " + str(i + 1) + ".\n")
        start_accounts[new_name] = 0.0
        new_spending = 0.0

        raw_string = input("Please enter " + new_name + "'s first spending (0 to quit).\n")
        try:
            new_spending = float(raw_string)
            start_accounts[new_name] += new_spending
        except ValueError:
            print("ValueError: " + raw_string + " is not a number.")
            print("Please enter a valid number.")

        while abs(new_spending) >= 0.01:
            raw_string = input("Please enter " + new_name + "'s next spending.\n")
            try:
                new_spending = float(raw_string)
                start_accounts[new_name] += new_spending
            except ValueError:
                print("ValueError: " + raw_string + " is not a number.")
                print("Please enter a valid number.")

    return start_accounts


if __name__ == '__main__':
    main()
