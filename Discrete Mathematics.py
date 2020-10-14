
def find_cart(list1, list2, n1, n2):
	for i in range(0,n1):
		for j in range(0,n2):
			print("\n"
                  "\n"
                  "{",list1[i],", ",list2[j],"}, ",sep="" , end="")


# creating an empty list
list1 = []
list2 = []

# number of elemetns as input
m1 = int(input("Enter number of elements you want your first set to have : "))


query1 = input("If you want to input integers press1\n"
               "If you want to input words press 2")

if query1 == "1":
# iterating till the range
    for i in range(0, m1):
        ele = int(input())

        list1.append(ele)  # adding the element

        print(list1)
        n1 = len(list1)
elif query1 == "2":
    for i in range(0, m1):
        ele = str(input())

        list1.append(ele)  # adding the element

        print(list1)
        n1 = len(list1)
else:
    print("Wrong input, try again!")


m2 = int(input("enter the number of elements you want your second set to have!"))
query2 = input("If you want to input integers press1\n"
               "If you want to input words press 2")

if query2 == "1":

    for j in range(0, m2):
        ele2 = int(input())

        list2.append(ele2)

        print(list2)
        # arr2 = set(list2)
        n2 = len(list2)

elif query2 == "2":
    for j in range(0, m2):
        ele2 = str(input())

        list2.append(ele2)

        print(list2)
        # arr2 = set(list2)
        n2 = len(list2)

else:
    print("Wrong input, try again!")


find_cart(list1, list2, n1, n2)