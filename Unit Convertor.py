value = float(input("Enter your value here.. "))
unit1 = input('Enter the unit of giver value..')
unit2 = input('Enter the unit in which you want to convert the given unit of value...')

if unit1 == 'km' and unit2 == 'm':
    result = float(value)*1000
    print(result)

elif unit1 == 'm' and unit2 == 'cm':
    result = float(value)*100
    print(result)

elif unit1 == 'cm' and unit2 == 'm':
    result = float(value)/100
    print(result)

elif unit1 == 'feet' and unit2 == 'inch':
    result = float(value)*12
    print(result)