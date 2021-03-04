print("Hello World")
#####################################################
def add_data(user_id,paswd):
    u=user_id.encode("utf-8");p=paswd.encode("utf-8")
    import pickle
    f1=open("user.dat","ab")
    d1={}
    d1[u]=p
    pickle.dump(d1,f1)
    print("The record has been appended successfully!!")
    f1.close()
#####################################################
def read_data():
    import pickle
    print("The Records:")
    print("user_id\tpaswd")
    with open("user.dat","rb") as f:
        while True:
            try:
                r=pickle.load(f)
                print(r)
            except EOFError:
                break
    f.close()
#####################################################
v=True
while v:
    print("\nmain_menu")
    print("1.\tAdd new record")
    print("2.\tRead record")
    c=input("\nEnter Choice")
    if c=='1':
        user_id=input("user: ")
        paswd=input("paswd:")
        add_data(user_id,paswd)
    elif c=='2':
        read_data()
    else:
        v=False
        
        
    
    

    
