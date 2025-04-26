F1_driver = ["Max Verstappen", "Lando Noris", "Lewis Hamilton", "Pierre Gasly", "Fernando Alonso"]

F1_2025 = ["Oscar Piastri", "George Russell", "Kimi Antonelli", "Charles Leclerc", "Alex Albon", "Esteban Ocon", "Lance Stroll","Nico Hulkenberg", "Liam Lawson", "Isack Hadjar", "Carlso Sainz", "Yuki Tsunoda", ]


while True:

    driver_to_remove = input("What item do you want to remove from the list?")
    
 
    if driver_to_remove.lower() == 'stop':
        break
    
    
    if driver_to_remove in F1_driver:
        F1_driver.remove(driver_to_remove)
        print(driver_to_remove, "has been removed from the list.")
    else:
        print(driver_to_remove, "is not in the list.")
    
    
    print("Updated driver list:", F1_driver)

    driver_add = input("what driver do you want to add in? ")

    def add_driver_list(driver_add):
        F1_driver[driver_add] = F1_2025
    
    if driver_add in F1_2025:
        F1_driver.append(driver_add)
        print(driver_add, "has been added to the list")
    else:
        print(driver_add, "is not on the list")

    print("Updated driver list", F1_driver)

    add_list = input("do you want to keep going. ")
    if add_list == "no":
        break



print("Final driver list:", F1_driver)