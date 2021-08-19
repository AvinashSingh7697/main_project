# a = "This is a book"
# s = a.split(" ")
# list = []
# for i in s:
#     list.append(i[::-1])
#     joinword = " ".join(list)
# print(joinword)
# for j in joinword:
#     print(j)

# print(s)
# words = s[-1::-1]
# print(words)

# outstring = " ".join(words)
# print(outstring)

s = 'JHGUGvvs'
x= ""
for i in s:
    if i.isupper():
        i= i.lower()
            
    else:
        i = i.upper()
    x += "#".join(i)
print(i)
    

             
lis = "this is a list"
# lis = lis.split(" ")
# print(lis)
lis = "-".join(lis)
print(lis)

for j in range(0,20):
    if (j% 2 == 0):
        print(j)