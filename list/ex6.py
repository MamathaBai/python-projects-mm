list = ['USA','India','Germany','France','Italy']
print("Here is the orginal list")
print(list)
print("Here is the sorted list")
print(sorted(list))
language = []
language.append('Telugu')
language.insert(1,'Hindi')
print(language)
language.append('Tamil')
print(language)
language[1] = '999'
print(language)
language.pop()
print(language)
print(f'insert new language {language.append('Tamil')}')
print(language)
print(f'remove number {language.remove('999')}')
print(language)
language.sort()
print(language)
del language[0]
print(language)



