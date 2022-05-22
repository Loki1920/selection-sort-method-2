#selection sort 
list1 = [56,3,2,78,6,0]
# sorting in ascending order 
for i in range(len(list1)):
  min_value = min(list1[i:])
  min_index = list1.index(min_value)
  list1[i],list1[min_index] = list1[min_index],list1[i]

print(list1)

# sorting in descending order 
for j in range(len(list1)):
  max_value = max(list1[j:])
  max_index = list1.index(max_value)
  list1[j],list1[max_index] = list1[max_index],list1[j]

print(list1)
