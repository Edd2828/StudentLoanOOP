# Standard library imports
from datetime import datetime, UTC


class Loan:

    ERROR_MESSAGE_1 = "Must be positive decimal or integer"
    ERROR_MESSAGE_2 = "Not a rate between 0 and 100"
    
    START_DATE = str(datetime.now(UTC).strftime("%Y-%m-%d"))
    RATE = 0

    def __init__(self, initial_amount, start_date=START_DATE, rate=RATE):
        self.initial_amount = initial_amount
        self.start_date = start_date
        self.rate = rate
    
    @property
    def initial_amount(self):
        return self._initial_amount
    
    @initial_amount.setter
    def initial_amount(self, value):
        if not (isinstance(value, (float, int)) and value >= 0):
            raise ValueError(self.ERROR_MESSAGE_1)
        self._initial_amount = value
    
    @property
    def outstanding_amount(self):
        return self._outstanding_amount
    
    @outstanding_amount.setter
    def outstanding_amount(self, value):
        if not(isinstance(value, (float, int)) and value >= 0):
            raise ValueError(self.ERROR_MESSAGE_1)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, value):
        if not(datetime.strptime(value, "%Y-%m-%d")):
            pass
        self._start_date = value
    
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, value):
        if not(datetime.strptime(value, "%Y-%m-%d")):
            pass
        self._end_date = value
    
    @property
    def rate(self):
        return self._rate
    
    @rate.setter
    def rate(self, value):
        if not(isinstance(value, (float, int))):
            raise ValueError(self.ERROR_MESSAGE_1)
        if not 0 <= value <= 100:
            raise ValueError("Not a rate between 0 and 100")
        self._rate = value