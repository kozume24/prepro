""" airport """

def cal_time(time):
    time_abv = time.split(" ")
    time_con = time_abv[1]
    depart = time_abv[0].split(":")
    hr = depart[0]
    minute = depart[1]
    return hr, minute, time_con

def country(foreign):
    hours_gap = 0
    minutes_gap = 0
    if foreign == "SGN":
        hours_gap += 1
        minutes_gap += 50
    elif foreign == "ATL":
        hours_gap += 20
        minutes_gap += 55
    elif foreign == "YVR":
        hours_gap += 16
        minutes_gap += 20
    elif foreign == "SYD":
        hours_gap += 9
        minutes_gap += 0
    else:
        hours_gap += 13
        minutes_gap += 0
    return hours_gap, minutes_gap

def main():
    departure_time = input("")
    arrive = input("")
    cal_time(departure_time) #แก้
    arrive = arrive[-4:-1]
    country(arrive) #แก้