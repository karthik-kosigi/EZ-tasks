import sqlite3


class login:
    def connsql(self):
        connection = sqlite3.connect('shopping.db')
        cur = connection.cursor()
        return cur
    
    def admin_login(self,username,password):
        self.username=username
        self.password=password
        cur=self.connsql()
        cur.execute("SELECT * FROM ADMINCRED WHERE username=? AND password=?", (self.username, self.password))
        result=cur.fetchone()
        return result
    def user_login(self,username,password):
        self.username=username
        self.password=password
        cur=self.connsql()
        cur.execute("SELECT * FROM USERCRED WHERE username=? AND password=?", (self.username, self.password))
        result=cur.fetchone()
        return result
    def create_user(self,email,username,password):
        self.email=email
        self.username=username
        self.password=password
        cur=self.connsql()
        try:
            cur.execute(f"INSERT INTO USERCRED (username,password,email) VALUES (?,?,?)",(self.email,self.username,self.password))
            cur.connection.commit()
            return True
        except sqlite3.Error as e:
            print("Error:", e)
            return False
        



class Admin:
    def showprivilages(self):
        while True:
            print("1.ADD PRODUCT")
            print("2.Remove products")    
            print("3.View products")
            print("4.View orders")
            print("5.admin logut")
            ch=int(input("Enter your choice: "))
            if ch==1:
                self.add_product()
            elif ch==2:
                self.remove_product()
            elif ch==3:
                self.view_products()
            elif ch==4:
                self.view_orders()
            elif ch==5:
                break
            else:
                print("invalid choice..")
            
            

    def add_product(self):
        product_id=int(input("Enter product id :"))
        pass

    def remove_product(self, product_id):
        # Logic to remove a product from the system based on its ID
        pass

    def view_orders(self):
        # Logic to view the order history or details of all orders
        pass

    def view_products(self):
        # Logic to view details of all registered users
        pass

    def __str__(self):
        return f"Admin: {self.username}"
ad=Admin()

while True:
    print("1.admin login")
    print("2.user login")
    print("3.create user")
    ch=int(input("Choose an option:"))
    if ch==1:
        username=input("Enter username: ")
        password=input("Enter password: ")
        l=login()
        if l.admin_login(username,password):
            print("Success")
            ad.showprivilages()
        else:
            print("Incorrect username or password...")
    elif ch==2:
        username=input("Enter username: ")
        password=input("Enter password: ")
        l=login()
        if l.user_login(username,password):
            print("Success")

        else:
            print("Incorrect username or password...")
    elif ch==3:
        username=input("Enter username: ")
        password=input("Enter password: ")
        email=input("Enter email: ")
        l=login()
        if l.create_user(username,password,email):
            print("USer created...")
        else:
            print("TRY again..")