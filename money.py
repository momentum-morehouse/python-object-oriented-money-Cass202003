# pylint: disable=unidiomatic-typecheck,unnecessary-pass
# pdb; pdb.set_trace()

class DifferentCurrencyError(Exception):
    pass


class Currency:
    """
    Represents a currency. Does not contain any exchange rate info.
    """

    def __init__(self, name, code, symbol=None, digits=2):
        """
        Parameters:
        - name -- the English name of the currency
        - code -- the ISO 4217 three-letter code for the currency
        - symbol - optional symbol used to designate currency
        - digits -- number of significant digits used
        """
      self.name = name
      self.code = code
      self.symbol = symbol
      self.digits = digits

      def __str__(self):
        if self.symbol:
          return f"{self.code} ({self.symbol})"
        else:
          return f"{self.code}"
      
        """
        Should return the currency code, or code with symbol in parentheses.
        """
       

    def __eq__(self, other):

        """
        All fields must be equal to for the objects to be equal.
        """
        return (type(self) == type(other)      self.name == other.name and
            self.code == other.code and self.symbol == other.symbol and
            self.digits == other.digits)


class Money:
    """
    Represents an amount of money. Requires an amount and a currency.
    """

    def __init__(self, amount ='0' , currency =''):

        """
        Parameters:
        - amount -- quantity of currency
        - currency -- type of currency
        """
        self.amount = amount 
        self.currency = currency
        self.money = []
        for amount in amounts:
          for currency in currencies:
            self.money.append(Money(amount, currency))

    def __str__(self):
      #breakpoint()
      if self.currency.symbol:f"{self.amount:.}
      {self.currency.digits}f}"
         else:
           return self.currency.code:f"{self.amount:.}
      {self.currency.digits}f}"


        """
        Should use the currency symbol if available, else use the code.
        Use the currency digits to determine number of digits to show.
        """

        

    def __repr__(self):
        return f"<Money {str(self)}>"

    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """

        return (type(self) == type(other) and self.amount == other.amount and
                self.currency == other.currency)

    def add(self, other):
        """
        Add two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        pass

    def sub(self, other):
        """
        Subtract two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        pass

    def mul(self, multiplier):
        """
        Multiply a money object by a number to get a new money object.
        """
        pass

    def div(self, divisor):
        """
        Divide a money object by a number to get a new money object.
        """
        pass
