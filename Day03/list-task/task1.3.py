def unique_numbers(lst):
    result=[]
    
    for  num in lst:
        if num not in result:
            result.append(num)
    return result

input=[2,2,2,3,7,7,7,10,15,15,15,20,20,25,25]

print("Input list:", input)
print("Unique numbers:", unique_numbers(input))