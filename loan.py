class Loan:

    AVG_RATE = 6

    def __init__(self, loan, avg_rate=AVG_RATE):
        self.loan = loan
        self.avg_rate = avg_rate
    
    @property
    def loan(self):
        return self._loan
    
    @loan.setter
    def loan(self, value):
        if not (isinstance(value, (float, int)) and value >= 0):
            raise ValueError("Not a loan must be positive decimal or integer")
        self._loan = value
    
    @property
    def avg_rate(self):
        return self._avg_rate
    
    @avg_rate.setter
    def avg_rate(self, value):
        if not(isinstance(value, (float, int))):
            raise ValueError("Not an decimal or integer")
        if not 0 <= value <= 100:
            raise ValueError("Not a rate between 0 and 100")
        self._avg_rate = value
    

my_loan = Loan(100)

print(my_loan.avg_rate)