from datetime import datetime as dt


class Date:
    def __init__(self):
        # Capturing present data using datetime module
        self.today = dt.today()

    def current_datetime(self):
        """Returns current date and time string using datetime module"""
        return self.today.strftime('%d/%m/%Y'), self.today.strftime('%H:%M:%S')
