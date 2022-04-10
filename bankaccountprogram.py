#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Account:
    
    def __init__(self,owner,balance):
        
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        
        return f" Account owner: {self.owner} \n Account balance: ${self.balance}"
            
    
        
    def deposit(self,deposit):
        
        self.balance = self.balance + deposit
        print("Deposit Accepted, we just added ${} to your balance".format(deposit))
    
    def withdraw(self,withdraw):
        
        self.balance = self.balance - withdraw
        if withdraw > self.balance:
            print("Funds Unavailable. The withdrawal amount exceeds your account balance")
        else:
            print("Withdrawal Accepted, we subtracted ${} from your account".format(withdraw))


# In[2]:


# 1. Instantiate the class
acct1 = Account('Jose',100)


# In[3]:


# 2. Print the object
print(acct1)


# In[4]:


# 3. Show the account owner attribute
acct1.owner


# In[5]:


# 4. Show the account balance attribute
acct1.balance


# In[6]:


# 5. Make a series of deposits and withdrawals
acct1.deposit(50)


# In[7]:


acct1.withdraw(75)


# In[8]:


# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)


# In[ ]:




