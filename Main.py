import hashlib

# Read Method---------------------------------------------------------------------------------------------------------------------
def read(): #Method that reads the text file and splits it into columns 
    for line in open("/Users/jovanvizcaino/Downloads/Fall 2019/Data Structures/Lab_Assignments/Lab_1/Lab 1 - Option B/Lab_1/password_file.txt","r"):
        col = line.split(',')# Splits the text file into separate columns based of commas 
        user_Pass = col[0] # puts the user passwords into a column 
        hash_Password = col[1] # puts the hashed passwords into a separate column 
        create(x,y,user_Pass,hash_Password) # calls the create passwords method 

# Given Code----------------------------------------------------------------------------------------------------------------------
def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8')) #creates hashed passwords
    hex_dig = hash_object.hexdigest()
    return hex_dig

# Create Passwords Method--------------------------------------------------------------------------------------------------------
def create(x,y,salt,hash_User): #| x: is my start | y: is my end | Similar to sample code given in class on 09/09/2019 |
    if len(x) == y:
        return x
    for i in range(10): # range for passwords (0000000-9999999)
        passwords = create(x + str(i),y,salt,hash_User) 
        connect = salt + passwords
        hash_Pass = hash_with_sha256(connect)
        if hash_User != hash_Pass: # checks if the user hash matches the hashed passwords and either prints found or not found
            print ("Not Found :( ")
        print ("Found! :) ")
    return create(x + str(i),y,salt,hash_Pass)

x = "" #start point
y = 2 #end point
read()#calls the read file method 