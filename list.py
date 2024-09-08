#List is changeable, meaning it can be changed, added to, remove items in a list, after it has been created.
soda = ['fanta', 'coke', 'sprite', 'mirinda', 'pepsi', 'mouintain dew']
print(soda)
print(len (soda))

names_of_states = ['lagos state', 'rivers state', 'edo state', 'delta state']
names_of_organization = ['jospedam', 'ecobank', 'zenith bank', 'polaris bank', 'union bank', 'fidelity bank', 780, 1.34]
government = ['governor', 'senators', 'president', 'honourable']
print(names_of_states)
print(names_of_organization)
print(government)
print(names_of_organization, names_of_states, government)

#Combination of list
combination_of_list = ['stand', 987, True, 1234]
print(combination_of_list)
print(type (combination_of_list))

combination_of_list_2 = ['standing', -987, False, +345]
print(combination_of_list_2)

combination_of_list_3 = list (('standing', -987, False, +345))
print(combination_of_list_3)

#Accessing names of states value 
print(names_of_states[3])
#Accessing soda (Line 2)
print(soda [-2])
#Accessing names of organization value: Using colon 
print(names_of_organization [2:6])
print(names_of_organization [:6])
print(names_of_organization [2:])
print(names_of_organization [-4:-1])

#Checking if item exist
government_2= ['governor', 'senators', 'president', 'honourable']
if 'president' in government_2:
    print('the president is useless')
else:
    print('the president is the best')
    
#Change the last item
names_of_states[3] = 'abuja'
print(names_of_states)

#Changing range of item values 
fruits = ['orange', 'apple', 'water melon', 'banana', 'guava', 'grapes']
fruits[2:4] = ['mangoes', 'peaches']
print(fruits)

Devices = [ 'Router', 'Switch', 'Laptop', ' Elevetor', 'Network Cables','Firewall','Wireless Access Points (WAPs)']
Devices [3:6] =['Intrusion Detection (IDPS)','Virtual Private Network (VPN) Appliances']
print(Devices)

#Using 'Insert' in python list
Devices = [ 'Router', 'Switch', 'Laptop', ' Elevetor', 'Network Cables','Firewall','Wireless Access Points (WAPs)']
Devices [3] =['Intrusion Detection (IDPS)']
Devices.insert(4,'Virtual Private Network (VPN) Appliances') 
print(Devices)

#Using 'Append' in python list
Devices_2 = [ 'Router', 'Switch', 'Laptop', ' Elevetor', 'Network Cables','Firewall','Wireless Access Points (WAPs)']
Devices_2.append('Cloud Management Access')
print(Devices_2)

#Using 'Extend' in pyhton list 
chocolates = ['snickers', 'diary milk', 'twix']
vegetables = ['okra', 'tomatoes', 'cabbage']
chocolates.extend(vegetables)
print(chocolates)

#Using 'Remove' in python list 
chocolates_2 = ['snickers', 'diary milk', 'twix', 'maryland']
chocolates_2.remove('twix')
print(chocolates_2)

chocolates_3 = ['snickers', 'diary milk', 'twix', 'maryland']
chocolates_3.pop(1)
print(chocolates_3)

chocolates_4 = ['snickers', 'diary milk', 'twix', 'maryland']
del chocolates_4[2]
print(chocolates_4)

chocolates_5 = ['snickers', 'diary milk', 'twix', 'maryland']
chocolates_5.clear()
print(chocolates_5)
