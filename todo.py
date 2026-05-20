tasks = []

while True:
    print("/n1. Näytä tehtävät")
    print("2. Lisää tehtävä")
    print("3. Poista tehtävä")
    print("4. Lopeta")

    choice = input("Valitse:")

    if choice == "1":
        if len(tasks) == 0:
            print("Ei tehtäviä")
        else:
            for i, task in enumerate(tasks):
                 print(f"{i + 1}. {task}")

    elif choice == "2":
       task = input("Lisää tehtävä:")
       tasks.append(task)

    elif choice == "3":
       number = int(input("Mikä poistetaan: "))
       if 0 < number <= len(tasks):
           tasks.pop(number - 1)

    elif choice == "4":
       break
