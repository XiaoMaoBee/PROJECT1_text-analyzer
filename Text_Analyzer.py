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

'''
The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''']


def underline():
    print('-' * 59, end='\n')


USER_PASSWORD = {'Bob': 123,
                 'Ann': 'pass123',
                 'Mike': 'password123',
                 'Liz': 'pass123'}

# Registered credentials
REGUSER = ['Bob', 'Ann', 'Mike', 'Liz']
REGPASS = [123, 'pass123', 'password123', 'pass123']
underline()

print('Welcome to the app. Please log in: ')

# Log in
USER_NAME = input('USERNAME: ')
PASSWORD = input('PASSWORD: ')
underline()

if USER_NAME == '' or PASSWORD == '':
    print('Please enter your login credentials')

elif USER_NAME == '' and PASSWORD == '':
    print('Please enter your login credentials')

elif PASSWORD in '1234567890':
    PASSWORD = int(PASSWORD)

elif USER_NAME not in REGUSER and PASSWORD not in REGPASS:
    print('Sorry: neither user name nor password is registered')
    quit()

elif PASSWORD not in REGPASS:
    print('This password is wrong - not registered')
    quit()

elif USER_NAME not in REGUSER:
    print('This user does not exist - not registered')
    quit()

PAIR = (USER_NAME, PASSWORD)
if PAIR in USER_PASSWORD.items():
    print(f'Welcome {USER_NAME}!')
else:
    print('User name or password is wrong.\nPlease try again.')
    exit()
underline()

print('We have 3 texts to be analyzed.')
# Choose a text to be analyzed

TEXT_CHOICE = input('Enter a number btw. 1 and 3 to select: ')
underline()

while TEXT_CHOICE == '' or int(TEXT_CHOICE) <= 0 or int(TEXT_CHOICE) > 3:
    print('''You either did not provide num btw 1 - 3,\nor no value entered. Please try again.''')
    TEXT_CHOICE = input('Enter a number btw. 1 and 3 to select: ')

TEXT_CHOICE = int(TEXT_CHOICE)

# Define and clean article
ARTICLE = []
SUM_OF_NUMBERS = 0
for word in TEXTS[TEXT_CHOICE -1].split():
    clean = word.strip(",.:;'")
    ARTICLE.append(clean)
    if clean.isnumeric():
        SUM_OF_NUMBERS += int(clean)

ARTICLE1 = ARTICLE.copy()
underline()

# Count words
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

underline()

# Count number of words according to length
couples = {}
while ARTICLE1:
    word = len(ARTICLE1.pop())
    if word not in couples:
        couples[word] = 0

    couples[word] = couples[word] + 1

couples_sorted = sorted(couples.items())

for i, num in couples_sorted:
    print(i, num * '*', num)

underline()

print(f'If we summed all the numbers in '
      f'this text we would get: {SUM_OF_NUMBERS}')
