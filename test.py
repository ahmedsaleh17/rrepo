lst = ["20" , 'ahmed', "20" , 'm', "True" , "yes" , "100"]

numbers = [int(item) for item in lst if item.isdigit()]
print(numbers)
