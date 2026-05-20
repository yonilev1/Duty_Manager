import soldier_manager, duty_manager

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
    soldier_ma = int(input("Enter soldiers MA (1-7 digits): "))
    soldier_name = input("Enter soldiers name (7-20 chars): ")
    soldier_manager.add_soldier(soldier_ma, soldier_name)
    

def handle_remove_soldier():
    soldier_ma = int(input("Enter soldiers MA (7 digits): "))
    soldier_manager.remove_soldier(soldier_ma)


def handle_view_soldiers():
    soldier_manager.get_all_soldiers()


def handle_add_duty():
    soldier_ma = int(input("Enter soldiers MA (7 digits): "))
    duty_name = input("Enter the duties name: ")
    duty_day = input("Enter the duties due date: ")
    duty_manager.add_duty_to_soldier(soldier_ma, duty_name, duty_day)


def handle_update_duty_status():
    soldier_ma = int(input("Enter soldiers MA (7 digits): "))
    duty_name = input("Enter duties name: ")
    new_status = input("Enter tasks status: ")
    duty_manager.update_duty_status(soldier_ma, duty_name, new_status)


def handle_view_soldier_duties():
    soldier_ma = int(input("Enter soldiers MA (7 digits): "))
    print(duty_manager.get_soldier_duties(soldier_ma))


def main():
    while True:
        show_menu()
        choice = get_user_choice()

        try:
            match choice:
                case 1:
                    handle_add_soldier()
                case 2:
                    handle_remove_soldier()
                case 3:
                    handle_add_duty()
                case 4:
                    handle_update_duty_status()
                case 5:
                    handle_view_soldiers()
                case 6:
                    handle_view_soldier_duties()
                case 0:
                    break
        except Exception as e:
            print(e)
        

if __name__ =="__main__":
    main()


    
    
