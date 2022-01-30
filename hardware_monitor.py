import psutil
from sys import argv
import datetime
import sys

try:
    src, data = sys.argv
except ValueError:
    print("Please, enter an argument after script")
    exit()

def memory(time):
    print("MEM")
    arr_1 = ("memory total", "memory available", "memory used", "memory free")
    arr_2 = ("swap total", "swap used", "swap free")
    value_1 = psutil.virtual_memory()
    print(arr_1[0] + ": " + str(round(value_1[0] * 10 ** -6, 2)) + "MB")
    print(arr_1[1] + ": " + str(round(value_1[1] * 10 ** -6, 2)) + "MB")
    print(arr_1[2] + ": " + str(round(value_1[3] * 10 ** -6, 2)) + "MB")
    print(arr_1[3] + ": " + str(round(value_1[4] * 10 ** -6, 2)) + "MB")
    value_2 = psutil.swap_memory()
    print(arr_2[0] + ": " + str(round(value_2[0] * 10 ** -6, 2)) + "MB")
    print(arr_2[1] + ": " + str(round(value_2[1] * 10 ** -6, 2)) + "MB")
    print(arr_2[2] + ": " + str(round(value_2[2] * 10 ** -6, 2)) + "MB")

def cpu(time):
    print("CPU")
    arr_3 = ("system", "user", "guest", "idle", "iowait")
    value_3 = psutil.cpu_times(percpu=False)
    print(arr_3[0] + ": " + str(value_3[2]) + "%")
    print(arr_3[1] + ": " + str(value_3[0]) + "%")
    print(arr_3[2] + ": " + str(value_3[8]) + "%")
    print(arr_3[3] + ": " + str(round(100 - psutil.cpu_times().user - psutil.cpu_times().nice, 2)) + "%")
    print(arr_3[4] + ": " + str(value_3[4]))


if data == "mem":
    memory(3)
elif data == "cpu":
    cpu(3)
else:
    print("You should enter mem or cpu")
    exit()
