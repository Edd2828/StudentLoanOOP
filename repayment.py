# Standard library imports
from datetime import datetime, UTC

# Local application or library-specific imports
from loan import Loan


class Repayment(Loan):

    START_DATE = str(datetime.now(UTC).strftime("%Y-%m-%d"))
    RATE = 0

    def __init__(self, end_date, initial_amount, start_date=START_DATE, rate=RATE):
        self.end_date = end_date
        super().__init__(initial_amount, start_date, rate)


my_repayment = Repayment(100)

print(my_repayment.__dict__)