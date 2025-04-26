def calculate_split(total_amount: float, number_of_people: int, currency: str) -> None:
    if number_of_people < 1:
        raise ValueError("Dude you have to pay for yourself :)")
    share_per_person: float = total_amount / number_of_people

    print(f"Total Expenses: {currency}{total_amount:,.2f}")
    print(f"Number Of People: {number_of_people}")
    print(f"Each Person Should Pay: {currency}{share_per_person:,.2f}")


def main(): ...


if __name__ == "__main__":
    main()
