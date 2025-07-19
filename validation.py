from display_menu import menu
def login():
    saved_pin='1234'
    attempt=3
    while True:
        user_pin=input("Enter your 4 digit pin: ")
        if len(saved_pin)!=len(user_pin):
            print("Try Again! Enter four digit pin")
        elif len(saved_pin)==len(user_pin):
            if saved_pin==user_pin:
                print("Login successful")
                menu()
                break

            else:
                print(f"Wrong pin entered! Attempt left {attempt}")
                if attempt==0:
                    print("Account freezed for 24 hours")
                    return attempt
                attempt+=1
