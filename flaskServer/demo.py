# zwf's demo file
import datetime


sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
       ('Mac', 'Mohan', 20, 'M', 2000)

str1 = "%s"%(12544)
# print(str1)

a = datetime.date.today()
b= datetime.date.today()
print(0==False)


a = [0,2,3,4,5]
print(a.index(3))