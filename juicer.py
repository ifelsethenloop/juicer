# E-juice nicotine mixing calculator

amount = int(input('Bottle size in (ml): '))
current = int(input('Current nicotine concentration of E-liquid (mg/ml): '))
nic_base = int(input('Nicotine base strength (mg/ml): '))
target = int(input('Desired nicotine strength (mg/ml): '))

# Calculate what the new target should be from user input
target_converted = target - current

if current == 0:
    print(' ({}ml bottle) / ({}mg/ml nicotine strength) x ({}mg/ml nicotine target strength) = '\
        .format(amount, nic_base, target))
    print(amount / nic_base * target,'ml')
else:
    print('You entered a current nicotine level of {}mg and target of {}mg, gap in \'mg\' is {}mg ' \
        .format(current, target, target_converted))
    print(' ({}ml bottle) / ({}mg/ml nicotine strength) x ({}mg/ml nicotine target strength) = '\
        .format(amount, nic_base, target_converted))
    print(amount / nic_base * target_converted, 'ml')