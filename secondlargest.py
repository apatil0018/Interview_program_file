#write a python program find the second largest number by using array

import array
stu_roll=array.array('i',[101,102,103,104,105])
stu_roll.remove(max(stu_roll))
print(max(stu_roll))
