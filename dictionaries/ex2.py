alein_0 = {'x_position' : 0,'y_postion': 25,'speed':'medium'}
print(f'original position: {alein_0['x_position']}')
if alein_0['speed'] == 'slow':
    x_increment = 1
elif alein_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alein_0['x_position'] = alein_0['x_position']+x_increment
print(f'New position: {alein_0['x_position']}')