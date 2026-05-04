favorite_language = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python'
    }
print("the following language have been mentioned:")
for language in set(favorite_language.values()):
    print(language.title())
'''for name in sorted(favorite_language.keys()):
    print(f'{name.title()}, thank you taking poll')'''
