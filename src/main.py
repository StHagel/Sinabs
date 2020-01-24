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
    n_people = 0
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
    for name in start_accounts.keys():
        print(name + ": " + str(start_accounts[name]))


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
