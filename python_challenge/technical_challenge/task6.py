# write a function that removes repeated characters from a string
# sample strings are: 1). Hello   2). Concatenate

from collections import OrderedDict
def remove_duplicates(value):
        y=list(OrderedDict.fromkeys(value))
        s=''
        for i in y:
            s+=i
        return s
print(remove_duplicates("Hello"))
print(remove_duplicates("Concatenate"))


