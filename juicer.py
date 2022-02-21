# nicotine mixing calculator

amount = int(input('Bottle size in (ml): '))
current = int(input('Current nicotine concentration of E-liquid (mg/ml): '))
nic_base = int(input('Nicotine base strength (mg/ml): '))
target = int(input('Desired nicotine strength (mg/ml): '))

print(' ({}ml bottle) / ({}mg/ml nicotine strength) x ({}mg/ml nicotine target strength) = '.format(amount, nic_base, target))
print(amount / nic_base * target,'ml')
