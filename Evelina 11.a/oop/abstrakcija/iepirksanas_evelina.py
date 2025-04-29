
class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price (self):
        total_price = self.price * self.quantity
        print(f"Product: {self.name}\nPrice: {self.price} $\nQuantity: {self.quantity}\nTotal price: {total_price} $")
        
product1 = Product("Apple",0.2,5)
product1.get_total_price()
print("")
product2 = Product("Milk",1.5,2)
product2.get_total_price()


class ShoppingCart(Product):
    def __init__(self,name):
        super().__init__(name)
    def add_product_to_cart(self):
        print(f"{self.name} was added to the cart.")

    def remove_product_from_cart(self):
        print(f"{self.name} was removed from the cart.")

    def get_total_price():
        super().get_total_price()

#cart = ShoppingCart()
#cart.add_product_to_cart()

class SystemUser:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

    def set_user_info(self):
        print(f"User info:\nUsername: {self.username}\nPassword: {self.password}\nEmail: {self.email}")

    def get_user_info():
        pass

class Customer(SystemUser):
    def __init__ (self,username,password,email,customer_id,purchase_history,membership_status):
        super().__init__(username,password,email)
        self.customer_id = customer_id
        self.purchase_history = purchase_history
        self.membership_status = membership_status

