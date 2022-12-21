def main():
    msg = input("msg: ")
    new_message = convert(msg)
    print (new_message)

def convert(msg):
    new_message = msg.replace(":)", "🙂").replace(":(", "🙁")
    return new_message
main()