#HDCC banking system program

class  Bank(object):
    def __init__(self):
        self.birth='' 
        self.first_name=''
        self.second_name=''
        self.email=''
        self.phone_no=0
        
        self.accountno=0
        self.userid=''
        self.password=''
        self.sex=''
        self.nationality=''
        self.permanent_add=''
        self.residential_add=''
        self.aadhar=0
        self.currentamt=0
    def create(self):
        list1=[]
        with open('trial.txt','r') as user1:
                a=user1.readlines()

        for i in range(len(a)):
            new1=a[i].split(',')
            list1.append(new1)
        try:
            self.birth=int(raw_input("Enter your age:"))
            if self.birth<18:
                print 'You are not eligible for creating an account as the minimum age for creating a bank account is 18. Thank you for your time.'
            else: 
                self.first_name=raw_input('Enter your first name:')
                self.second_name=raw_input('Enter your second name:')
                self.email=raw_input('Enter your email id:')
                for i in range(len(list1)):
                    if self.email in list1[i]: 
                        print 'An account registered through this Email-id already exists. For more information, contact the Customer Services. Thank you for your time.'
                        break  
                    else: 
                        self.phone_no=raw_input('Enter your phone number:')
                        self.accountno= random.randint(1000,2000)                
                        self.user_id=raw_input('Enter your user id:')
                        if self.user_id in list1[i]:
                            print 'An account with this username already exists.'
                            print 'Try some other username.'
                            break 
                             
                        else:
                            self.password=raw_input('Enter password with more than 8 characters and either ! , / or _  :')
                            if len(self.password)>=8 and '!' in self.password or '!' in self.password or '/' in self.password or '_' in self.password:

                                print 'Password accepted'
                                self.sex=raw_input('Enter your Sex ( Female / Male/ Other:)')
                                self.nationality=raw_input('Enter your nationality:')
                                self.permanent_add=raw_input("Enter you permanent address:")
                                self.residential_add=raw_input('Enter your residential address:')
                                self.aadhar=raw_input('Enter your aadhar card number:')
                                self.currentamt=int(raw_input('Enter the amount you would like to deposit in your new account:'))
                                print "\n"
                                print "Welcome,",self.first_name+self.second_name
                                print "Your account number is:",self.accountno
                                print "Your password is:", len(self.password)*'*'
                                
                                full=self.first_name+','+self.second_name+','+self.email+","+self.phone_no+","+str(self.accountno)+","+self.user_id+","+self.password+","+self.sex+","+self.nationality+","+self.permanent_add+","+self.residential_add+","+self.aadhar+','+str(self.currentamt)
                                with open('trial.txt','a') as user1:
                                    user1.writelines(full)
                                    user1.writelines('\n')
                                print 'YOUR ACCOUNT HAS BEEN CREATED.'
                            else:
                                print 'The password you entered could not be accepted. Your password should be more than or equal to 8 characters.'
                                print 'It should contain atleast one special charcter from "!" or "/" or "_". Try again.'
                                break
        except ValueError:
            print 'Only numbers can be accepted. Please enter a correct value.' 
        user1.close()
    def withdraw(self):
        print 'Do you already have an account?'
        acc=raw_input('YES or NO?:')
        if acc=='NO' :
            print ' Would you like to create one?'
            acc2=raw_input('YES or NO?:')
            if acc2=='YES'  :
                user.create()
            else:
                print 'Thank you for using our bank. Visit soon! '        
        else: 
            list1=[] 
            self.accountno=raw_input('Enter your account number:')
            with open('trial.txt','r') as user1:
                a=user1.readlines()
            for i in range(len(a)):
                new1=a[i].split(',')
                list1.append(new1)
            
            for k in range (len(list1)):
                if self.accountno in list1[k]:
                    self.password= raw_input('Enter your password:')
                    if self.password in list1[k]:
                        print 'You are logged into your account.'
                        loan=int(raw_input('Enter the amount you would like to withdraw: Rs'))
                        temp=list1[k][-1]
                        mon=int(temp)
                        fin=mon-loan
                        if mon<loan:
                            print "There aren't enough funds in your account."
                        else:
                            add=str(fin)
                            list1[k][-1]=add 
                            newline='' 
                            for j in list1[k]:
                                newline+=j+','
                            newline=newline.rstrip(',')+'\n'
                            a[i]=newline
                            now = datetime.datetime.now()
                            with open('trial.txt','w') as user1:
                                user1.writelines(a)
                            print '\n'
                            print '---------------------------------------------------------------------------' 
                            print 'Current amount in your account is : Rs',int(temp)
                            print 'After your deposit, the amount in your account is: Rs',add
                            print 'DATE AND TIME OF MONEY DEPOSITION:', datetime.datetime.now(),now.strftime("%A")
                            break 
                    else :
                         print 'The password you entered is incorrect. Try again.'
                if list1[k]==list1[-1]:
                    print ' This account does not exist.'
                    break 
                    
    def deposit(self):
        print 'Do you already have an account?'
        acc=raw_input('YES or NO?:')
        if acc=='NO' :
            print ' Would you like to create one?'
            acc2=raw_input('YES or NO?:')
            if acc2=='NO':
                print 'Thank you for using our bank. Visit soon! '
            elif acc2=='YES' :
                create()
        else:
            list1=[] 
            self.accountno=raw_input('Enter your account number:')
            with open('trial.txt','r') as user1:
                a=user1.readlines()
            for i in range(len(a)):
                new1=a[i].split(',')
                list1.append(new1)
            
            for k in range (len(list1)):
                if self.accountno in list1[k]:
                    self.password= raw_input('Enter your password:')
                    if self.password in list1[k]:
                        print 'You are logged into your account.'
                        deposit=int(raw_input('Enter the amount you want to deposit to your account:'))
                        current=int(list1[k][12])
                        amt=current+deposit
                        list1[k][-1]=str(amt) 
                        newline=''
                        for j in list1[k]:
                            newline+=j+','
                        newline=newline.rstrip(',')+'\n'
                        print newline 
                        a[i]=newline
                        with open('trial.txt','w') as user1:
                            user1.writelines(a[i])
                        now=datetime.datetime.now()
                        print '---------------------------------------------------------------------------' 
                        print 'Current amount in your account is : Rs',int(current)
                        print 'After your deposit, the amount in your account is: Rs',amt
                        print 'DATE AND TIME OF MONEY DEPOSITION:', datetime.datetime.now(),now.strftime("%A")
                        break 
                    else:
                        print 'Incorrect password. Try again later.'
                        break 
                if list1[k]==list1[-1]:
                    print 'This account does not exist.'
                    break 
    def check(self):
        print 'Do you already have an account?'
        acc=raw_input('YES or NO?:')
        if acc=='NO' :
            print ' Would you like to create one?'
            acc2=raw_input('YES or NO?:')
            if acc2=='YES' :
                user.create()
            else:
                print 'Thank you for using our bank. Visit soon! '
        else:
            list1=[] 
            self.accountno=raw_input('Enter your account number:')
            with open('trial.txt','r') as user1:
                a=user1.readlines()
            for i in range(len(a)):
                new1=a[i].split(',')
                list1.append(new1)
            
            for k in range (len(list1)):
                if self.accountno in list1[k]:
                    self.password= raw_input('Enter your password:')
                    if self.password in list1[k]:
                        print 'You are logged into your account.'
                        print 'Would you like to see your details?'
                        details=raw_input('YES or NO? : ' )
                        if details == 'YES' or 'yes' :
                            print '''
                            '''
                            print '\t' ,  'Your account details are:'
                            print '------------------------------------------' 
                            print '\n' 
                            print '\t' ,  'NAME:',list1[k][0],list1[k][1]
                            print '\t' ,  'EMAIL:',list1[k][2]
                            print '\t' ,  'PHONE:',list1[k][3]
                            print '\t' ,  'ACCOUNT NUMBER:',list1[k][4]
                            print '\t' ,  'USERNAME:',list1[k][5]
                            print '\t' ,  'PASSWORD:', list1[k][6]
                            print '\t' ,  'SEX:',list1[k][7]
                            print '\t' ,  'NATIONALITY:',list1[k][8]
                            print '\t' ,  'PERMANENT ADDRESS:',list1[k][9]
                            print '\t' ,  'RESIDENTIAL ADDRESS:',list1[k][10]
                            print '\t' ,  'AADHAR CARD NUMBER:', list1[k][11]
                            print '\t' ,  'CURRENT AMOUNT:',list1[k][12]
                            break
                        else:
                            print 'Thank you for using HDCC bank. See you soon!'
                            break 
                                    
                    else:
                        print 'Incorrect password. Try again later.'
                        break
                if list1[k]==list1[-1]:
                    print 'This account does not exist.'
                     
            user1.close() 
                        
    def utility_payment(self):
        print 'Do you already have an account?'
        acc=raw_input('YES or NO?:')
        if acc=='NO' :
            print ' Would you like to create one?'
            acc2=raw_input('YES or NO?:')
            if acc2=='YES' :
                user.create()
            else:
                print 'Thank you for using our bank. Visit soon! '
        else:
            list1=[] 
            self.accountno=raw_input('Enter your account number:')
            with open('trial.txt','r') as user1:
                a=user1.readlines()
            for i in range(len(a)):
                new1=a[i].split(',')
                list1.append(new1)
            for k in range (len(list1)):
                if self.accountno in list1[k]:
                    self.password= raw_input('Enter your password:')
                    if self.password in list1[k]:
                        print 'You are logged into your account.'
                        print '''
                        1) Gas company
                        2) Electricity supply
                        3) Water supply (Jal Board)  '''
                        utility=raw_input('Enter the company you want to pay to :')
                        temp=list1[k][12]
                        if utility=='1':
                            another='98623'
                            print '''

                            '''
                            transfer=int(raw_input('Enter the amount you have to transfer:'))
                            if transfer>=int(temp):
                                print 'Your account does not have so many funds.'
                                break 
                            else:
                                fin=int(temp)-transfer-22 
                                thn=str(fin)
                                list1[k][12]=thn
                                newline=''
                                for j in list1[k]:
                                    newline+=j+','
                                newline=newline.rstrip(',')+'\n' 
                                a[i]=newline
                                with open('trial.txt','w') as user1:
                                    user1.writelines(a)
                                now = datetime.datetime.now()
                                print '\t', 'Current chrges: Rs',transfer
                                print '\t','GST: Rs','22'
                                print '\t','Total amount to be transferred: Rs',transfer+ 22
                                print '\t','Date and time of money transfer:', datetime.datetime.now(),now.strftime("%A")
                                print '\t','THE TRANSFER WAS SUCCESSFUL. YOU TRANSFERRED RS',transfer+22 ,'TO THE GAS COMPANY,ACCOUNT NUMBER',another,'.' 
                                print '\t','The amount left in your account left is Rs', fin
                                break 
                        elif utility=='2':
                            another='89372'
                            print '''

                            '''
                            transfer=int(raw_input('Enter the amount you have to transfer to the Electricity supplier\'s account:'))
                            if transfer>=int(temp):
                                print 'Your account does not have so many funds.'
                                break
                            else:
                                fin=int(temp)-transfer-18 
                                thn=str(fin)
                                list1[k][12]=thn
                                newline=''
                                for j in list1[k]:
                                    newline+=j+','
                                newline=newline.rstrip(',')+'\n' 
                                a[i]=newline
                                with open('trial.txt','w') as user1:
                                    user1.writelines(a)
                                now= datetime.datetime.now()
                                print '\t','Current chrges: Rs',transfer
                                print '\t','GST: Rs','18'
                                print '\t','Total amount to be transferred: Rs',transfer+ 18
                                print '\t','Date and time of money transfer:', datetime.datetime.now(),now.strftime("%A")
                                print '\t','THE TRANSFER WAS SUCCESSFUL. YOU TRANSFERRED RS',transfer+18 ,'TO THE ELECTRICTY SUPPLIER,ACCOUNT NUMBER',another,'.' 
                                print '\t','The amount left in your account left is Rs', fin
                                break
                        elif utility=='3':
                            another='28113'
                            print '''

                            '''
                            transfer=int(raw_input('Enter the amount you have to transfer to the Jal Board account:'))
                            if transfer>=int(temp):
                                print 'Your account does not have so many funds.'
                                break
                            else:
                                fin=int(temp)-transfer-36 
                                thn=str(fin)
                                list1[k][12]=thn
                                newline=''
                                for j in list1[k]:
                                    newline+=j+','
                                newline=newline.rstrip(',')+'\n' 
                                a[i]=newline
                                with open('trial.txt','w') as user1:
                                    user1.writelines(a)
                                now= datetime.datetime.now()
                                print '\t','Current chrges: Rs',transfer
                                print '\t','GST: Rs','36'
                                print '\t','Total amount to be transferred: Rs',transfer+ 36
                                print '\t','Date and time of money transfer:', datetime.datetime.now(),now.strftime("%A")
                                print '\t','THE TRANSFER WAS SUCCESSFUL. YOU TRANSFERRED RS',transfer+36 ,'TO THE WATER SUPPLY COMPANY,ACCOUNT NUMBER',another,'.' 
                                print '\t','The amount left in your account left is Rs', fin
                                break 
                        else:
                            print 'Incorrect choice. Choose only from sub menu 1 to 3.'
                            break 
                    else:
                        print 'Incorrect password.'
                        break 
                if list1[k]==list1[-1]:
                        print 'This account does not exist.'
                        break

            user1.close() 
    def payment(self):
        print 'Do you already have an account?'
        acc=raw_input('YES or NO?:')
        if acc=='NO':
            print ' Would you like to create one?'
            acc2=raw_input('YES or NO?:')
            if acc2=='YES':
                user.create()
            else:
                print 'Thank you for using our bank. Visit soon! '
        else:
            list=[]
            self.accountno=raw_input('Enter your account number:')
            with open('trial.txt','r') as user1:
                a=user1.readlines()
                           
            for i in range(len(a)) :
                new=a[i].split(',')
                list.append(new)
            for k in range (len(list)):
                if self.accountno in list[k]:
                    self.password= raw_input('Enter your password:')
                    if self.password in list[k]:
                        print 'You are logged into your account.'
                        account=raw_input('Enter the account number you have to pay to:')                     
                        pay=int(raw_input('Enter payment :'))
                        temp=list[k][12]
                        final=temp
                        fin=int(temp)
                        if fin<pay:
                            print 'The amount you entered could not be payed. Not enough funds in your account.'
                            break
                        else: 
                            thn=fin-pay
                            new_amt=str(thn)
                            list[k][12]=new_amt 
                            newline=''
                            for j in list[k]:
                                newline+=j+','
                            newline=newline.rstrip(',')+'\n' 
                            a[i]=newline
                            with open('trial.txt','w') as user1:
                                user1.writelines(a)
                            now= datetime.datetime.now()
                            print '\t','Current amount in your account : Rs',fin  
                            print '\t','Your payment of Rs',pay, ' was successful.'
                            print '\t', 'Date and time of money payment:', datetime.datetime.now(),now.strftime("%A")
                            print '\t','The amount in your account after payment to account number','',account,'is: Rs',new_amt
                            break
                    else:
                        print 'Incorrect password. Try again.' 
                        break                                         
                if list[k]==list[-1]:
                    print 'This account does not exist.'
                    break 

    def exit(self):
        print '''~~~~~~~~~~~~THANK YOU FOR USING HDCC BANKING SYSTEM. HOPE YOU HAD A PLEASANT VISIT.~~~~~~~~~~~
                 ~~~~~~~~~~~~~VISIT SOON!~~~~~~~~~~~~ '''
        sys.exit()
    def __str__(self):
        a='WELCOME'+','+self.first_name+'\t'+self.second_name
        return a 
        
        

while True :
    import sys
    import pickle,random,datetime
    print '                                             ','---------------------------------------'
    print '                                             ','---------------------------------------' 
    print '                                                ', "Welcome, dear user to HDCC bank.", "\n"  

    print '''To carry out an operation, select any one menu,
    1) Create an account
    2) Cash Withdrawal 
    3) Deposit Funds
    4) Check your account
    5) Utility Payment
    6) Payment 
    7) Exit ''', '\n'
    user=Bank()          
    try:
        
        choice= int(raw_input('Enter your choice number:'))
        if choice==1:
            user.create()
            fml=open('binary.det','ab+')
            pickle.dump(user,fml)
            fml.close()
        elif choice==2:
            user.withdraw()
        elif choice==3:
            user.deposit()
        elif choice==4:
            user.check()
        elif choice==5:
            user.utility_payment()
        elif choice==6:
            user.payment()
        elif choice==7:
            user.exit()
        else:
            print 'Incorrect choice, choose only from menu options 1 to 7.'
    except ValueError:
        print 'Only numbers can be accepted. Try again.' 
                
                
            



     
