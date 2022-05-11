import random


class Product:
    
    def __init__(self,name,price,category):
        self.name = name 
        self.price = price
        self.category= category
        self.id = f"{self.name} Id: "   
    def identify(self):
        self.id = f"{self.name} Id: "   
        for k in range(1,21,1):
            self.id += str(random.randrange(0,10))
        return self.id

    def update_price(self,percent_change,is_increased):
        if is_increased == True:
            updatePricetrue
            updatePricetrue = self.price
            updatePricetrue *= percent_change
            self.price += updatePricetrue
            return self
        if is_increased == False:
            updatePricefalse
            updatePricefalse = self.price
            updatePricefalse *= percent_change
            self.price -= updatePricefalse
            return self
    
    def print_info(self):
        print(self.name, self.category,self.price)
        return self


apple = Product("Apple", 3.00,"Fruits")
banana = Product("Banana", 3.00, "Fruits")
grapes= Product("Grape", 5.00, "Fruits")
milk =Product("Milk",5.00,"Dairy")
steak =Product("Steak",30.00,"Meats")
chicken =Product("Chicken",9.00,"Meats")

print(apple.identify())
print(apple.id)
steak.identify()
print(steak.id)
print(apple.id)