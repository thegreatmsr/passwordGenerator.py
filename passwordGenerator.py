from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open ("key.key", "wb") as key_file:
        key_file.write(key)
write_key()'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key



master_Pwd= input("what is the master password?")
key = load_key() +master_Pwd.bytes
fer = Fernet(key)






def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            print(line)

    
def add():
    name=input("Account Name:")
    pwd =input("Password:")
    
    with open('passwords.txt', 'a') as f:
        f.write(name + " " +pwd +"\n")
        
    
    

while True:
    mode= input("Would you like to add a new password or view existing ones (View, Add)")
    
    if mode =="View":
        view()
    elif mode == "Add":
        add()
    else:
        print("Invalid Option")
        continue
    