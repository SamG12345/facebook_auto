import random
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import getpass
from cryptography.fernet import Fernet

class web:
    def __init__(self) -> None:
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://www.facebook.com")
        self.driver.minimize_window()
        
    def khol(self, email, password, tm):
        
        try:
            email_set = self.driver.find_element('id', "email")
            email_set.send_keys(email)
            password_set = self.driver.find_element('id', "pass")
            password_set.send_keys(password)
            self.driver.find_element('name', "login").click()
            
            try:

                error = self.driver.find_element('class name', "_9ay7")
                if error.text == "The email or mobile number you entered isn’t connected to an account. Find your account and log in.":
                    return False
                
            except:
                print(e)
        except Exception as e:
            print(e)
        self.driver.maximize_window()
        time.sleep(tm)
    def change_pass(self, genretaed_pass, old_pswd):
        try:
            self.driver.minimize_window()
            self.driver.get("https://accountscenter.facebook.com/password_and_security/password/change")
            profile = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div[4]/div/div/div[2]/div/div")
            self.driver.implicitly_wait(3)
            try:
                profile.click()
                old_pass = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[3]/div[2]/div[4]/div/div/div[3]/div/div/input")
                old_pass.send_keys(old_pswd)
                new_pass = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[3]/div[2]/div[4]/div/div/div[4]/div/div/input")
                new_pass.send_keys(genretaed_pass)
                new_pass1 = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[3]/div[2]/div[4]/div/div/div[5]/div/div/input")
                new_pass1.send_keys(genretaed_pass)
            except Exception as e:
                print(e)

            self.driver.maximize_window()
        
        
        except Exception as e:
            print(e)
        
        time.sleep(1000)
    def close(self):
        self.driver.close()
    def back(self):
        self.driver.get("https://www.facebook.com")
        self.driver.maximize_window()
        time.sleep(100)
    

class hashing:
    def __init__(self, key = Fernet.generate_key(), email=None, password=None) -> None:
        self.key = key
        self.cipher_suite = Fernet(self.key)
        self.email = email
        self.password = password
    def encrypt(self, plaintext):
        ciphertext = self.cipher_suite.encrypt(plaintext.encode())
        return ciphertext
    def decrypt(self, ciphertext):
        try:
            plaintext = self.cipher_suite.decrypt(ciphertext).decode()
            return plaintext
        except Exception as e:
            print("Decryption error:", e)
            return None
    def write(self, email, pswd):
        try:
            place = "c:/info/info.txt"
            with open(place, 'wb') as file:

                file.write("Please donot make any changes to the file\n".encode())
                hashed_id = self.encrypt(email)
                hashed_pass = self.encrypt(pswd)
                
                file.write("key = ".encode())
                file.write(self.key)
                
                file.write("\ncipher = ".encode())
                file.write(hashed_pass)
                
                file.write("\nid = ".encode())
                file.write(hashed_id)
                os.chmod(place, 0o600)
                print("Credentials saved")

                file.close()
        except Exception as e:
            print("Error saving the file",e)
            pass
    
    def get_cred(self):
        return self.decrypt(self.email), self.decrypt(self.password)


def stored():

        with open('c:/info/info.txt', 'r') as file:
            key = None
            cipher_suite = None
            email = None
            password = None
            try:
                for i in f:
                    if "=" in i:
                        indx = i.index("=")
                        if i[:indx].strip() == "key":
                            key = i[indx+1:]
                        elif i[:indx].strip() == "cipher_suite":
                            cipher_suite = i[indx+1:]
                        elif i[:indx].strip() == "cipher":
                            password = i[indx+1:]
                        elif i[:indx].strip() == "id":
                            email = i[indx+1:]
            except:
                pass
            h = hashing(key, email, password)
            return h.get_cred()
def user_input():
    email = input("Enter email : ").strip()
    password = getpass.getpass("Enter pass: ").strip()
    return email, password
def create(i):
    b = random.randint(33,126)    
    if i == 16:
        return str(random.randint(1,9))
    else:
        return chr(b) + create(i+1)

def mk_d():
    try:
        os.mkdir('c:/info')
    except:
        pass

