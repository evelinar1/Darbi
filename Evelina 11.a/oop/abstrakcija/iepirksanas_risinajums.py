class Product(): # A Uzd
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    # B Uzd
    def get_total_price (self):
        total_price = self.price * self.quantity
        return total_price
#C Uzd
siers = Product("Holandes",4,3)
print("Produkts 1:", siers.get_total_price())
maize = Product("Ķelmēnu",2,2)
print("Produkts 2:", maize.get_total_price())

# 2.Uzd - Iepirkumu grozs
class ShoppingCart(): # D Uzd
    def add_product_to_cart(self, product): # E Uzd
        print("Produkts: ",product.name, "pievienots grozam.")

    def remove_product_from_cart(self,product):
        print("Produkts: ",product.name, "noņemts no groza.")

    def get_total_price(self,product):
        print("Kopējā summa:", product.get_total_price())

# F Uzd - objekts ShoppingCart klasei
iepirkumu_grozs = ShoppingCart()
# G Uzd - izsaukt metodes
iepirkumu_grozs.add_product_to_cart(siers)
iepirkumu_grozs.get_total_price(siers)
iepirkumu_grozs.remove_product_from_cart(siers)

# 3.Uzd
class SystemUser(): # H Uzd
    def __init__(self,username,password,email): # I Uzd
        self.username = username
        self.password = password
        self.email = email

    # J Uzd - nomainīt eksistējošus atribūtus
    def set_user_info(self,new_username,new_password,new_email):
        self.username = new_username
        self.password = new_password
        self.email = new_email
        print("Informācija ir nomainīta!")

    def get_user_info(self):
        print("Informācija par lietotāju---")
        print("Lietotājs: ",self.username)
        print("Parole: ",self.password)
        print("E-pasts: ",self.email)
        
# K Uzd
Liene = SystemUser("Liene","1234567","liene@inbox.lv")
# Nomainīt info un parādīt
Liene.set_user_info("Lienesaule","7654321","lienesaule@inbox.lv")
Liene.get_user_info() # Parāda nomainītos datus

# 4.Uzd
class Customer(SystemUser):# L Uzd
    def __init__ (self,username,password,email,customer_id,purchase_history,membership_status):
        super().__init__(username,password,email)
        # N Uzd - pievieno jaunus atributus
        self.customer_id = customer_id
        self.purchase_history = purchase_history
        self.membership_status = membership_status

    # M Uzd
    def set_user_info(self, new_username, new_password, new_email,new_customer_id,new_purchase_history,new_membership_status):
        # Izsaukt bāzes metodi + 3 jauni atribūti
        super().set_user_info(new_username, new_password, new_email)
        self.customer_id = new_customer_id
        self.purchase_history = new_purchase_history
        self.membership_status = new_membership_status

    def get_user_info(self):
        super().get_user_info()
        print("Lietotāja ID: ",self.customer_id)
        print("Pirkumu vēsture: ",self.purchase_history)
        print("Membership statuss: ",self.membership_status)

# O - klienta objekts ar atjauninātu informāciju
Karlis = Customer("Karlis4","12345","karlis@k.lv",13,"","") # Nav statusa vēstures
# Atjaunināt informāciju
Karlis.set_user_info("Karlis5","1212122","Karlis@k.lv",13,"Āboli","Zelta klients")
Karlis.get_user_info()



    