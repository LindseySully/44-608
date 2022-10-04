import random

""" Rolling Two six-sided dice 6 million times"""
frequency1 = 0 
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0
frequency7 = 0
frequency8 = 0
frequency9 = 0
frequency10 = 0
frequency11 = 0
frequency12 = 0
#need to hold the number of rolls for fractions
number_of_rolls = 6_000_000
#Dice Rolls
for roll in range(number_of_rolls):
    face = random.randrange(1,7)+random.randrange(1,7)

    #increase freqency counters
    if face == 1:
            frequency1 += 1
    elif face == 2:
            frequency2 += 2
    elif face == 3:
            frequency3 += 3
    elif face == 4:
            frequency4 += 4
    elif face == 5:
            frequency5 += 5
    elif face == 6:
            frequency6 += 6
    elif face == 7:
            frequency7 += 7
    elif face == 8:
            frequency8 += 8
    elif face == 9:
            frequency9 += 9
    elif face == 10:
            frequency10 += 10
    elif face == 11:
            frequency11 += 11
    elif face == 12:
            frequency12 += 12
    
print(f'Face{"Frequency":>13}')
print(f'{1:>4}{frequency1:>13}')
print(f'{2:>4}{frequency2:>13}')
print(f'{3:>4}{frequency3:>13}')
print(f'{4:>4}{frequency4:>13}')
print(f'{5:>4}{frequency5:>13}')
print(f'{6:>4}{frequency6:>13}')
print(f'{7:>4}{frequency7:>13}')
print(f'{8:>4}{frequency8:>13}')
print(f'{9:>4}{frequency9:>13}')
print(f'{10:>4}{frequency10:>13}')
print(f'{11:>4}{frequency11:>13}')
print(f'{12:>4}{frequency12:>13}')


craps = frequency2+frequency3+frequency12
wins = frequency7+frequency11

print(f'Number of craps: {craps/number_of_rolls:.2f}')
print(f'Number of times won: {wins/number_of_rolls:.2f}')
print('Code written by Lindsey Sullivan')