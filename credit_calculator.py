import argparse
import math


parser = argparse.ArgumentParser(description='Credit Calculator')

parser.add_argument('--type', choices=['annuity', 'diff', 'a', 'p'], help='Type of payments')
parser.add_argument('--principal', type=float, help='Credit principal')
parser.add_argument('--periods', type=int, help='Number of months')
parser.add_argument('--interest', type=float, help='Interest rate')

parser.add_argument('--payment', type=float, help='Monthly payment')

args = parser.parse_args()

if not args.type:
    print('Incorrect parameters')
elif args.type == 'annuity' and not (args.principal and args.periods and args.interest):
    print('Incorrect parameters')
elif args.type == 'diff' and not (args.principal and args.periods and args.interest):
    print('Incorrect parameters')
elif args.type == 'a' and not (args.payment and args.periods and args.interest):
    print('Incorrect parameters')
elif args.type == 'p' and not (args.payment and args.periods and args.interest):
    print('Incorrect parameters')

elif args.type == 'p':
    annuity_payment = args.payment
    periods = args.periods
    interest_rate = args.interest

    loan_principal = annuity_payment / (
            (interest_rate * math.pow(1 + interest_rate, periods)) / (math.pow(1 + interest_rate,periods) -1))

    print(f"Your loan principal = {round(loan_principal)}!")

elif args.type == 'a':
    principal = args.principal
    periods = args.periods
    interest_rate = args.interest
    monthly_interest = interest_rate / 100 / 12
    payment = (principal * monthly_interest) / (1 - (1+ monthly_interest) ** (-periods))
    print(f"Your monthly payment = {round(payment)}!")


elif args.type == 'annuity' and args.payment and args.periods:
    i = args.interest / 1200  # месячная процентная ставка
    A = args.payment
    P = args.principal

    n = math.log(A / (A - i * P), 1 + i)
    years = math.floor(n / 12)
    months = math.ceil(n % 12)

    overpayment = round(A * (years * 12 + months) - P, 0)

    if years == 0:
        print(f"It will take {months} months to repay this loan!")
    elif months == 0:
        print(f"It will take {years} years to repay this loan!")
    else:
        print(f"It will take {years} years and {months} months to repay this loan!")

    print(f"Overpayment = {overpayment}")

elif args.type == 'annuity' and args.payment and not args.periods:
    i = args.interest / 1200  # месячная процентная ставка
    A = args.payment
    P = args.principal

    n = math.log(A / (A - i * P), 1 + i)
    months = math.ceil(n)
    years = months // 12
    remaining_months = months % 12

    overpayment = round(A * months - P, 0)

    if years == 0:
        print(f"It will take {months} months to repay this loan!")
    elif remaining_months == 0:
        print(f"It will take {years} years to repay this loan!")
    else:
        print(f"It will take {years} years and {remaining_months} months to repay this loan!")

    print(f"Overpayment = {overpayment}")

elif args.type == 'annuity' and not args.payment and args.periods:
    i = args.interest / 1200  # месячная процентная ставка
    n = args.periods
    P = args.principal

    A = round(P * ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
    years = n // 12
    remaining_months = n % 12

    overpayment = round(A * n - P, 0)

    if years == 0:
        print(f"Your annuity payment = {A}!")
        print(f"It will take {remaining_months} months to repay this loan!")
    elif remaining_months == 0:
        print(f"Your annuity payment = {A}!")
        print(f"It will take {years} years to repay this loan!")
    else:
        print(f"Your annuity payment = {A}!")
        print(f"It will take {years} years and {remaining_months} months to repay this loan!")

    print(f"Overpayment = {overpayment}")

elif args.type == 'diff':
    loan_principal = args.principal
    periods = args.periods
    interest_rate = args.interest / (12 * 100)

    total_payment = 0
    for m in range(1, periods + 1):
        payment = loan_principal / periods + interest_rate * (loan_principal - loan_principal * (m - 1) / periods)
        total_payment += payment
        print(f"Month {m}: payment is {round(payment, 2)}")

    overpayment = total_payment - loan_principal
    print(f"\nOverpayment = {round(overpayment)}")
else:
    print('Incorrect parameters')