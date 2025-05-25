# len function determines length of string.length is counted normally from 1. 

a="hey,there!"
print(len(a))

# string slicing is done if you want a particular part of string. [:n-1]

print(a[1:4:1]) #includes 1 but not 4.
# step over or slice step just steps over to next. 1st means onto next , 2 means onto next 2nd index
# if first before colon is not specified default value is 0 and similarly default after value is length of string.
# in case of negative slicing it is subtracted from the length of the string.

print(a[:])
print(a[-4:-3])
