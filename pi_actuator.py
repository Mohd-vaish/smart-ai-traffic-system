import time
import time

def control_signal(signal):
    print(f"🚦 Signal set to: {signal}")
    time.sleep(2)


def control_signal(signal):
    print(f"🚦 Signal set to: {signal}")
    time.sleep(2)

if __name__ == "__main__":
    while True:
        control_signal("GREEN")
        control_signal("YELLOW")
        control_signal("RED")
