# zwf's demo file
import datetime
from multiprocessing import Pool
import os, time, random



# class A():
#        def __init__(self):
#               pass
#        def ha(self,line):
#               print('hahaa ',line)

#        def he(self):
#               print('dadaParent process %s.' % os.getpid())
#               p = Pool(4)
#               for i in range(5):
#                      p.apply_async(self.ha, args=(i,))
#               print('Waiting for all subprocesses done...')
#               p.close()
#               p.join()
#               print('All subprocesses done.')

# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__=='__main__':
#        a = A()
#        a.he()
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     a = A()
#     for i in range(5):
#         p.apply_async(a.ha, args=('sb',))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#        LAST_NAME, AGE, SEX, INCOME) \
#        VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
#        ('Mac', 'Mohan', 20, 'M', 2000)

# str1 = "%s"%(12544)
# # print(str1)

# a = datetime.date.today()
# b= datetime.date.today()
# print(0==False)


# a = [0,2,3,4,5]
# print(a.index(3))