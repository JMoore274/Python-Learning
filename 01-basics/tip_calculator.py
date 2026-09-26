bill = float(input('25: $'))
tip_percent = int(input('10: '))

tip = bill * (tip_percent / 100)
total = bill + tip

print(f'Tip: ${tip: .2f}')
print(f'Total: ${total: 2f}')
