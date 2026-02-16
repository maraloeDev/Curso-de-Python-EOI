while True:
    entrada = input("Enter age (or 'exit' to stop): ")
    if entrada.lower() == 'exit':
        break
    age = int(entrada)
    if age >= 20:
        print("Adult")
    elif age >= 10:
        print("Youth")
    else:
        print("Kid")
