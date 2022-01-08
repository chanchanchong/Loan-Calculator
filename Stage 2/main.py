class LoanCalculator:
    def __init__(self):
        self.loan_principal_message = 'Loan principal: 1000'
        self.final_output_message = 'The loan has been repaid!'
        self.first_month_message = 'Month 1: repaid 250'
        self.second_month_message = 'Month 2: repaid 250'
        self.third_month_message = 'Month 3: repaid 500'

    def start(self):
        print(self.loan_principal_message)
        print(self.first_month_message)
        print(self.second_month_message)
        print(self.third_month_message)
        print(self.final_output_message)


def main():
    loan = LoanCalculator()
    loan.start()


if __name__ == '__main__':
    main()
