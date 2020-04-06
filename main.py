##https://pypi.org/project/psutil/
import psutil
import datetime
import collections
import time


print("--------------  PC_Health  --------------")
#score ratio:
#battery = 10
#active cores = 30
#cpu utilization = 20
#cpu frequency = 20
#load on cpu = 10
#temprrature = 10
score =0
print()
#this fuction will return a list
number_of_users = psutil.users()
print("User Details = ")

print(number_of_users)
# print(type(number_of_users))
time.sleep(1.9)
print()




#this function will return the number of CPU cores
number_of_cpu_count = psutil.cpu_count()
print("Number of Cores of CPU = ", end="")
print(psutil.cpu_count())
time.sleep(2)

#Note that this number is not equivalent to the number of CPUs the current process can actually use.
# That can vary in case process CPU affinity has been changed, 
# Linux cgroups are being used or on Windows systems using processor groups or having more than 64 CPUs. 
# The number of usable CPUs can be obtained with:
number_of_useable_cpu_count = len(psutil.Process().cpu_affinity())
print("Number of active Cores of CPU = ", end="")
print(len(psutil.Process().cpu_affinity()))


if (number_of_cpu_count - number_of_useable_cpu_count) == 0:
    score += 25
if (number_of_cpu_count - number_of_useable_cpu_count) <= 2:
    score += 20

if (number_of_cpu_count - number_of_useable_cpu_count) > 2:
    score +=5
print()

#Return a float representing the current system-wide CPU utilization as a percentag
current_cpu_usage = psutil.cpu_percent(interval=1)
print("Current system-wide CPU utilization = ", end="")
print(psutil.cpu_percent(interval=1))

if (current_cpu_usage > 5):
    score += 5
if ((current_cpu_usage < 5) and (current_cpu_usage > 2)):
    score += 10
if (current_cpu_usage < 2):
    score += 20
time.sleep(2)
print() 


#Return CPU frequency as a nameduple including current, min and max frequencies expressed in Mhz.
# On Linux current frequency reports the real-time value, on all other platforms it represents the nominal “fixed” value

cpu_freq =str(psutil.cpu_freq())
# print(type(cpu_freq))
# print(cpu_freq)

# cpu_freq_current =
# cpu_freq_min =
# cpu_freq_max =




# 1) For Current Frequency
cpu_freq_current = ""
cpu_freq_current_d = 0
currentLoc = cpu_freq.find("current") + 8 
for i in range(currentLoc, len(cpu_freq)):
    if (cpu_freq[i].isnumeric() or cpu_freq[i] == '.'):
        if (cpu_freq[i] == '.' or cpu_freq_current_d > 0):
            cpu_freq_current_d +=1
        cpu_freq_current += cpu_freq[i]
        if (cpu_freq_current_d == 4):
            break
print("Current CPU frequency of the System = ", end="")
print(cpu_freq_current)
cpu_freq_current = float(cpu_freq_current)
time.sleep(2)


# 2) For Min Frequency
cpu_freq_min = ""
cpu_freq_min_d = 0
minLoc = cpu_freq.find("min") + 4 
for i in range(minLoc, len(cpu_freq)):
    if (cpu_freq[i].isnumeric() or cpu_freq[i] == '.'):
        if (cpu_freq[i] == '.' or cpu_freq_min_d > 0):
            cpu_freq_min_d +=1
        cpu_freq_min += cpu_freq[i]
        if (cpu_freq_min_d == 4):
            break
print("Minimum CPU frequency of the System = ", end="")
print(cpu_freq_min)
time.sleep(2)

# 3) For Max Frequency
cpu_freq_max = ""
cpu_freq_max_d = 0
maxLoc = cpu_freq.find("max") + 4 
for i in range(maxLoc, len(cpu_freq)):
    if (cpu_freq[i].isnumeric() or cpu_freq[i] == '.'):
        if (cpu_freq[i] == '.' or cpu_freq_max_d > 0):
            cpu_freq_max_d +=1
        cpu_freq_max += cpu_freq[i]
        if (cpu_freq_max_d == 4):
            break
print("Minimum CPU frequency of the System = ", end="")
print(cpu_freq_max)
time.sleep(2)
print()
if (cpu_freq_current < 1000):
    score += 20
if ((cpu_freq_current > 1000) and (cpu_freq_current < 2000)):
    score += 10
else:
    score += 5




#Return the average system load over the last 1, 5 and 15 minutes as a tuple.
# The load represents the processes which are in a runnable state, either using the CPU or waiting to use the CPU

#print(psutil.getloadavg())
#print([x / psutil.cpu_count() * 100 for x in psutil.getloadavg()])
load_on_cpu_tuple = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]

load_on_cpu = sum(load_on_cpu_tuple) / len(load_on_cpu_tuple)
print("Average system load over last 15 minutes = ", end="")
print(load_on_cpu)
time.sleep(2)
print()

#Return statistics about system memory usage as a named tuple including the following fields, expressed in bytes
mem = psutil.virtual_memory()
#print(mem)
mem = tuple(mem)
memory_used_percent = mem[2]
print("Total memory of the system = ", mem[0])
time.sleep(2)
print("Available memory of the system = ", mem[1])
time.sleep(2)
print("Percentage of the memory used = ", end="")
print(memory_used_percent)
time.sleep(2)
print()

time.sleep(1.5)
print("Calculating the Temperature of CPU...")
# temperature
time.sleep(2.5)
temp = psutil.sensors_temperatures()

temp = (tuple(temp['acpitz']))
temp = str(str(temp))
# print(temp)

temp_l = temp.find("current")

temperature_of_cpu = float(temp[(temp_l + 8) : (temp_l + 12)])
print("Current Temperature of the CPU is = ", end="")
print(temperature_of_cpu)
time.sleep(2)
print()

if (temperature_of_cpu > 30):
    score += 10
else:
    score += 20


#battery
time.sleep(1)
battery = psutil.sensors_battery()

mm, ss = divmod(battery.secsleft, 60)
hh, mm = divmod(battery.secsleft, 60)
# print(type(battery.percent))
# print(hh)

if (mm > 30):
    hh += 1

if (battery.percent > 90):
    if (hh >= 4):
        score += 10
    if (hh <= 1):
        score += 2
    else:
        score += 5


if (battery.percent > 55 and battery.percent < 90):
    if (hh >= 3):
        score += 10
    if (hh <= 1):
        score += 2
    else:
        score += 5

    
if (battery.percent > 20 and battery.percent < 55):
    if (hh >= 2):
        score += 10
    if (hh <= 1):
        score += 3
    else:
        score += 5

# print( score)


#boot time
time.sleep(1)
print("System boot time =  ", end="")
print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))
print()
print()


#final Result is computed on the bases of the score we calculated 

print("Computing the values and determining the health of the PC...")
print()
time.sleep(2)
#final result
if (score >= 100):
    print("Your Systems Health is GOOD!!")
if (score < 100 and score > 55):
    print("Your Systems Health is AVERAGE!!")
if (score < 55):
    print("Your Systems Health is BAD!!")
