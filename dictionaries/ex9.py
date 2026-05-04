country_rivers = {'nile' : 'egypt',
'india' :'ganga',
'usa' : 'virgin'
}
for name,rivers in country_rivers.items():
    print(f'{name.title()} country river is {rivers.title()}')