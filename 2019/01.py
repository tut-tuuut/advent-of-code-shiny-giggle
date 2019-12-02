with open(__file__ + '.input') as file:
    input = file.read()

def fuel_for_given_module(inputRow):
    return int(int(inputRow)/3)-2

print(f"this should be 2 : {fuel_for_given_module('12')}")
print(f"this should be 2 : {fuel_for_given_module('14')}")
print(f"this should be 654 : {fuel_for_given_module('1969')}")
print(f"this should be 33583 : {fuel_for_given_module('100756')}")

print('first puzzle solution:')
print(sum(list(map(fuel_for_given_module, input.split('\n')))))

def fuel_for_given_module_and_fuel(inputRow):
    amount = fuel_for_given_module(inputRow)
    fuelAmount = fuel_for_given_module(amount)
    while fuelAmount > 0:
        amount += fuelAmount
        fuelAmount = fuel_for_given_module(fuelAmount)
    return amount

print(f"this should be 2 : {fuel_for_given_module_and_fuel('14')}")
print(f"this should be 966 : {fuel_for_given_module_and_fuel('1969')}")
print(f"this should be 50346 : {fuel_for_given_module_and_fuel('100756')}")

print('second puzzle solution:')
print(sum(list(map(fuel_for_given_module_and_fuel, input.split('\n')))))