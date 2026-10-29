color_list1=input("Enter color in color_list1:").split(',')
color_list2=input("Enter color in color_list2:").split(',')

result=[color for color in color_list1 if color not in color_list2]

print("color in color_list1 but not in color_list2:")
print(result)