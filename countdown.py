# import time

# def countdown(t):
#     while t:
#         mins, secs = divmod(t, 60)
#         timeformat = '{:02d}:{:02d}'.format(mins, secs)
#         print(timeformat, end='\r')
#         time.sleep(1)
#         t -= 1
#     print('Goodbye!\n')

# countdown(120)


# import datetime

# end_time = datetime.datetime.combine(
#     datetime.date.today(), 
#     datetime.time(16, 0))

# print(end_time)


# import time
# import datetime

# format = "%H:%M"
# timenow = time.strftime(format)
# print("Current time: {}".format(timenow))
# busleaves = input("What time does your bus leave? ")
# bus = time.strptime(busleaves, format)
# print("Bus leaves: {}".format(bus))
# # timeleft = datetime.datetime(timenow, format)-datetime.datetime(bus, format)  #is this the right way to do the calculation???


from datetime import datetime
time_now = datetime.now().strftime("%H:%M")
print(time_now)
end_time = input("What is the end time? ")
print(end_time)
# delta = end_time - time_now
# print(delta)
# datetime.timedelta