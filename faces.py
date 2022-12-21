def main():
    msg = input("msg: ")
    new_msg = convert(msg)
    print(new_msg)
def convert(msg):
    new_msg = msg.replace(":)", "🙂").replace(":(", "🙁")
    return new_msg
main()
