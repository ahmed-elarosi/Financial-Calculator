def prompt_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("! Please enter a valid number.")


def calculate_split(total_amount: float, number_of_people: int, currency: str) -> None:
    if number_of_people < 1:
        raise ValueError("Dude you have to pay for yourself :)")
    share_per_person: float = total_amount / number_of_people

    print()
    print(f"Total Expense: {currency}{total_amount:,.2f}")
    print(f"Number Of People: {number_of_people}")
    print(f"Each Person Should Pay: {currency}{share_per_person:,.2f}")


def main():
    total_amount: float = prompt_float("Enter The Total Amount of The Expense: ")
    number_of_people: int = prompt_float("Enter Number of People: ")
    calculate_split(total_amount, number_of_people, "€")


if __name__ == "__main__":
    main()
