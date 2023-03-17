def add_time(t1, t2, day=None):
  #split hours, minutes and day_zone
  end_time = t1.split() 
  time = end_time[0].split(":")
  hr = int(time[0])
  mins = int(time[1])

  endin_base = end_time[1]
  
  time1 = t2.split(":") 
  hr1 = int(time1[0])
  mins1 = int(time1[1])

  # count how many hours in duration time
  day_count = int(hr1 / 24)
  # in task from Assignment:
  #         add_time("6:30 PM", "205:12") 
  #         Returns: 7:42 AM (9 days later)
  #if divided "205/24" result will be 8.542 but not "9 days later", thats why we received remainder of the division and indicate that if we have 0.5 day count as 1 day
  day_c = hr1 / 24
  d_c = int(day_c % 1 * 10)
  if d_c >= 5:
    day_count += 1

  #count minutes
  f_mins = mins + mins1  
  if f_mins >= 60:
    hr += 1
    f_mins = f_mins % 60
  f_mins = f_mins if f_mins>9 else "0" + str(f_mins)
  
  
  f_hr = int((hr + hr1)%12)
  f_hr = f_hr = 12 if f_hr == 0 else f_hr
  
  #prepare flipping of day zone
  flip_count = int((hr + hr1)/12)
  endin_flip = {"PM": "AM", "AM": "PM"}
  if (endin_base == "PM" and hr + (hr1 % 12) >= 12):
    day_count += 1
    
  #flipp day zone
  endin_base = endin_flip[endin_base] if flip_count % 2 == 1 else endin_base

  #assign final result string to variable f_result
  f_result = str(f_hr) + ":" + str(f_mins) + " " + endin_base
  days_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}

  #create array with days of the week 
  days_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  # check if variable day not equal to None, matching day with days of the week and add to the string variable f_result name of the day
  if day != None:
    day = day.lower()
    index = int((days_index[day]) + day_count) % 7
    new_d = days_array[index]
    f_result = str(f_hr) + ":" + str(f_mins) + " " + endin_base + ", " + new_d
  # count how many days from starting time and add necessary ending to the string variable f_result: next_day or days later
  if (day_count == 1):
    return f_result + " " + "(next_day)"
  elif(day_count > 1):
    return f_result + " (" + str(day_count) + " days later)"
  return f_result
