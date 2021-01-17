#csv-comma seperated value
#writin the data in csv file-->csv.writer(),to read csv.reader()
"""import csv
with open("sales.csv","w",newline='') as f: # if we dont give newline='' it will created a blank line on csv 
    w=csv.writer(f)  # to write
    w.writerow(["product_name","product_id","product_cost"]) #header
    n=int(input("Enter the no of required products: "))
    for each in range(n):
          product_name=input("Enyer the product name: ")
          product_id=input("Enter the product id: ")
          product_cost=input("enter the product cost: ")
          w.writerow([product_name,product_id,product_cost]) # assined values are inserted in row
print("Required product details are inserted successfilly")

"""
import csv
f=open("sales.csv","r")
w=csv.reader(f)
for a in w:
    for b in a:
        print(b,"\t\t",end='')
    print()
