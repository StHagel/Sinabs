"""
 Copyright © 2019, 2020 Stephan Hagel (stephan.hagel@physik.uni-giessen.de)

 This file is part of the Sinabs project.

 This project is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This project is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


def main():
    print("Welcome to Sinabs!")

    # Read the number of people splitting the bill.
    while True:
        raw_string = input("How many people want to split the bill?\n")
        try:
            n_people = int(raw_string)
            break
        except ValueError:
            print("ValueError: " + raw_string + " is not a number.")
            print("Please enter a valid number.")

    name_dict, start_accounts = get_start_accounts(n_people)
    inv_name_dict = {v: k for k, v in name_dict.items()}

    print("The initial balance after all spendings are:")
    for name in name_dict.keys():
        print(name + ": " + str(start_accounts[name_dict[name]]))

    payment_matrix = generate_payments(start_accounts)

    for i, row in enumerate(payment_matrix):
        for j, payment in enumerate(row):
            if payment > 0.01:
                print(inv_name_dict[j] + " has to pay " + str(round(payment, 2)) + " to " + inv_name_dict[i])


def generate_payments(accounts):
    high_spender = None
    low_spender = None
    payment_matrix = [[0.0 for i in range(len(accounts))] for j in range(len(accounts))]
    while high_spender != low_spender or high_spender is None:
        high_spender = accounts.index(max(accounts))
        low_spender = accounts.index(min(accounts))

        average_account = sum(accounts) / float(len(accounts))
        max_account = accounts[high_spender]
        min_account = accounts[low_spender]

        if abs(max_account - average_account) < 0.01 or abs(average_account - min_account) < 0.01:
            break

        p_max_to_min = min([max_account - average_account, average_account - min_account])
        p_min_to_max = -p_max_to_min

        payment_matrix[high_spender][low_spender] = p_max_to_min
        payment_matrix[low_spender][high_spender] = p_min_to_max

        accounts[high_spender] -= p_max_to_min
        accounts[low_spender] -= p_min_to_max

    return payment_matrix


def get_start_accounts(n):
    start_accounts = [0.0 for i in range(n)]
    name_dict = {}
    for i in range(n):
        new_name = input("Please enter the name of person " + str(i + 1) + ".\n")
        name_dict[new_name] = i
        start_accounts[i] = 0.0
        new_spending = 0.0

        raw_string = input("Please enter " + new_name + "'s first spending (0 to quit).\n")
        try:
            new_spending = float(raw_string)
            start_accounts[i] += new_spending
        except ValueError:
            print("ValueError: " + raw_string + " is not a number.")
            print("Please enter a valid number.")

        while abs(new_spending) >= 0.01:
            raw_string = input("Please enter " + new_name + "'s next spending.\n")
            try:
                new_spending = float(raw_string)
                start_accounts[i] += new_spending
            except ValueError:
                print("ValueError: " + raw_string + " is not a number.")
                print("Please enter a valid number.")

    return name_dict, start_accounts


if __name__ == '__main__':
    main()
