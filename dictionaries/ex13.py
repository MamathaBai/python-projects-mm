favorite_language = {
    'jen' : ['python','rush'],
    'sarah' : ['c'],
    'edwards' : ['rust','go'],
    'phil' : [ 'python','haskell'],
}
for name,languages in favorite_language.items():
    print(f"\t{name.title()}'s favorite language are:")
    for language  in languages:
        print(f"\t{language.title()}")