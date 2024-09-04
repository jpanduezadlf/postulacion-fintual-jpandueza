from datetime import datetime as dt

class Portfolio:
    def __init__(self, stocks = None):
        #The portfolio can be defined without stocks, and it should have a function to buy new stocks, but it will enter this "if"
        #whenever the portfolio was defined empty. For this exercise, this part of the code could have not been done, but I like having
        #a more realistic class
        if stocks == None:
            self.stocks == []
        #Whenever the class does have stocks, it will define them here (I'm taking the supposition that stock is a class and stocks is
        #a list of instances of that class)
        else:
            self.stocks = stocks

    def profit(self, startDate, endDate):
        #We calculate the period in years and the return calling the corresponding function
        t = self.calculateT(startDate, endDate)
        ret = self.calculateReturn(startDate, endDate)
        #Then, calculate the Annualized Return and give it back to the user
        annualized_return = ((1 + ret) ** (1 / t)) - 1
        return annualized_return * 100

    #I'm supposing that the dates come as a touple defined as (yyyy, mm, dd)
    def calculateT(self, startDate, endDate):
        #We give the dates a format that would allow us to make operations with daytime (dt)
        firstDate = dt(startDate(0), startDate(1), startDate(2))
        lastDate = dt(endDate(0), endDate(1), endDate(2))
        #After that, we calculate the amount of days
        daysBetween = (lastDate - firstDate).days
        #And return the amount of days divided by 365 to get yearly period (it can also be done with 365.25 for a more precise result)
        return (daysBetween / 365)
    
    def calculateReturn(self, startDate, endDate):
        #We initialize the variables that will contain the initial and final value of the portfolio
        initialPrice, endPrice = 0, 0
        #With a for, we move in the list of stocks adding the value of each stock to our total portfolio value
        for stock in self.stocks:
            #Both initial
            initialPrice += stock.Price(startDate)
            #And final
            endPrice += stock.Price(endDate)
        #Then, we calculate the return and give it back to the caller of the function
        return (endPrice - initialPrice) / initialPrice