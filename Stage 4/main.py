import math
import argparse


class LoanCalculator:
    type_choices = ["diff", "annuity"]

    def __init__(self):
        self.payment_message = "Month {}: payment is {}"
        self.overpayment_message = "Overpayment = {}"
        self.annuity_message = "Your annuity payment = {}!"
        self.principal_message = "Your loan principal = {}!"
        self.periods_message = ["It will take {y} year{} and {m} month{} to repay this loan!",
                                "It will take {} year{} to repay this loan!",
                                "It will take {} month{} to repay this loan!"]
        self.error_message = "Incorrect parameters."

        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--type", choices=LoanCalculator.type_choices)
        self.parser.add_argument("--payment", type=int)
        self.parser.add_argument("--principal", type=int)
        self.parser.add_argument("--periods", type=int)
        self.parser.add_argument("--interest", type=float)
        self.args = self.parser.parse_args()

        arguments = [self.args.type, self.args.payment, self.args.principal,
                     self.args.periods, self.args.interest]
        if self.args.type is None or self.args.type not in LoanCalculator.type_choices:
            print(self.error_message)
            self.parser.exit()
        if self.args.type == "diff" and self.args.payment is not None:
            print(self.error_message)
            self.parser.exit()
        if self.args.interest is None:
            print(self.error_message)
            self.parser.exit()
        if len([a for a in arguments if a is not None]) < 4:
            print(self.error_message)
            self.parser.exit()

        self.i = self.args.interest / (12 * 100)

    def start(self):
        # self.overpayment = (self.payment * n) - P
        # self.overpayment = self.payments - P
        # print((self.args.payment * n) - principal)
        # modes = {'diff': self.diff_calculate, 'annuity': self.annuity_calculate}
        # self.diff_calculate()
        # self.annuity_calculate()
        # self.principal_calculate()
        # print(self.return_periods())
        # print(self.return_principal())
        if self.args.type == self.type_choies[0]:
            self.print_diff()
        elif self.args.type == self.type_choices[1]:
            if self.args.payment is None:
                self.print_payment()
            elif self.args.principal is None:
                self.print_principal()
            elif self.args.periods is None:
                self.print_periods()
        else:
            print(self.error_message)
            self.parser.exit()

    def print_periods(self):
        n = self.return_periods()
        s = lambda p: "s" if p > 12 else ""
        y = n // 12
        m = n % 12
        if n < 12:
            print(self.periods_message[2].format(n, s(n)))
        elif m == 0:
            print(self.periods_message[1].format(y, s(n)))
        else:
            print(self.periods_message[0].format(s(y), s(m), y=y, m=m))
        print(self.overpayment_message.format(self.return_overpayment(self.args.payment * n, self.args.principal)))
        
    def print_principal(self):
        print(self.principal_message.format(self.return_principal()))
        print(self.overpayment_message.format(
            self.return_overpayment(self.args.payment * self.args.periods, self.return_principal())))

    def print_payment(self):
        print(self.annuity_message.format(self.return_annuity()))
        print(self.overpayment_message.format(
            self.return_overpayment(self.return_annuity() * self.args.periods, self.args.principal)))

    def print_diff(self):
        for m in range(1, self.args.periods + 1):
            print(self.payment_message.format(m, self.return_diff(m)))
        print("\n" + self.overpayment_message.format(
            self.return_overpayment(self.return_diff_payment(), self.args.principal)))

    def return_diff_payment(self):
        return sum([math.ceil(self.args.principal / self.args.periods + self.i * (
                self.args.principal - ((self.args.principal * (m - 1)) / self.args.periods))) for m in
                    range(1, self.args.periods + 1)])

    def return_diff(self, m):
        return math.ceil(self.args.principal / self.args.periods + self.i * (
                self.args.principal - ((self.args.principal * (m - 1)) / self.args.periods)))

    def return_annuity(self):
        return math.ceil(self.args.principal * (
                (self.i * ((1 + self.i) ** self.args.periods)) / (((1 + self.i) ** self.args.periods) - 1)))

    def return_principal(self):
        return math.floor(sum([self.args.payment / ((1 + self.i) ** m) for m in range(1, self.args.periods + 1)]))

    def return_periods(self):
        return math.ceil(math.log((self.args.payment / (self.args.payment - self.i * self.args.principal)), 1 + self.i))

    def return_overpayment(self, payments, P):
        return payments - P


def main():
    loan = LoanCalculator()
    loan.start()


if __name__ == '__main__':
    main()
