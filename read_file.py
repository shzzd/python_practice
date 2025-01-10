# To read file
count_file = open('countries.txt', 'r')
# to check if file available
print(count_file.readable())
# to print all lines in list form
print(count_file.readlines())

for c in count_file.readlines():
    print(c)

count_file.close()