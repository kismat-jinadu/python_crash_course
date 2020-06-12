#long dictionary

favourite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

language = favourite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}.")

#using loop

for name,language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")

#to access the key only you can use .keys() or not. same output

for name in favourite_languages.keys():
    print(name.title())

for name in favourite_languages:
    print(name.title())

friends=['phil','sarah']
for name in favourite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends: 
        language=favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

#check if a name is in the list

if 'erin' not in favourite_languages.keys():
    print("Erin, please take our poll!")

# to loop in alphabetical order 

for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

#use values() to loop through values

print("The following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())

# use set() to remove repitition

print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())

# to build a set directly you use {}

languages ={'python','ruby','python','c'}
for language in languages:
    print(language.title())

#nesting 

favourite_languages={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby', 'go'],
    'phil':['python', 'haskell'],
    }

for name, languages in favourite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

#correct tense, use len()

favourite_languages={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby', 'go'],
    'phil':['python', 'haskell'],
    }


for name, languages in favourite_languages.items():
    if len(languages)==1:
        print(f"\n{name.title()}'s favourite languages is:")
        for language in languages:
            print(f"\t{language.title()}")
    else:   
        print(f"\n{name.title()}'s favourite languages are:")
        for language in languages:
            print(f"\t{language.title()}")