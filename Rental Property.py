class RentalPropertyCalculator:
    def __init__(self, rental_income, laundry_income, storage_income, misc_income,
                 taxes, insurance, water_sewer, garbage, electric_gas, hoa_fee, lawn_snow,
                 vacancy, repairs, capex, prop_mgmt, mortgage, downpayment, closing_costs,
                 rehab_budget, misc_other):
        self.rental_income = rental_income
        self.laundry_income = laundry_income
        self.storage_income = storage_income
        self.misc_income = misc_income
        self.taxes = taxes
        self.insurance = insurance
        self.water_sewer = water_sewer
        self.garbage = garbage
        self.electric_gas = electric_gas
        self.hoa_fee = hoa_fee
        self.lawn_snow = lawn_snow
        self.vacancy = vacancy
        self.repairs = repairs
        self.capex = capex
        self.prop_mgmt = prop_mgmt
        self.mortgage = mortgage
        self.downpayment = downpayment
        self.closing_costs = closing_costs
        self.rehab_budget = rehab_budget
        self.misc_other = misc_other

    def calculate_total_monthly_income(self):
        total_monthly_income = self.rental_income + self.laundry_income + \
                               self.storage_income + self.misc_income
        return total_monthly_income

    def calculate_total_monthly_expenses(self):
        total_monthly_expenses = self.taxes + self.insurance + self.water_sewer + self.garbage + \
                                 self.electric_gas + self.hoa_fee + self.lawn_snow + \
                                 self.vacancy + self.repairs + self.capex + self.prop_mgmt + \
                                 self.mortgage
        return total_monthly_expenses

    def calculate_total_monthly_cashflow(self):
        total_monthly_cashflow = self.calculate_total_monthly_income() - \
                                 self.calculate_total_monthly_expenses()
        return total_monthly_cashflow

    def calculate_annual_cashflow(self):
        total_annual_cashflow = self.calculate_total_monthly_cashflow() * 12
        return total_annual_cashflow

    def calculate_total_investment(self):
        total_investment = self.downpayment + self.closing_costs + self.rehab_budget + \
                           self.misc_other
        return total_investment

    def calculate_cash_on_cash_return(self):
        annual_cashflow = self.calculate_annual_cashflow()
        total_investment = self.calculate_total_investment()
        coc_return = (annual_cashflow / total_investment) * 100
        return coc_return


# Test the calculator
if __name__ == "__main__":
    # Example usage
    rental_income = 2000
    laundry_income = 100
    storage_income = 50
    misc_income = 30
    taxes = 300
    insurance = 100
    water_sewer = 50
    garbage = 30
    electric_gas = 80
    hoa_fee = 0
    lawn_snow = 20
    vacancy = 150
    repairs = 100
    capex = 80
    prop_mgmt = 100
    mortgage = 900
    downpayment = 50000
    closing_costs = 3000
    rehab_budget = 2000
    misc_other = 500

    calculator = RentalPropertyCalculator(rental_income, laundry_income, storage_income, misc_income,
                                          taxes, insurance, water_sewer, garbage, electric_gas,
                                          hoa_fee, lawn_snow, vacancy, repairs, capex, prop_mgmt,
                                          mortgage, downpayment, closing_costs, rehab_budget,
                                          misc_other)

    cash_on_cash_return = calculator.calculate_cash_on_cash_return()
    print(f"Cash on Cash Return: {cash_on_cash_return:.2f}%")
