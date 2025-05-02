# def prompt_float(prompt: str) -> float:
#     while True:
#         try:
#             return float(input(prompt))
#         except ValueError:
#             print("! Please enter a valid number.")


# def calculate_split(total_amount: float, number_of_people: int, currency: str) -> None:
#     if number_of_people < 1:
#         raise ValueError("No one Wanna pay")
#     elif number_of_people == 1:
#         print(f"Dude you have to pay for yourself :) {currency}{total_amount:,.2f}")
#     else:
#         choice = (
#             input("Do you want to split the bill evenly or by percentage? (Yes/No): ")
#             .strip()
#             .lower()
#         )
#         if choice == "yes":
#             share_per_person: float = total_amount / number_of_people
#         if choice == "no":


#     print()
#     print(f"Total Expense: {currency}{total_amount:,.2f}")
#     print(f"Number Of People: {number_of_people}")
#     print(f"Each Person Should Pay: {currency}{share_per_person:,.2f}")


# def main():
#     total_amount: float = prompt_float("Enter The Total Amount of The Expense: ")
#     number_of_people: int = prompt_float("Enter Number of People: ")
#     calculate_split(total_amount, number_of_people, "€")


# if __name__ == "__main__":
#     main()


def prompt_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("! Please enter a valid number.")


def calculate_split(total_amount: float, number_of_people: int, currency: str) -> None:
    if number_of_people < 1:
        raise ValueError("No one Wanna pay")
    elif number_of_people == 1:
        print(f"Dude you have to pay for yourself :) {currency}{total_amount:,.2f}")
    else:
        choice = (
            input("Do you want to split the bill evenly? (Yes/No): ").strip().lower()
        )

        print()
        print(f"Total Expense: {currency}{total_amount:,.2f}")
        print(f"Number Of People: {int(number_of_people)}")

        if choice == "yes":
            share_per_person: float = total_amount / number_of_people
            for i in range(1, int(number_of_people) + 1):
                print(f"Person {i} should pay: {currency}{share_per_person:,.2f}")

        elif choice == "no":
            percentages = []
            total_percent = 0.0

            for i in range(1, int(number_of_people)):
                percent = prompt_float(f"Enter percentage for person {i}: ")
                total_percent += percent
                if total_percent >= 100.0:
                    print(
                        f"\nError: You've already assigned {total_percent}%. It must be less than 100% before the last person."
                    )
                    return
                percentages.append(percent)

            # Automatically calculate the last person's percentage
            last_percent = 100.0 - total_percent
            percentages.append(last_percent)
            print(
                (
                    f"Person {number_of_people} will automatically pay the remaining "
                    f"{last_percent:.2f}%",
                )
            )

            # Calculate and print how much each person should pay
            for i, percent in enumerate(percentages, start=1):
                amount = total_amount * (percent / 100)
                print(f"Person {i} should pay: {currency}{amount:,.2f}")

        else:
            print("Invalid choice. Please enter 'Yes' or 'No'.")


def main():
    total_amount: float = prompt_float("Enter the total amount of the expense: ")
    number_of_people: int = int(prompt_float("Enter number of people: "))
    calculate_split(total_amount, number_of_people, "€")


if __name__ == "__main__":
    main()
