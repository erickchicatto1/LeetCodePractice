'''
My try on the solution

def timeConversion(s):
    # Write your code here
    hours = s[0]
    minutes = s[1]
    seconds = s[2]
    time = ['PM','AM']
    pmTime = {
        "1" : "13",
        "2" : "14",
        "3" : "15",
        "4" : "16",
        "5" : "17",
        "6" : "18",
        "7" : "19",
        "8" : "20",
        "9" : "21",
        "10": "22",
        "11" :"23",
        "12" :"24"
    }
    
    if hours <= "12":
        return hours + minutes + seconds + time[0]
    elif hours >= "12":
        for i in pmTime.items():
            if pmTime[i]==hours:
                return pmTime[i] + minutes + seconds + time[1]


'''

#Correct answer
def timeConversion(s):
    hour = int(s[:2])
    minutes = s[2:8]
    period = s[8:]
    
    if period == "PM" and hour != 12:
        hour += 12
    if period == "AM" and hour == 12:
        hour = 0
    
    return f"{hour:02d}{minutes}" 

