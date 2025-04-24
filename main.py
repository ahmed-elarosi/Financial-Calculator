def calculate_finances(monthly_income: float, tax_rate: float, currency: str) -> None:

    monthly_tax: float = monthly_income * (tax_rate / 100)
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_salary: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_salary - yearly_tax

    print("-------------------------------------------------------------")
    print(f"Monthly Income: {currency}{monthly_income:,.2f}")
    print(f"Tax Rate: {tax_rate:,.0f}%")
    print(f"Monthly Tax: {currency}{monthly_tax:,.2f}")
    print(f"Monthly Net Income: {currency}{monthly_net_income:,.2f}")
    print(f"Yearly Income: {currency}{yearly_salary:,.2f}")
    print(f"Yearly Tax: {currency}{yearly_tax:,.2f}")
    print(f"Yearly Net Income: {currency}{yearly_net_income:,.2f}")
    print("-------------------------------------------------------------")


# calculate_finances(1550, 20, "€")

if __name__ == "__main__":
    print(__name__)
    calculate_finances(1550, 20, "€")
