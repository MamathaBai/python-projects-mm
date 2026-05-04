favorite_language = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python'
    }
friends = ['phil','sarah']
for name in favorite_language.keys():
    print(f'Hi,{name.title()}')
    if name in friends:
        language = favorite_language[name].title()
        print(f'\t {name.title()},I see you love {language} !')
