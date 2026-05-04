favorite_language = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python'
    }
for name in favorite_language:
    print(name.title())
for name , language in favorite_language.items():
    print(f"{name.title()}'s favourite language is {language.title()}")
language = favorite_language['sarah'].title()
print(f'sarah favorite language is {language}.')