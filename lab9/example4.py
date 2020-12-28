import time
def countdown(t):
    if t ==0:
        print("B U M")
        return
    else:
        print(f"{t} seconds remaining")
        time.sleep(1)
        return countdown(t-1)
countdown(5)
