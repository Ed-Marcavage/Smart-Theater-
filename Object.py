class Menu:
  
# Initializer 
  def __init__(self,total):
    self.total = total
    
  def total_taxed(self, tax_rate):
    total_taxed = self.total + (self.total * tax_rate)
    total_taxed = round(total_taxed, 2)             #round it to 2 decimal places
    return total_taxed

    
    