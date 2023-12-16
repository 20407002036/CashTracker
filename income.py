#!/usr/bin/python3

class Income():
    """ Class Income that has the attributes:
    Time,
    Source
    Amount
    """
    def __init__(self,Source=None, Amount=0):
        """
        The initialization function for the class Inclome
        """

        # self.Time = Time
        self.Source = Source
        self.Amount = Amount

    def verifySource(self):
        """
        This Method will be used to verify the source given
        """

        if(type(self.Source) != str):
            raise Exception("Your Source Must be a String...")
        
        else:
            return True


