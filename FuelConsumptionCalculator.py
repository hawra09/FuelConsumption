def fuel_cost_calculator():
    distance = float(input('Enter the total distance (in miles):'))
    fuel_efficiency = float(input('Enter fuel efficiency (miles per liter:'))
    fuel_price = float(input('Enter fuel price per liter:'))
    fuel_needed = distance / fuel_efficiency
    total_cost = fuel_needed * fuel_price

    print(f'Total fuel needed: {fuel_needed:.2f} liters!')
    print(f'Total cost: ${total_cost:.2f}')
