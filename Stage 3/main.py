import math


class LoanCalculator:
    def __init__(self):
        self.opening_message = '''What do you want to calculate
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal: '''
        self.ask = ["Enter the loan principal: ", "Enter the monthly payment: ",
                    "Enter the number of periods: ", "Enter the loan interest: ",
                    "Enter the annuity payment:"]
        self.n_month_messages = ["It will take {y} year{} and {m} month{} to repay this loan!",
                                 "It will take {} year{} to repay this loan!",
                                 "It will take {} month{} to repay this loan!"]
        self.return_message = ["Your monthly payment = {}!", "Your loan principal = {}!"]
        self.n_month = 0
        self.annuity = 0
        self.loan_principal = 0
        self.loan_interest = 0
        self.payment = 0


    def start(self):
        calculate = {'n': self.n_month_calculate, 'a': self.annuity_calculate, 'p': self.principal_calculate}
        print(calculate[input(self.opening_message)]())

    def n_month_calculate(self):
        self.loan_principal = int(input(self.ask[0]))
        self.payment = int(input(self.ask[1]))
        self.loan_interest = float(input(self.ask[3]))
        ni_rate = self.loan_interest / (12 * 100)
        self.n_month = math.ceil(math.log((self.payment / (self.payment - ni_rate * self.loan_principal)), 1 + ni_rate))

        if self.n_month < 12:
            return self.n_month_messages[2].format(self.n_month, "s" if self.n_month > 12 else "")
        elif self.n_month == 12:
            return self.n_month_messages[1].format(self.n_month, "s" if self.n_month > 1 else "")
        else:
            y = self.n_month // 12
            m = self.n_month % 12
            return self.n_month_messages[0].format("s" if y > 1 else "", "s" if m > 1 else "", y=y, m=m, )

    def annuity_calculate(self):
        self.loan_principal = int(input(self.ask[0]))
        self.n_month = int(input(self.ask[2]))
        self.loan_interest = float(input(self.ask[3]))
        i = self.loan_interest / (12 * 100)
        self.payment = math.ceil(
            self.loan_principal * ((i * ((1 + i) ** self.n_month)) / (((1 + i) ** self.n_month) - 1)))
        return self.return_message[0].format(self.payment)

    def principal_calculate(self):
        self.annuity = float(input(self.ask[4]))
        self.n_month = int(input(self.ask[2]))
        self.loan_interest = float(input(self.ask[3]))
        i = self.loan_interest / (12 * 100)
        self.loan_principal = math.floor(
            self.annuity / ((i * ((1 + i) ** self.n_month)) / (((1 + i) ** self.n_month) - 1)))
        return self.return_message[1].format(self.loan_principal)


def main():
    loan = LoanCalculator()
    loan.start()


if __name__ == '__main__':
    main()
