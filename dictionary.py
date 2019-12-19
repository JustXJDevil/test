alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)
del alien_0['points']
print(alien_0)


user_0 = {
    'name':'efermi',
    'first':'enrico',
    'last':'fermi',
    '1':'1',
    '2':'2',
    '3':'1',
    '4':'1'
    }
for key,value in user_0.items():
    print('\nkey:'+key)
    print('value:'+value)
for key in user_0:
    print('key:'+key)
for v in user_0.values():
    print('value:'+v)
print('\n')
for v in set(user_0.values()):
    print('value:'+v)
print("============")

alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
print("=========")

aliens = []
for num in range(30):
    new_alien = {'color':'green','points':5}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print('aliens_num:'+str(len(aliens)))
print("=============")

pizza = {
    'crust':'thick',
    'toppings':['mushroom','extra cheese']
    }
print(pizza['toppings'])
for topping in pizza['toppings']:
    print(topping)
