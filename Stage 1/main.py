class LoanCalculator:
    def __init__(self):
        self.loan_principal_message = 'Loan principal: {}'
        self.final_output_message = 'The loan has been repaid!'
        self.monthly_message = 'Month {}: repaid {}'

    def start(self):
        print(self.loan_principal_message.format(1000))
        print(self.monthly_message.format(1, 250))
        print(self.monthly_message.format(2, 250))
        print(self.monthly_message.format(3, 500))
        print(self.final_output_message)


def main():
    loan = LoanCalculator()
    loan.start()


if __name__ == '__main__':
    main()
