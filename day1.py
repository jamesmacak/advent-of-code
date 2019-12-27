module = open('day1_module.txt', 'r')
fuel_requirement = 1
total_fuel_required = 0

for mass in module:
    fuel_requirement = int(mass)
    while fuel_requirement // 3 - 2 > 0:
        fuel_requirement = fuel_requirement // 3 - 2
        total_fuel_required += fuel_requirement

module.close()
print(total_fuel_required)