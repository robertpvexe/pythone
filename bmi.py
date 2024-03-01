print("Obliczymy twoje BMI, poniżej podaj nam wymagane dane!")
waga = int(input("Podaj swoją wagę w kilogramach: "))
wzrost = float(input("Podaj swój wzrost w centymetrach: "))/100

bmi = round(waga / (wzrost * wzrost), 2)

if bmi < 18.5:
    print(f"Masz niedowage, zjedz snikersa " + {bmi})
elif 18.5 <= bmi >= 24.9:
    print(f"Waga ok, ale przydałoby się iść na siłownie wariacie {bmi}")
elif 25 <= bmi >= 29.9:
    print(f"Masz nadwagę, idź na siłownie grubasie {bmi}")
else:
    print(f"no kurwa to przesada, idź ćwiczyć i nie wpierdalaj tyle {bmi}")