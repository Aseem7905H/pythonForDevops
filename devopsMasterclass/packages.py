import os 
import shutil
print(os.getcwd())

print(shutil.disk_usage("/"))

total ,used ,free = shutil.disk_usage("/")
print("total space of disk : ",total // 2**30)
print("used space is : ",used // 2**30)
print("free space is : ",free// 2**30)

print("BELOW WE USE f FORMATED STRING")

print(f"total space of disk : {total // 2**30}")
print(f"used space is : {used // 2**30 } ")
print(f"free space is : {free// 2**30} ")

