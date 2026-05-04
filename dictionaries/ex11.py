aleins = []
for alein in range(5):
    new_alein = {'color':'green','points':5}
    aleins.append(new_alein)
for alein in aleins[:2]:
    if alein['color'] == 'green':
        alein['color'] = 'yellow'
        alein['speed'] = 'medium'
        alein['points']  = 10
print(aleins) 
