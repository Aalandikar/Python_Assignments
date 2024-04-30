#EMI = [P x R x (1+R)^N]/[(1+R)^N-1]
#EMI=(loanAmount * rate *(1+rate)**(numberOfMonths))/(1+rate)**(numberOfMonths-1)
def calculate_EMI(loanAmount, rate, years):
    rate = rate / 12 / 100
    numberOfMonths = years * 12
    if rate > 0:
        EMI=(loanAmount * rate *((1+rate)**(numberOfMonths)))/((1+rate)**(numberOfMonths-1))
    else:
        EMi = loanAmount / numberOfMonths
    
    return EMI


loanAmount = float(input("Enter the loan amount: "))
rate = float(input("Enter the annual interest rate (in percentage): "))
years = int(input("Enter the number of years for the loan: "))
EMI = calculate_EMI(loanAmount,rate, years)
print("The monthly EMI for the loan will be:-> ",EMI)

