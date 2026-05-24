#https://github.com/yonilev1/Duty_Manager
import soldier_manager, duty_manager, data

def show_menu():
    """
    prints all options of menu
    """

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
    

def get_user_choice()->int:
    """
    get users choice, prints the choice to terminal user

    Returns: 
        option that was chosen(int)
    """
    choice = int(input("Please enter your choice: "))
    print(f"You chose option: {choice} ->")
    return choice


def handle_add_soldier(all_soldiers:list):
    """
    get's soldiers id and name form user, and sends it to the logic level to add to list

    Args:
        all_soldiers(list): list of all soldiers
    Returns:
        None
    """
    soldier_id = int(input("Enter soldiers id (1-7 digits): "))
    soldier_name = input("Enter soldiers name (7-20 chars): ")
    soldier_manager.add_soldier(all_soldiers, soldier_id, soldier_name)
    

def handle_remove_soldier(all_soldiers:list):
    """
    get's soldiers id and sends to ligic level to try to remove

    Args:
        all_soldiers(list): list of all soldiers

    Returns: None
    """
    soldier_id = int(input("Enter soldiers id (7 digits): "))
    soldier_manager.remove_soldier(all_soldiers, soldier_id)


def handle_view_soldiers(all_soldiers:list):
    """
    sends to ligic level to print all soldiers

    gets: list
    returns: None
    """
    soldier_manager.get_all_soldiers(all_soldiers)


def handle_add_duty(all_soldiers:list):
    """
    get's soldier id, duty name and day from user and send to logic level to add

    Args:
        all_soldiers(list): list of all soldiers

    Returns:
        None
    """
    soldier_id = int(input("Enter soldiers id (7 digits): "))
    duty_name = input("Enter the duties name: ")
    duty_day = input("Enter the duties due date: ")
    duty_manager.add_duty_to_soldier(all_soldiers, soldier_id, duty_name, duty_day)


def handle_update_duty_status(all_soldiers:list):
    """
    get's soldier id, duty name and new status from user and send to logic level to update

    Args:
        all_soldiers(list): list of all soldiers

    Returns:
        None
    """
    soldier_id = int(input("Enter soldiers id (7 digits): "))
    duty_name = input("Enter duties name: ")
    new_status = input("Enter tasks status: ")
    duty_manager.update_duty_status(all_soldiers, soldier_id, duty_name, new_status)


def handle_view_soldier_duties(all_soldiers:list):
    """
    get's soldier id and sends to logic level to get all his duties

    Args:
        all_soldiers(list): list of all soldiers

    Returns:
        None
    """
    soldier_id = int(input("Enter soldiers id (7 digits): "))
    print(duty_manager.get_soldier_duties(all_soldiers, soldier_id))


def main():
    """
    oparate all function to use the system
    """
    user_logged_in = True
    all_soldiers = data.soldier_list
    while user_logged_in:
        show_menu()
        choice = get_user_choice()
        try:
            match choice:
                case 1:
                    handle_add_soldier(all_soldiers)
                case 2:
                    handle_remove_soldier(all_soldiers)
                case 3:
                    handle_add_duty(all_soldiers)
                case 4:
                    handle_update_duty_status(all_soldiers)
                case 5:
                    handle_view_soldiers(all_soldiers)
                case 6:
                    handle_view_soldier_duties(all_soldiers)
                case 0:
                    user_logged_in = False
        except ValueError as e:
            print(f"Input error: {e}")

        except KeyError as e:
            print(f"Key not found: {e}")

        except Exception as e:
            print(f"Unexpected error: {e}")
        

if __name__ =="__main__":
    main()


    
    
