# a = [2,3,46,5,78,9]

# for i in a:
#     print(a.count(5))

# print("Checking if 15 exists in list")
 
# # number of times element exists in list
# test_list = [10, 15, 20, 7, 46, 2808]
# exist_count = test_list.count(15)
 
# # checking if it is more then 0
# if exist_count > 0:
#     print(i,a[i])
# else:
#     print("No, 15 does not exists in list")


# # Python code to demonstrate
# # checking of element existence
# # using loops and in

# # Initializing list
# test_list = [ 1, 6, 3, 5, 3, 4 ]

# print("Checking if 4 exists in list ( using loop ) : ")

# # Checking if 4 exists in list
# # using loop
# for i in test_list:
# 	if(i == 4) :
# 		print ("Element Exists")

# print("Checking if 4 exists in list ( using in ) : ")

# # Checking if 4 exists in list
# # using in
# if (4 in test_list):
# 	print ("Element Exists",i,test_list[i])
def search(a, key):
    

    for i in range(len(a)):
        if key == a[i]:
            print("found element", key, i)
            break
    else:
        print("nf")
            

a = [3,52,1,43,56]
key = int(input("find no"))
search(a, key)


print("----")
def fabo(z):
    if z == 0:
        return 1
    else:
        return z * fabo(z-1)
n = 5


print(f"the value of {n}! is {fabo(n)}")
