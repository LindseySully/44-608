dice_rolls = [1,3,4,2,6,5,3,4,5,2]

import statistics

print(f'Variance: {statistics.pvariance(dice_rolls):.2f}')
print(f'Standard Deviation: {statistics.pstdev(dice_rolls):.2f}')
print('Written by Lindsey Sullivan')