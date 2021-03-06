"""  Shell'den boyle cagirabiliriz : 

import class1
class1.Employee("hakan","50000").displayEmployee()
Employee("hakan","50000").displayEmployee()

yani Class'dan bir instance create etmemiz lazim once.
"""

"""Common base class for all employees"""
class Employee:
   
   empCount = 0    # class variable


   def __init__(self, name, salary):   
	# Class'dan instance create ederken, 2 argument vermek zorundayiz
      self.name = name    # instance variable
      self.salary = salary
      Employee.empCount += 1  # Class variable'a nasil eristigimize dikkat et.
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

# Bir instance'in, sahip olmasini istedigin variable'lari __init__'in
# disinda declare etmene gerek yok, yani __init__ disinda declare etsen 
# hata olmuyor, ama genelde __init__ fonksiyonu icinde tanimlanir
# Local variable'larin, _init__ icinde tanimlandigina dikkat et.

# __init__ icinden, class variable'a soyle de erisebilirdik : empcount+=1

# empCount'u __init_icinde de declare edebilirdik.

# Yani hem class variable'lari hem de instance variable'lari, hem __init__ icinde
# hem de__init__ disinda (su anki empcount'un declare edildigi yerde) declare edebiliriz.
