"""
@title:100以内素数和.py
@author:shuzang
@date:2018-8-13 10:46
@brief:求100以内素数和
"""

sum = 0
for i in range(2, 100):
    for j in range(2, i+1):
        if i % j == 0:
            if j == i:
                sum += i
            else:
                break
print(sum)
