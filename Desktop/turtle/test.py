numbers_input = list(map(float, input("Enter maximum 7 numbers only: ").split()))
list_number = []

for i in numbers_input:
    i = i.__round__(1)
    list_number.append(i)
print(list_number)
sum = 0
angles = []

for i in list_number:
    sum = sum + i

for i in list_number:
    i = (360 * (i * (sum/100))/100)
    angles.append(i)
for i in angles:
    new = angles[i] + angles[i - 1]

print(new)