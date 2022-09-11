import re
txt = "The rain in Spain"
x = re.search("^The.*in ", txt)
print(x)
print("first occurence is in position:",x.start(), ' - ',x.end())
x= re.findall("\w+\s*",txt)
print(x)
print(type(x))
print(len(x))
for i in range (len(x)):
    print(x[i].strip())

x=re.split("\s", txt)
print(x)