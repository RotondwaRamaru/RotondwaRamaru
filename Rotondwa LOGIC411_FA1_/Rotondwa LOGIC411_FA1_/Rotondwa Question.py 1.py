#Question 2 
print("\t\t\tMeadowdale Dairy Farm")

#2.1
Eggs_wanted = int(input("\n\nHow many eggs would you like: "))

#2.2
def calculate_eggs(Eggs_wanted):
    dozens = Eggs_wanted // 12
    loose_eggs = Eggs_wanted % 12
    return dozens, loose_eggs

dozens, loose_eggs = calculate_eggs(Eggs_wanted)

#2.3
cost_dozen = 3.25
cost_loose = 0.45
total_cost = (dozens*cost_dozen) + (loose_eggs * cost_loose)

#2.4
print(f"\nCustomer wants {dozens} dozen and {loose_eggs} loose egg(s).")
print("\n\t\t\t\t\tTotal due: R", total_cost)