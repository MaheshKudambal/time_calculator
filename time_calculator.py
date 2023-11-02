

# function to make 12 hours time format
def helper(hr,mn,days):
    days+=hr//24
    hr%=24
    hr+=mn//60
    mn%=60
    return [hr,mn,days]

#  main function to add time 
def add_time(initial_time,added_time,week_day=''):

    time1 = initial_time.split()[0]
    t = initial_time.split()[1]
    hr1 = int(time1.split(':')[0])
    mn1 = int(time1.split(':')[1])
    hr2 = int(added_time.split(':')[0])
    mn2 = int(added_time.split(':')[1])

    # calling helper function to make added time to 12 hour format
    temp = helper(hr2,mn2,0)
    # calling helper function to make overall time to 12 hour format
    temp2=helper(hr1+temp[0],mn1+temp[1],temp[2])
    # final hour 
    hr=temp2[0]
    # final minute 
    mn=temp2[1]
    # total days count
    days=temp2[2]

    # checking is still hour is in 24 hour format
    if hr>12:hr%=12

    # calculating left time to 12 o'clock 
    hr3=abs(11-hr1)
    mn3=abs(60-mn1)

    # cheking if added time is already greater than leftover time to become 12 o'clock
    if temp[0]>=hr3:
        if t=='AM':t='PM'
        else:t='AM'

    # if hour became 00 then we can consider it as 12
    if hr==0:hr=12

    # just to make hour and minute in correct format of two digits
    if hr>0 and hr<10:hr='0'+str(hr)
    else:hr=str(hr)
    if mn<10:mn='0'+str(mn)
    else:mn=str(mn)

    print(hr+':'+mn,t,end='')

    # if week day is provided then will print it
    if len(week_day)!=0:
        print(',',week_day.upper(),end='')

    # printing total days 
    if days==1:print(' (next day)',end='')
    elif days>1:print(' ({} days later)'.format(days))

add_time("01:03 PM", "10:57", "tueSday")




