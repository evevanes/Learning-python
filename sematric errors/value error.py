class TaxPayer:
  income = 0
  def __init__(self,income):
    self.income = income
    self.validateIncome()
    
  def validateIncome(self):
    if self.income.isnumeric() == False:
      raise ValueError("The income {} is not numeric".format(self.income))
      
  def calculate_tax(self):
    return float(self.income) * 0.3
    
income = input("What is your income:")
employee = TaxPayer(income)
print(employee.calculate_tax())