import math


class LoanCalculator:
    def __init__(self):
        self.loan_ask = "Enter the loan principal:"
        self.option_message = '''What do you want to calculate?\ntype "m" - for number of monthly payments,\ntype "p" - for the monthly payment:'''
        self.month_ask = "Enter the monthly payment:"
        self.month_message = "It will take {} month{} to repay the loan"
        self.n_months_ask = "Enter the number of months:"
        self.n_month = "Your monthly payment = {}"
        self.last_payment_message = "Your monthly payment = {} and the last payment = {}."
        self.principal = 0
        self.months = 0
        self.payment = 0 #self.principal // self.months
        self.last_payment = 0

    def start(self):
        self.principal = int(input(self.loan_ask))
        option = input(self.option_message)[0]
        if option == 'm':
            self.monthly_payment()
        elif option == 'p':
            self.number_month()

    def monthly_payment(self):
        self.payment = int(input(self.month_ask))
        self.month = math.ceil(self.principal / self.payment)
        print(self.month_message.format(self.month, "s" if self.month > 1 else ""))

    def number_month(self):
        self.months = int(input(self.n_months_ask))
        self.payment = math.ceil(self.principal / self.months)
        if self.principal % self.months == 0:
            print(self.n_month.format(self.payment))
        else:
            self.last_payment = self.principal - (self.months - 1) * self.payment
            print(self.last_payment_message.format(self.payment, self.last_payment))
def main():
    loan = LoanCalculator()
    loan.start()


if __name__ == '__main__':
    main()
