import sys, time, random

def loading_bar(display_message, pause_time=0.04, loading_symbol="#"):
    spaces = "--------------------"
    bars = ""
    print(display_message)
    for i in range(101):
        if i % 5 == 0:
            bars += loading_symbol
            spaces = spaces[:-1]
        sys.stdout.write(f"\r[{bars}{spaces}] {i}%")
        sys.stdout.flush()
        time.sleep(pause_time)
    print()

def spaz_out(duration=5, max_chars=100):
    """
    Displays random characters on the screen to create a "screen spazzing out" effect.

    Args:
        duration (float, optional): The duration of the spazzing effect in seconds. Defaults to 5.
        max_chars (int, optional): The maximum number of random characters to display per iteration. Defaults to 100.
    """
    start_time = time.time()
    while time.time() - start_time < duration:
        # Generate a list of random characters
        random_chars = [chr(random.randint(33, 126)) for _ in range(random.randint(1, max_chars))]

        # Print the random characters to the screen
        sys.stdout.write('\r' + ''.join(random_chars))
        sys.stdout.flush()

        # Add a short delay to create the "spazzing" effect
        time.sleep(0.01)

    # Clear the screen
    sys.stdout.write('\r' + ' ' * 80 + '\r')
    sys.stdout.flush()

def sign_in():
  secret_username = "opensesame"
  hacker_username = "Hacker123"
  
  loading_bar("Loading...")

  username = str(input("Enter your username: "))
  if username == "opensesame":
    loading_bar("Encrypted authentication in progress...")
    print("Congrats! You have been granted administrative abilities!")
  elif username == "Hacker123":
    spaz_out(10, 500)

  password = str(input("Enter your password: "))

  correct_username = "admin"
  correct_password = "password123"

  loading_bar("Processing...")
  
  if username != correct_username and username != secret_username and username != hacker_username:
    print("Your username is incorrect, please try again")
    sign_in()
  elif password != correct_password:
    print("Your password is incorrect, please try again")
    sign_in()
  else:
    loading_bar("Authenticating...")
    print("Congrats! You have been successfully signed in!")    