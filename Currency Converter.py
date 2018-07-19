import time

print("Welcome to Sabads' Currency Converter")
time.sleep(0.5)
a = input("What is your name? ")
time.sleep(0.5)
print("Hello,", a,)
time.sleep(0.5)
def main():
    count = 0
    print("First, Select what currency you want to convert.")
    time.sleep(0.5)
    print("A.Dollars to Dirham")
    time.sleep(0.5)
    print("B.Dirham to Dollar")
    time.sleep(0.5)
    b = input("Which one??? [A/B] ")

    f = 0
    d = 0

    if b == "A" or b == "a" or b == "Dollars to Dirham" or b == "dollars to dirham":
        time.sleep(0.5)
        c = int(input("How many dollars "))
        d = 3.67*c
        print("Proccessing.....")
        time.sleep(2)
        print("AED", d,)

    if b == "B" or b == "b" or b == "Dirham to Dollars " or b == "dirham to dollar":
        time.sleep(0.5)
        e = int(input("How many dirhams "))
        f = 0.27*e
        print("Proccessing.....")
        time.sleep(2)
        print(f, "$")

    restart = str(input("Do you want to convert again? "))
    if restart == "Yes" or restart == "yes" or restart == "YES" or restart == "y" or restart == "Y":
            main()
    else:
        print("Thanks for using my Currency Converter")
        exit()
