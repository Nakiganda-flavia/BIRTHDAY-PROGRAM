import calendar
NAME=input('ENTER NAME: ')
months=['January','February','March','April','May','June',
        'July','August','September','October','November','December']
days=['Monday', 'Tuesday','Wednesday',
      'Thursday', 'Friday', 'Saturday', 'sunday']
print('Hello! '+NAME+", What's your Birthday?\nEdit Date integers")
d=input('Enter Your Day(1-31): ')
DAY=int(d)
m=input('Enter Your Month(1-12): ')
MONTH=int(m)
y=input('Enter Your Year: ')
YEAR=int(y)
day_index =calendar.weekday(month=MONTH, day=DAY, year=YEAR)
print(NAME+', you were born on '+ days[day_index]+' '+d+'/'+months[MONTH-1]+'/'+y)
input('Press <Enter> to Exit')
