import product


class Store:
    
    def __init__(self, name):
        self.name = name 
        self.productList = [] 
        self.productPrice=[]
        self.productCategory =[]
    def add_product(self,new_product):
        self.productList.append(new_product.name)
        self.productPrice.append(new_product.price) 
        self.productCategory.append(new_product.category)
        return self
    def sell_product(self,id):
        print(self.productList[id])
        self.productList.pop(id)
        self.productPrice.pop(id)
        self.productCategory.pop(id)
        return self
    def displayPlist(self):
        for i in range(0,len(self.productList),1):
            print(f"{self.productList[i]} in Category: {self.productCategory[i]} is ${self.productPrice[i]}")
        return self
    def whatnumisit(self,productName):
        for i in range(0,len(self.productList),1):
            if productName == self.productList[i]:
                print(self.productList[i])
                print(i)
        return self
    def inflation(self,percent_increase):
        for i in range(0,len(self.productPrice)):
            temp = 0
            temp = self.productPrice[i]
            temp *= percent_increase
            self.productPrice[i] += temp
    def set_clearance(self,category,percent_discount):
        for i in range(0,len(self.productCategory)):
            if self.productCategory[i] == category:
                tempone = 0
                tempone = self.productPrice[i]
                tempone *= percent_discount
                self.productPrice[i] -= tempone



foodies = Store("foodies")

foodies.add_product(product.apple).add_product(product.banana).add_product(product.grapes)
foodies.add_product(product.milk).add_product(product.steak).add_product(product.chicken)

foodies.displayPlist()
foodies.whatnumisit('Apple')
foodies.inflation(.10)
foodies.set_clearance('Fruits',.5)
print(foodies.productPrice)




