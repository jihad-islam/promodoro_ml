work_session_time = 25*60
short_break_time = 5*60
long_break_time = 15*60

def show_menu():
    print("Welcome to ML powered Promodoro Timer!")
    print('1. Start Work Session (25 minutes)')
    print('2. Short Break (5 minutes)')
    print('3. Long Break (15 minutes)')
    print('4. Exit')

def main():
    while True:
        show_menu()
        choice = input('Choose and option: ').strip()

        if choice == '1':
            print('Work session selected.')
        elif choice == '2':
            print('Short break selected.')
        elif choice == '3':
            print('Long break selected.')
        elif choice == '4':
            print('Goodbye!')
            break
        else:
            print('Invalid choice.')


if __name__ == "__main__":
    main()