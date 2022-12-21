def main():
    msg = input("what is the hour? ")
    time = convert(msg)
    if time >= 7 and time <= 8:
        print("Breakfast time")
    if time >= 12 and time <= 13:
        print("lunch time")
    if time >= 18 and time <= 19:
        print("dinner")
def convert(msg):
    hours, minutes = msg.split(":")
    new_minutes = float(minutes) / 60
    return float(hours) + new_minutes
if __name__ == "__main__":
    main()