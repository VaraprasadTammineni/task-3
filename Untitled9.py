#!/usr/bin/env python
# coding: utf-8

# In[11]:


class chinna:
     name='varaprasad'
     age='21'
     def show(self):
            print('name:-',self.name)
            print('age:-',self.age)
            
object=chinna()
object.show()

        
        


# In[19]:


class chinna:
     
     def _init_(self,a='chinna',b=32):
            self.name=a
            self.age=b
     def show(self):
            print('name:-',self.name)
            print('age:-',self.age)
            
object=chinna("karan",21)
object.show()


# In[ ]:


class car:
    def _init_(self,a='40'):
        self.speed=a
    def getspeed(self):
        return self.speed
    def set_speed(self,a):
        self.speed=a
object=car()
print(object.getspeed)

        
    
        


# In[ ]:




