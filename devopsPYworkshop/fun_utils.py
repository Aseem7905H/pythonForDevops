import os
import datetime

def show_date():
    return datetime.datetime.today()

print(show_date())

print("   ==  cpu  ==   ")
def check_cpu(command):
    print(os.system(command))
#check_cpu("lscpu")

print("  ==  date  ==  ")
def check_date(command):
    print(os.system(command))

check_date("date")
print("  == ram == ")
def check_ram(command):
    return (os.system(command))
check_ram("free -h")    