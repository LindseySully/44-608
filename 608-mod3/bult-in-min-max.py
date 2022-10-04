def max(value1, value2, value3):
    max_value = value1
    if value2 > max_value:
            max_value = value2
    if value3 > max_value:
            max_value = value3
    return max_value
print('The maximum is: ',max(12,27,36))

def min(value1,value2,value3):
    min_value = value1
    if value2 < min_value:
            min_value = value2
    if value3 < min_value:
            min_value = value3
    return min_value
print('The minimum is:',min(15,9,27))

print('Code written by - Lindsey Sullivan')