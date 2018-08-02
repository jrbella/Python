days = ("Mon","Tues","Weds","Thurs","Fri","Sat","Sun")

def day_of_the_week(day):
    print(day)
    
#day_of_the_week("Monday")

def days_of_the_week(*args):
    thing = args[0]
    for item in thing:
        if(thing == "Mon"):
            return thing
        
days_of_the_week(days)
        
def daily_reminder(thing):
    steps = 10,000
    print("Today your goal is 10,000 steps")
    return steps
    
daily_reminder(days_of_the_week(days))
