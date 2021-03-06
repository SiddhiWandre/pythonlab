#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class atm:
    user={"Siddhi":[1111,992319372,10000,1994],
          "Karan":[1161,56519241651,15000,2910],
          "Kshitij":[1121,74839022,2000,2000],
          "Kevin":[1131,964611926,8000,2704],
          "Himaja":[1141,2688152871,3000,1127],
          "Urvi":[1151,8824183627,10000,1212]}

                
    def __init__(self,name):
        self.name=name


    def acc_info(self,name):
        print("\n ACCOUNT DETAILS:")
        print('Name:',name)
        info.verification(name)
        print('Account:',self.user[name][0])
        print('Mobile:',self.user[name][1])
        print('Balance:',self.user[name][2])
        
    def verification(self,name):
        count=3
        pin=int(input("Enter pin:"))
        if pin==self.user[name][3]:
            print("Pin matched.")
        else:
            count=count-1
            print("Pin incorrect.")
            if count==0:
                print("CARD BLOCKED!")
            else:
                print(count," attempts left.")
                
            
        
        
    def pin_change(self,name):
        count=3
        pin=int(input("Enter pin:"))
        if pin==self.user[name][3]:
            print("Pin matched.")
            ch=input("Press Y to change pin else, press N.")
            if ch=="Y" or ch=="y":
                pin=int(input("Enter new pin:"))
                pin=self.user[name][3]
            elif ch=="N" or ch=="n":
                print("Process continuing..")
            else:
                print("Wrong key entered.")
        else:
            count=count-1
            print("Pin incorrect.")
            if count==0:
                print("CARD BLOCKED!")
            else:
                print(count," attempts left.")
                    
                
    def balance(self,name):
        info.verification(name)
        print("\nBALANCE INQUIRY : ")
        print("Your account balance is: Rs.",self.user[name][2])

        
    def withdrawal(self,name):
        info.verification(name)
        print("\nWITHDRAWAL: ")
        m=int(input("Enter amount to be withdrawn: "))
        n=self.user[name][2]
        if(m>n):
            print("Insufficient Balance.")
        else:
            n=n-m
            print("Balance remaining: Rs.",n)
        
    def deposit(self,name):
        info.verification(name)
        print("\nDEPOSIT")
        n=user[name][2]
        m=int(input("Enter amount to be deposited: "))
        if (m<100):
            print("Minimum amount must be Rs.100")
        else:
            n=n+m
            print("New Balance: ",n)
       
    
user={"Siddhi":[1111,992319372,10000,1994],"Karan":[1161,56519241651,15000,2910],"Kshitij":[1121,74839022,2000,2000],"Kevin":[1131,964611926,8000,2704],"Himaja":[1141,2688152871,3000,1127],"Urvi":[1151,8824183627,10000,1212]}
while (1):
    name=input('Enter Name: ')
    info=atm(name)
    if name in user.keys():
        print('(1)Account Info.','\n(2)PIN Change.','\n(3)Balance Inquiry.',
              '\n(4)Withdrawal.','\n(5)Deposit.')
        s=int(input('Select Operation(1-5): '))
        if s==1:
            info.acc_info(name)
        elif s==2:
            info.pin_change(name)
        elif s==3:
            info.balance(name)
        elif s==4:
            info.withdrawal(name)
        elif s==5:
            info.deposit(name)
        else:
            print('Invalid Option!')
            continue
        e=input('Enter 0 to exit, press any other key to continue operations: ')
        if e==0:
            print('Thank You!')
            break
        else:
            continue
        break
        
    break


# In[ ]:




