class Purchase(object):
    def __init__(self, amount):
        self.amount = amount
    def calculateTax(self, taxPercent):
        return self.amount * taxPercent/100.0
    def calculateTip(self, tipPercent):
        return self.amount * tipPercent/100.0
    def calculateTotal(self, taxPercent, tipPercent):
        return self.amount * (1 + taxPercent/100.0 + tipPercent/100.0)
#Bill #1    
purchase = Purchase(100.0)

taxPercent = 7.5
tipPercent = 20.0

tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

print('Bill #1')
print ('Tax:', tax)
print ('Tip',tip)
print(f'Bill total: {purchase.calculateTotal(taxPercent,tipPercent):.2f}')

#Bill #2
purchase = Purchase(35.75)

taxPercent = 7.5
tipPercent = 25.0

tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

print('Bill #2')
print('Tax:',tax)
print('Tip:',tip)
print(f'Bill total: {purchase.calculateTotal(taxPercent,tipPercent):.2f}')
