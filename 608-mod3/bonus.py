import random
import statistics


#random data set that pulls 100 values from the range 0 - 200
random.seed(33) #set random seed to continue continuity
data_set = random.sample(range(0,200),100)

print('Data set:',data_set, end= ' ')

#Variance and Standard Deviation
print('Variance & Standard Devation Calculations')
print(f'Variance: {statistics.pvariance(data_set):.2f}')
print(f'Standard Deviation: {statistics.pstdev(data_set):.2f}')
print('Code written by Lindsey Sullivan')