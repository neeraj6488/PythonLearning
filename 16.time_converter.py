def time_to_float(time_str):
    hours, minutes = map(int, time_str.split(":"))
    return hours + minutes / 60

def float_to_time(time_float):
    hours = int(time_float)
    minutes = int((time_float - hours) * 60)
    return f"{hours:02}:{minutes:02}"

local_time_str = input("Enter the time in [HH:MM]: ")
local_time = time_to_float(local_time_str)
time_diff = float(input("Enter the time difference: "))
converted_time = (local_time + time_diff) % 24
converted_time_str = float_to_time(converted_time)
print(f"The converted time is {converted_time_str}")