if __name__ == "__main__":
    print("\n\nWelcome to Facebook_auto_Login\n\n")
    
    mk_d()
    while True:
        print("1. Login\t\t2. Auto login\n3. generate_pass\t4. Change_password")
        start = int(input("Enter : "))

        browser = web()
        if start == 1:
            email, password = user_input()
            
            choice = input("\n if you want to save the credentials enter y or press any other to not : ")
            if choice == 'y':
                run = hashing()
                run.write(email, password)
            else:
                continue
            while not browser.khol(email, password, 1000):
                print("\n!!!!Incorrect credents!!!!")
                email, password = user_input()
                run.write(email, password)
            
        elif start == 2:
            try:
                place = "c:/info"
                f = open(place+"/info.txt", 'r')
                email, password = stored()
                while not browser.khol(email, password, 1000):
                    print("\n!!!!Incorrect credents!!!!")
                    email, password = user_input()
            except:
                print("\nNo strored credentials found!!!!")
                choice = input("\n if you want to save the credentials enter y or press any other to not : ")
                if choice == 'y':
                    email, password = user_input()
                    browser.khol(email, password)
                    run = hashing()
                    run.write(email, password)
                else:
                    while not browser.khol(email, password):
                        print("\n!!!!Incorrect credents!!!!")
                        email, password = user_input()
                    
            browser.close()
        elif start == 3:
            new_pswrd = create(0)
            time.sleep(3)
            if (new_pswrd != ""):
                print(f"Password created : {new_pswrd}")

                confirm = input("If you want to implement the password change enter y : ")
                
                if confirm == 'y':
                    try:
                        place = "c:/info"
                        f = open(place+"/info.txt", 'r')
                        email, password = stored()
                        while not browser.khol(email, password, 100):
                            print("\n!!!!Incorrect credents!!!!")
                            email, password = user_input()
                            browser.change_pass(password, new_pswrd)
                    except:
                        print("\nNo strored credentials found!!!!")
                        choice = input("\n if you want to save the credentials enter y or press any other to not : ")
                        if choice == 'y':
                            email, password = user_input()
                            browser.khol(email, password, 7)
                            
                        else:
                            while not browser.khol(email, password, 7):
                                print("\n!!!!Incorrect credents!!!!")
                                email, password = user_input()
                        browser.change_pass(password, new_pswrd)
                    run = hashing()
                    run.write(email, new_pswrd)
                
            browser.close()
        elif start == 4:
            change = input("Change password options \n1. create password automatically and change password\n2. manually change password\nenter : ")
            
            if change == 1:
                print("change :", change)
                new_pswrd = create(0)
                print(f"Password created : {new_pswrd}")
                if (new_pswrd != ""):
                    

                    confirm = input("If you want to implement the password change enter y : ")
                    pass
                    if confirm == 'y':
                        try:
                            place = "c:/info"
                            f = open(place+"/info.txt", 'r')
                            email, password = stored()
                            while not browser.khol(email, password, 7):
                                print("\n!!!!Incorrect credents!!!!")
                                email, password = user_input()
                                browser.change_pass(password, new_pswrd)
                                run = hashing()
                                run.write(email, new_pswrd)
                        except:
                            print("\nNo strored credentials found!!!!")
                            choice = input("\n if you want to save the credentials enter y or press any other to not : ")
                            if choice == 'y':
                                email, password = user_input()
                                browser.khol(email, password, 7)
                                run = hashing()
                            else:
                                while not browser.khol(email, password, 7):
                                    print("\n!!!!Incorrect credents!!!!")
                                    email, password = user_input()
                                    run.write(email, password)
                                browser.change_pass(password, new_pswrd)
                browser.back()
                
            elif change == 2:
                
                def wen():
                    email = input("Enter Email : ")
                    new_pswrd = getpass.getpass("Enter new password : ")
                    re = getpass.getpass("Re-Enter password : ")
                    
                    if(new_pswrd == "" or re == "" or email==""):
                        return False
                    if (new_pswrd != re):
                        return False
                    return email, new_pswrd
                
                email, new_pswrd = wen()
                while not new_pswrd:
                    wen()
                    if new_pswrd != False:
                        break

                print(f"Password created.")

                run = hashing()
                run.write(email, new_pswrd)
            
                while not browser.khol(email, new_pswrd, 1000):
                    print("\n!!!!Incorrect credents!!!!")
                    email, password = user_input()
                    run.write(email, password)
                    
                browser.close()

            
        
        