#muj prvni projekt

'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]


def UNDERLINE():
    print('-' * 59, end='\n')


USER_PASSWORD = {'bob': 123,
                 'ann': 'pass123',
                 'mike': 'password123',
                 'liz': 'pass123'}

REGUSER = ['bob', 'ann', 'mike', 'liz']
REGPASS = [123, 'pass123', 'password123', 'pass123']

UNDERLINE()
print('Welcome to the app. Please log in: ')

USER_NAME = input('USERNAME: ')
PASSWORD = input('PASSWORD: ')

if PASSWORD in '1234567890':
    PASSWORD = int(PASSWORD)

if USER_NAME not in REGUSER or PASSWORD not in REGPASS:
    print('User or password not registered')
    quit()
UNDERLINE()

print('We have 3 texts to be analyzed.')
TEXT_CHOICE = int(input('Enter a number btw. 1 and 3 to select: ')) -1

ARTICLE = []
SUM_OF_NUMBERS = 0
for word in TEXTS[TEXT_CHOICE].split():
    clean = word.strip(",.:;'")
    ARTICLE.append(clean)
    if clean.isnumeric():
        SUM_OF_NUMBERS += int(clean)

ARTICLE1 = ARTICLE.copy()
UNDERLINE()

words_num = 0
titlecase = 0
uppercase = 0
lowercase = 0
numeric = 0

while ARTICLE:
    word = ARTICLE.pop()
    words_num += 1
    if word.istitle():
        titlecase += 1
    elif word.isupper():
        uppercase += 1
    elif word.islower():
        lowercase += 1
    elif word.isdigit():
        numeric += 1

print(f'There are {words_num} words in the selected text.',
      f'There are {titlecase} titlecase words.',
      f'There are {uppercase} uppercase words.',
      f'There are {lowercase} lowercase words.',
      f'There are {numeric} numeric strings.',
      sep='\n')

UNDERLINE()

couples = {}
while ARTICLE1:
    word = len(ARTICLE1.pop())
    if word not in couples:
        couples[word] = 0

    couples[word] = couples[word] + 1

couples_sorted = sorted(couples.items())

for i, num in couples_sorted:
    print(i, num * '*', num)

UNDERLINE()

print(f'If we summed all the numbers in '
      f'this text we would get: {SUM_OF_NUMBERS}')
