#import time
#t = time.strftime('%H:%M:%S')
#hour = time.strftime('%H')
hour = int(input("Enter hour: "))
print(hour)
if(hour=>0 and hour<12):
  print("good morning")
elif(hour>=12 and hour<16):
  print("good afternoon")
elif(hour>=16 and hour<19):
  print("good evening")
elif(hour>=19 and hour<0):
  print("good night")
