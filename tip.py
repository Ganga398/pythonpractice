def main():
    dollars = dollars_to_float(input("How much was the food?"))
    percent = percent_to_float(input("how much percent do you want to give?"))
    tip = dollars * percent
    print(f"leave ${tip:.2f}")

def dollars_to_float(d):
    d = d.replace("$", "")
    return float(d)
def percent_to_float(p):
    p = p.replace("%", "")
    p = float(p)/100
    return float(p)

main()