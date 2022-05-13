# Pjestimi
def pjestimi(x, y):
    return x / y

# Shumezimi
def shumezimi(x, y):
    return x * y

# Mbledhja
def mbledhja(x, y):
    return x + y

# Zbritja
def zbritja(x, y):
    return x - y

print("Zgjidh njerin nga operatoret:")
print("1.Pjestimi")
print("2.Shumezimi")
print("3.Mbledhja")
print("4.Zbritja")

while True:
    # Merr nje input nga perdoruesi
    zgjedhjet = input("Zgjidh njeren:(1/2/3/4): ")

    if zgjedhjet in ('1', '2', '3', '4'):
        num1 = float(input("Shkruaj numrin e pare: "))
        num2 = float(input("Shkruaj numrin e dyte: "))

        if zgjedhjet == '1':
            print(num1, "/", num2, "=", pjestimi(num1, num2))

        elif zgjedhjet == '2':
            print(num1, "*", num2, "=", shumezimi(num1, num2))

        elif zgjedhjet == '3':
            print(num1, "+", num2, "=", mbledhja(num1, num2))

        elif zgjedhjet == '4':
            print(num1, "-", num2, "=", zbritja(num1, num2))


        kalkulimi_tjeter = input("Le te bejme kalkulimin tjeter? (po/jo): ")
        if kalkulimi_tjeter == "jo":
            break
        else:
          print("?")
