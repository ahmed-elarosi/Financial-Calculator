def expenses() -> tuple[float, float, float, float, float, float]:
    monthly_rent: float = float(input("Enter your monthly rent:"))
    yearly_rent: float = monthly_rent * 12
    monthly_food_exp: float = float(input("Enter your monthly food expenses:"))
    yearly_food_exp: float = monthly_food_exp * 12
    monthly_gym: float = float(input("Enter your monthly gym membership:"))
    yearly_gym_exp: float = monthly_gym * 12

    return (
        monthly_rent,
        monthly_food_exp,
        monthly_gym,
        yearly_rent,
        yearly_food_exp,
        yearly_gym_exp,
    )


def calculate_finances(monthly_income: float, tax_rate: float, currency: str) -> None:

    (
        monthly_rent,
        monthly_food_exp,
        monthly_gym,
        yearly_rent,
        yearly_food_exp,
        yearly_gym_exp,
    ) = expenses()

    monthly_tax: float = monthly_income * (tax_rate / 100)
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_salary: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_salary - yearly_tax

    total_monthly_expenses = monthly_rent + monthly_food_exp + monthly_gym
    total_yearly_expenses = yearly_rent + yearly_food_exp + yearly_gym_exp

    monthly_net_after_expenses = monthly_net_income - total_monthly_expenses
    yearly_net_after_expenses = yearly_net_income - total_yearly_expenses

    print("-------------------------------------------------------------")
    print(f"Monthly Income: {currency}{monthly_income:,.2f}")
    print(f"Tax Rate: {tax_rate:,.0f}%")
    print(f"Monthly Tax: {currency}{monthly_tax:,.2f}")
    print(f"Monthly Net Income: {currency}{monthly_net_income:,.2f}")

    print()
    print("Monthly Expenses:")
    print(f"  Rent: {currency}{monthly_rent:,.2f}")
    print(f"  Food: {currency}{monthly_food_exp:,.2f}")
    print(f"  Gym: {currency}{monthly_gym:,.2f}")
    print(f"  Total Monthly Expenses: {currency}{total_monthly_expenses:,.2f}")
    print(f"Monthly Income After Expenses: {currency}{monthly_net_after_expenses:,.2f}")
    print()

    print(f"Yearly Income: {currency}{yearly_salary:,.2f}")
    print(f"Yearly Tax: {currency}{yearly_tax:,.2f}")
    print(f"Yearly Net Income: {currency}{yearly_net_income:,.2f}")
    print()
    print("Yearly Expenses:")
    print(f"  Rent: {currency}{yearly_rent:,.2f}")
    print(f"  Food: {currency}{yearly_food_exp:,.2f}")
    print(f"  Gym:  {currency}{yearly_gym_exp:,.2f}")
    print(f"  Total Yearly Expenses: {currency}{total_yearly_expenses:,.2f}")
    print(f"Yearly Income After Expenses: {currency}{yearly_net_after_expenses:,.2f}")
    print("-------------------------------------------------------------")


def main() -> None:
    monthly_income: float = float(input("Enter your monthly salary:"))
    tax_rate: float = float(input("Enter your tax rate (%):"))
    calculate_finances(monthly_income, tax_rate, currency="€")


if __name__ == "__main__":
    main()
