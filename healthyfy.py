from pygame import mixer
import datetime
from time import time
def notification(stop):
    mixer.init()
    mixer.music.load("Run fast music.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play(-1)
    while True:
        query = input()           
        if query==stop:
            mixer.music.stop()
            break
            
def log(Activity):
    with open("log.txt",'a') as f:
        f.write(f"{Activity} exercise completed at {datetime.datetime.now()}\n")
if __name__=='__main__':
    init_water=time()
    init_eyes=time()
    init_exercise=time()
    watersecs=2
    eyesecs=5
    exercisesec=10
    while True:
        
        if time()-init_water>watersecs:
            print("Water drinking time. Enter Drank to stop")
            notification("Drank")
            init_water=time()
            log("Water")
        if time()-init_eyes>eyesecs:
            print("Eyes exercise time. Enter Done to stop")
            notification("Done")
            init_eyes=time()
            log("Eye")     
        if time()-init_exercise>exercisesec:
            print("Physical exercise time.Enter Done to stop")
            notification("Done")
            init_exercise=time()
            log("Physical")
