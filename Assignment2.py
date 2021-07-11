#Now ask the user to enter 2 of his favourite tv shows. Take that as input and then use the append() function to add those inputs into the list.

list1=["inception","interstellar","stranger things","money heist"]

y=int(input("Enter your no. of favorite shows to be added "))

for i in range(0, y):
    inp =input()
  
    list1.append(inp)
      
print(list1)