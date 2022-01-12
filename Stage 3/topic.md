# Work on project. Stage 3/4: Annuity payment

#### Description
Let's compute all the parameters of the loan. There are at
least two kinds of loan: those with annuity payment and 
those with differentiated payment. In this stage, you are 
going to calculate only the annuity payment which is fixed
during the whole loan term.

Here is the formula:
A<sub>*ordinary_annuity*</sub> = P * (i * (1 + i)<sup>*n*</sup>) / (1 + i)<sup>*n*</sup> - 1

Where:
*A* = annuity payment;
*P* - loan principal;
*i* - nominal (monthly) interest rate. Usually, it's 1/12 of the
annual interest rate, and usually, it's a floating value, not a 
percentage. For example, if your annual interest rate = 12%, then
i = 0.01;

*n* = number of payments. This is usually the number of 
months in which repayments will be made.

You are interested in four values: the number of monthly
payments required to repay the loan, the monthly payment
amount, the loan principal, and the loan interest. Each of 
these values can be calculated if others are known:

**Loan principal**:
P = A / ((i * (1 + i)<sup>*n*</sup>) / ((1 + i)<sup>*n*</sup> - 1))

**The number of payments**:
n = log<sub>*1 + i*</sub> (A / (A - i * P))

#### Objectives
In this stage, you should add new behavior to the calculator:

1. First, you should ask the user which parameter they want to calculate. The 
   calculator should be able to calculate the number of monthly payments, the 
   monthly payment amount, and the loan principal.
2. Then, you need to ask them to input the remaining values.
3. Finally, computer and output the value that they wanted.

        Note that the user inputs the interest rate as a percentage, for example 11.7, so you
        should divide this value by 100 to use it in the formula above.

Please be careful converting "X months" to "Y years and Z months". Avoid writing "0
years and 11 months" (output "11 months" instead) and "1 years and 0 months" (output "1
year" instead).

Note that in this stage, you have to ask the user to input parameters in a specific order
which is provided below. Simply skip the value the user wants to calculate:
- The first is the loan principal.
- The second is the monthly payment.
- The next is the number of monthly payments.
- The last is the loan interest.

#### Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that 
this is not part of the input.

##### Example 1
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
> n
Enter the loan principal:
> 1000000
Enter the monthly payment:
> 15000
Enter the loan interest:
> 10
It will take 8 years and 2 months to repay this loan!

Le's take a closer look at **Example 1**.

You know the loan principal, the loan interest and want to calculate the number of 
monthly payments. What do you do?

1. You need to know the nominal interest rate. It calculated like this:
   i = 10% / 12 * 100% = 0.0083333...
2. Now you can calculate the number of months:
   n = log<sub>1 + 0.0083333...</sub> (15000 / 1500 - 0.008333 * 1000000) = 97.71...
3. You need an integer number, so let's round it up. Notice that the user will pay the 
   same amount every month for 97 months, and in the 98 month the user will pay 0.71...
   of the monthly payment, So, there are 98 months to pay.
   n = 98

4. Finally, you need to convert "98 months" to "8 years and 2 months" so that it is more 
   readable and understandable for the user.

###### Example 2
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
> n
Enter the loan principal:
> 100000
Enter the monthly payment:
> 15000
Enter the loan interest:
> 10
It will tke 8 years and 2 months to repay this loan!