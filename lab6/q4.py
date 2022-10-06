str_line = input()

int_arr = list(map(lambda x : int(x), str_line.split()))

try :
    print(int_arr[0]/int_arr[1])
except ZeroDivisionError:
    print("division by zero")

