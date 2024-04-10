# Standard library imports
from datetime import datetime

# Local application or library-specific imports
from loan import Loan

class Repayment(Loan):

    def __init__(self, initial_amount):
        super().__init__(initial_amount)
        self._outstanding_amount = initial_amount
        self._end_date = super().start_date

    @property
    def end_date(self):
        return self.end_date
    
    @end_date.setter
    def end_date(self, value):
        self._end_date = str(datetime.strptime(value, "%Y-%m-%d").strftime("%Y-%m-%d"))

    def change_start_date(self, value):
        self.start_date = value

    def change_rate(self, value):
        self.rate = value

my_loan = Repayment(100)

my_loan.end_date = "2024-04-12"

print(my_loan.__dict__)