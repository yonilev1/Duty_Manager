import soldier_manager

def show_menu():
    print("""
Welcome to the duty Maneger App:
          To add a soldier - 1,
          To delete a soldier - 2,
          To assign duty to soldier - 3,
          To update duties status - 4,
          To show all soldiers - 5,
          To show a soldiers duties - 6,
          To exit - 0.
""")
    

def get_user_choice():
    choice = int(input("Please enter your choice: "))
    print(f"You chose option: {choice} ->")
    return choice


def handle_add_soldier():
    soldier_ma = int(input("Enter soldiers MA (7 digits): "))
    soldier_name = input("Enter soldiers name (7-20 chars): ")
    #logic by soldier_manager
    

def handle_remove_soldier():
    soldier_ma = int(input("Enter soldiers MA (7 digits): "))
    #logic by soldier_manager


def handle_view_soldiers():
    #call view by soldier_manager
    pass


def handle_add_duty():
    soldier_ma = int(input("Enter soldiers MA (7 digits): "))
    #call create tast
    #call add duty to soldier in soldeir_manager


def handle_update_duty_status():
    status = input("Enter tasks status: ")
    #call update duty


def handle_view_soldier_duties():
    soldier_ma = int(input("Enter soldiers MA (7 digits): "))
    #call soldier_manager


def main():
    soldier_list = []
    duties_list = []
    show_menu()
    choice = get_user_choice()
    while True:
        match choice:
            case 1:
                handle_add_soldier()
            case 2:
                handle_remove_soldier()
            case 3:
                handle_add_duty()
            case 4:
                handle_update_duty_status
            case 5:
                handle_view_soldiers()
            case 6:
                handle_view_soldier_duties
            case 0:
                break
        


    
    
