from time import sleep

seconds = 15
while seconds >= 0:
    mins, secs = divmod(seconds, 60)
    time = "   {:02d}:{:02d}".format(mins,secs)
    print(time, end="\r")
    sleep(1)
    seconds -= 1