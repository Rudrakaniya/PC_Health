##https://pypi.org/project/psutil/
import psutil

#this fuction will return a list
number_of_users = psutil.users()

print(number_of_users)
print(type(number_of_users))

#this function will return the number of CPU cores
number_of_cpu_count = psutil.cpu_count()
print(psutil.cpu_count())


#Note that this number is not equivalent to the number of CPUs the current process can actually use.
# That can vary in case process CPU affinity has been changed, 
# Linux cgroups are being used or on Windows systems using processor groups or having more than 64 CPUs. 
# The number of usable CPUs can be obtained with:
number_of_useable_cpu_count = len(psutil.Process().cpu_affinity())
print(len(psutil.Process().cpu_affinity()))

#Return a float representing the current system-wide CPU utilization as a percentag
current_cpu_usage = psutil.cpu_percent(interval=1)
print(psutil.cpu_percent(interval=1))






#Return CPU frequency as a nameduple including current, min and max frequencies expressed in Mhz.
# On Linux current frequency reports the real-time value, on all other platforms it represents the nominal “fixed” value

cpu_freq =str(psutil.cpu_freq())
print(type(cpu_freq))
print(cpu_freq)





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

print(cpu_freq_current)




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

print(cpu_freq_min)






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

print(cpu_freq_max)





# cpu_freq_current =
# cpu_freq_min =
# cpu_freq_max = 