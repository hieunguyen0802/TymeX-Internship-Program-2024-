# 2.1
with open("inventory.txt") as file:
    items = []
    dict = {}
    for line in file:
        if line:
            data = line.strip().replace(" ","").split(':')
            category = data[0]
            info = data[1]
        
        
        
        #split price and quantity
        price = info.split(",")[0]
        quantity = info.split(",")[1]
        total = float(price[5:]) * int(quantity[8:])
        
        
        
        items.append({"category": category,
                    "price": float(price[5:]),
                    "quantity": int(quantity[8:])
                })   
        
        dict[category] = total
    
    print(items)
       
    # print total 
    print(f"1. grand total: {sum(dict.values())}")

    # most expensive product
    print(f"2. most expensive product: {(sorted(dict, key= lambda s:s[1]))[0]}")
    
    # check if product is in stock
    print(f"3. if headphones is in stock: {"Headphones" in dict.keys()}")

    # sort by price / quantity
    print("4. sort by price:")
    print(sorted(items, key=lambda x: x["price"], reverse=True))

    print("4. sort by quantity:") 
    print(sorted(items, key=lambda x: x["quantity"], reverse=True))

#2.2: comment 2.1 and uncomment 2.2 to run 2.2
# def main(s):
#     for i in range(len(sorted(s))-1):
#         if sorted(s)[i+1] - sorted(s)[i] != 1:
#             return sorted(s)[i]+1



# #2nd solution: sort the array and check if the index and value are the same. If not, return the value at the different index.
# def main2(s):
# 	for index, value in enumerate(sorted(s), start=1):
# 		if index != value: return index



# print(main([3,4,5,1])) 
# print(main2([3,4,5,1])) 
