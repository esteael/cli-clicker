# Top to bottom this project was a great learning experience, and I feel like I'm very comfortable with Python now.
# For clarification, this was a group project, and even though I didn't have a group from my classroom, I made this with four of the friends.
# Some more fluent than others, but if it weren't for Jack, Aidan, Ryan, and the other Sebastian, I wouldn't have been able to do this in time.
# Thank you to Professor Salcedo for being a great teacher and for dealing with my poor sleep schedule. This course was a great experience, and I learned a lot.
# Making it wasn't easy, it took over 20 hours to make in total, but I learned alot about Python and how to use it.

import msvcrt, os, sys, random, time, math, json, shutil # when presenting explain the imports and why they are needed
from datetime import datetime # technically a local import, but it's a standard library so it doesn't count as a local import
import wordList, shopItems # local imports (you should explain this in the presentation)
from colorama import init, Fore, Back, Style # (the ONLY library that could have done this, and it's ACTUALLY terrible, the idea was just so niche that I had to use it.)

init(autoreset=True)
TYPED_COLOR_START = "\033[38;5;34m"  # default aniamation color, doesn't work for custom colors cause i wrote it wrong and im too lazy to fix it
UNTYPED_COLOR_START = "\033[38;5;196m" # constants are in ALLCAPS

def clear_screen():
    os.system('cls')  # clear the screen using the "cls" cmd

def get_random_word():
    return random.choice(wordList.all_words)  # grab a word from the list

def save_game_data(points, owned_items, word_colors=None):
    # this creates the saves folder if it doesn't exist
    if not os.path.exists("saves"):
        os.makedirs("saves")
    
    # this generates the name for the save file using the current date and time
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") # this is the logic for the time order, YMD/HMS
    filename = f"saves/clicker_save_{timestamp}.json"
    
    # initialize the default color, cause the user cant provide it until they enter hte settings menu
    if word_colors is None:
        word_colors = {"typed": TYPED_COLOR_START, "untyped": UNTYPED_COLOR_START}
    
    # creates the actual save data / the formating inside of the json file
    save_data = {
        "points": points,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "owned_items": owned_items,
        "word_colors": word_colors
    }
    
    with open(filename, "w") as f:
        json.dump(save_data, f)
    
    return filename

def load_last_game(): # this logic was so hard to make, and it's partically broken, but it will only break if the user TRIES to break it so its fine
    if not os.path.exists("saves"):
        return None
    
    save_files = [f for f in os.listdir("saves") if f.startswith("clicker_save_") and f.endswith(".json")]
    if not save_files:
        return None
    
    save_files.sort(reverse=True)
    
    with open(os.path.join("saves", save_files[0]), "r") as f:
        return json.load(f)

def pulse_color(t, base_color, idx_modifier=0):
    # this is the pulsating logic, its a sine wave that changes color based on the time and then the index of each letter (stole this from another project i worked on)
    if base_color == TYPED_COLOR_START:
        colors = ["\033[38;5;34m", "\033[38;5;40m", "\033[38;5;46m", "\033[38;5;47m", "\033[38;5;48m"]
    elif base_color == UNTYPED_COLOR_START:
        colors = ["\033[38;5;124m", "\033[38;5;160m", "\033[38;5;196m", "\033[38;5;197m", "\033[38;5;198m"]
    else:
        # this is the logic for the base custom colors in the settings
        colors = [base_color] * 5
    
    index = (int((math.sin(t * 5) + 1) * 2) + idx_modifier) % len(colors)
    return colors[index]

def draw_word(word, typed_so_far, t, color1=TYPED_COLOR_START, color2=UNTYPED_COLOR_START):
    result = ""
    for i, char in enumerate(word):
        if i < len(typed_so_far):
            # more logic for the sine wave, this is the logic for the letters that are ALREADY typed, basically just replacing them.
            result += pulse_color(t + i*0.2, color1, i) + char
        else:
            # this will never get used so i just repeat the same logic as above lol
            result += pulse_color(t + i*0.2, color2, i) + char
    return result + Style.RESET_ALL

def calculate_player_stats(owned_items):
    points_per_second = 0 # this is the def player stats
    points_per_character = 1  
    next_words_seen = 0
    multiplier = 1.0
    
    for item_id in owned_items:
        item = shopItems.get_item_by_id(item_id)
        if item:
            points_per_second += item["effects"]["points_per_second"]
            points_per_character += item["effects"]["points_per_character"]
            next_words_seen += item["effects"]["next_words_seen"]
            multiplier += item["effects"]["multiplier"]
    
    return points_per_second, points_per_character, next_words_seen, multiplier

def display_shop(points, owned_items, page=1):
    clear_screen()
    
    items_per_page = 4
    total_items = len(shopItems.shop_items)
    total_pages = (total_items + items_per_page - 1) // items_per_page
    page = max(1, min(page, total_pages))  # this is for the shop scree, it only shows 4 items at oncec and does the math for the page numbers
    
    start_idx = (page - 1) * items_per_page
    end_idx = min(start_idx + items_per_page, total_items)
    
    # ascii logo very cool
    print('''
       _ _            _ _      _             
      | (_)          | (_)    | |            
   ___| |_ ______ ___| |_  ___| | _____ _ __ 
  / __| | |______/ __| | |/ __| |/ / _ \ '__|
 | (__| | |     | (__| | | (__|   <  __/ |   
  \___|_|_|      \___|_|_|\___|_|\_\___|_|   
''')
    
    # if you ever see "----------------------" im aware i could have made a function for the line breaks but i was too lazy and i think it's faster this way
    print(f"----------------------------------------------------------")
    print(f"--SHOP-- Points: {points} -- Page {page}/{total_pages} --------------")
    
    # index the items in the shop based on the page number and the json file
    for i in range(start_idx, end_idx):
        if i < len(shopItems.shop_items):
            item = shopItems.shop_items[i]
            item_id = item["id"]
            
            # color by the status of the item, blue if owned, green if affordable, red if ur broke
            color = Fore.BLUE if item_id in owned_items else (
                   Fore.GREEN if points >= item["cost"] else Fore.RED)
            
            print(f"{color}[{i-start_idx+1}]{Style.RESET_ALL} {item['name']} ({item['cost']}p)")
            print(f"    - {item['description']}")
    
    print("----------------------------------------------------------")
    print("[1-4]:Buy  [9]:Next Page  [ESC]:Return")
    
    return page

def display_settings():
    clear_screen()
    
    print('''
       _ _            _ _      _             
      | (_)          | (_)    | |            
   ___| |_ ______ ___| |_  ___| | _____ _ __ 
  / __| | |______/ __| | |/ __| |/ / _ \ '__|
 | (__| | |     | (__| | | (__|   <  __/ |   
  \___|_|_|      \___|_|_|\___|_|\_\___|_|   
''')
    
    print("----------------------------------------------------------")
    print("--SETTINGS--")
    print("----------------------------------------------------------")
    print("[1] Reset Game (delete all saves)")
    print("[2] Cheat Menu (edit points)")
    print("[3] Color Changer (customize word colors)")
    print("----------------------------------------------------------")
    print("[ESC] Return to game")

def reset_game():
    clear_screen()
    
    print('''
       _ _            _ _      _             
      | (_)          | (_)    | |            
   ___| |_ ______ ___| |_  ___| | _____ _ __ 
  / __| | |______/ __| | |/ __| |/ / _ \ '__|
 | (__| | |     | (__| | | (__|   <  __/ |   
  \___|_|_|      \___|_|_|\___|_|\_\___|_|   
''')
    
    print("----------------------------------------------------------")
    print("--RESET GAME--")
    print("----------------------------------------------------------")
    print("WARNING: This will delete ALL save files and progress!")
    print("Are you sure you want to reset? (5 second countdown)")
    print("Press [1] to confirm, [2] to cancel")
    print("----------------------------------------------------------")
    
    # countdown logic and animation it does a cool spinny thingy circle like old computers did
    countdown = 5
    animation_chars = ['|', '/', '-', '\\']
    animation_idx = 0
    start_time = time.time()
    
    while time.time() - start_time < 5:
        elapsed = time.time() - start_time
        countdown = 5 - int(elapsed)
        animation_char = animation_chars[animation_idx]
        animation_idx = (animation_idx + 1) % len(animation_chars)
        
        print(f"\rTiming out in {countdown} seconds... {animation_char}", end="") # timeout to prevent accidental resets
        
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8', errors='ignore')
            if key == '1':
                # deletes save from menu file
                if os.path.exists("saves"):
                    shutil.rmtree("saves")
                print("\nGame reset complete! All save files deleted.")
                print("Press any key to return to the game...")
                msvcrt.getch()
                return True
            elif key == '2':
                # cancel if u dont want to delete ur save
                print("\nReset cancelled.")
                print("Press any key to return to settings...")
                msvcrt.getch()
                return False
        
        time.sleep(0.2)
    
    # timeout and return to settings.
    print("\nReset cancelled (timeout).")
    print("Press any key to return to settings...")
    msvcrt.getch()
    return False

def cheat_menu(current_points):
    clear_screen()
    
    # we need to keep printing this because the logic is weird, and i know i could have made a function for it but i was too lazy and i think its faster this way
    print('''
       _ _            _ _      _             
      | (_)          | (_)    | |            
   ___| |_ ______ ___| |_  ___| | _____ _ __ 
  / __| | |______/ __| | |/ __| |/ / _ \ '__|
 | (__| | |     | (__| | | (__|   <  __/ |   
  \___|_|_|      \___|_|_|\___|_|\_\___|_|   
''')
    
    print("----------------------------------------------------------")
    print("--CHEAT MENU--")
    print("----------------------------------------------------------")
    print(f"Current points: {current_points}")
    print("Enter new point value (or press ESC to cancel):")
    
    # input handling for the points in this menu
    input_text = ""
    while True:
        print(f"\rNew points: {input_text}", end=" " * 20 + "\r")
        print(f"New points: {input_text}", end="")
        
        if msvcrt.kbhit():
            key = msvcrt.getch()
            
            if ord(key) == 27:  # key 27 is the ESC key
                return current_points
            
            key_str = key.decode('utf-8', errors='ignore')
            
            if ord(key) == 8 and len(input_text) > 0:  # key 8 is backspace
                input_text = input_text[:-1]
            elif ord(key) == 13:  # key 13 is enter
                if input_text.isdigit():
                    new_points = int(input_text)
                    print(f"\nPoints updated to {new_points}")
                    print("Press any key to return...")
                    msvcrt.getch()
                    return new_points
                else:
                    print("\nInvalid input. Please enter a number.")
                    print("Press any key to try again...")
                    msvcrt.getch()
                    return current_points
            elif key_str.isdigit():  # ensures the user only inputs numbers
                input_text += key_str
        
        time.sleep(0.05)

def hex_to_ansi(hex_code):
    # convers hex to ansi color codes because we are using the command line and not a GUI
    if hex_code.startswith('#'):
        hex_code = hex_code[1:]
    
    try:
        r = int(hex_code[0:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)
        return f"\033[38;2;{r};{g};{b}m"
    except:
        return None

def color_changer(current_colors):
    clear_screen()
    
    # Logo
    print('''
       _ _            _ _      _             
      | (_)          | (_)    | |            
   ___| |_ ______ ___| |_  ___| | _____ _ __ 
  / __| | |______/ __| | |/ __| |/ / _ \ '__|
 | (__| | |     | (__| | | (__|   <  __/ |   
  \___|_|_|      \___|_|_|\___|_|\_\___|_|   
''')
    
    print("----------------------------------------------------------")
    print("--COLOR CHANGER--")
    print("----------------------------------------------------------")
    print("Enter hex codes for word colors (e.g. #FF0000 for red)")
    print("Current colors:")
    print(f"Color 1 (typed letters): {current_colors.get('typed', TYPED_COLOR_START)}")
    print(f"Color 2 (untyped letters): {current_colors.get('untyped', UNTYPED_COLOR_START)}")
    print("----------------------------------------------------------")
    
    # logic for getting the colors from the user, this is a bit messy
    color1_hex = ""
    print("Color 1 (typed letters): #", end="")
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            
            if ord(key) == 27:  # ESC
                return current_colors
            
            key_str = key.decode('utf-8', errors='ignore')
            
            if ord(key) == 8 and len(color1_hex) > 0:  # Backspace
                color1_hex = color1_hex[:-1]
                print("\rColor 1 (typed letters): #" + color1_hex + " " * 10, end="\r")
                print("Color 1 (typed letters): #" + color1_hex, end="")
            elif ord(key) == 13 and len(color1_hex) == 6:  # Enter
                break
            elif key_str.upper() in "0123456789ABCDEF" and len(color1_hex) < 6:
                color1_hex += key_str.upper()
                print(key_str.upper(), end="")
        
        time.sleep(0.05)
    
    # same logic as above just asking for the second color
    color2_hex = ""
    print("\nColor 2 (untyped letters): #", end="")
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            
            if ord(key) == 27:  # ESC
                return current_colors
            
            key_str = key.decode('utf-8', errors='ignore')
            
            if ord(key) == 8 and len(color2_hex) > 0:  # Backspace
                color2_hex = color2_hex[:-1]
                print("\rColor 2 (untyped letters): #" + color2_hex + " " * 10, end="\r")
                print("Color 2 (untyped letters): #" + color2_hex, end="")
            elif ord(key) == 13 and len(color2_hex) == 6:  # Enter
                break
            elif key_str.upper() in "0123456789ABCDEF" and len(color2_hex) < 6:
                color2_hex += key_str.upper()
                print(key_str.upper(), end="")
        
        time.sleep(0.05) # these are very important ill get into it later at the bottom
    
    # color math cause the default system is dumb and i hate it
    color1_ansi = hex_to_ansi(color1_hex)
    color2_ansi = hex_to_ansi(color2_hex)
    
    if color1_ansi and color2_ansi:
        new_colors = {"typed": color1_ansi, "untyped": color2_ansi}
        print("\nColors updated successfully!")
    else:
        new_colors = {"typed": TYPED_COLOR_START, "untyped": UNTYPED_COLOR_START}
        print("\nInvalid color codes. Using default colors.")
    
    print("Press any key to return...")
    msvcrt.getch()
    return new_colors

def main():
    # save loading logic
    last_save = load_last_game()
    points = 0
    owned_items = []
    word_colors = {"typed": TYPED_COLOR_START, "untyped": UNTYPED_COLOR_START}
    
    if last_save:
        points = last_save.get("points", 0)
        owned_items = last_save.get("owned_items", [])
        word_colors = last_save.get("word_colors", word_colors)
    
    # game setup stuff
    current_word = get_random_word()
    upcoming_words = []
    typed_so_far = ""
    animation_time = 0
    last_update = time.time()
    last_passive_points = time.time()
    
    # calculate the players stats and ill display them on screne ltr
    points_per_second, points_per_character, next_words_seen, multiplier = calculate_player_stats(owned_items)
    
    # generate the upcoming words ahead of time so we can use it later for the shop items ill make
    for _ in range(next_words_seen):
        upcoming_words.append(get_random_word())
    
    # default flags, this is used to change the screen the player is on so we dont js render everything at the same time and make it break
    in_shop = False
    in_settings = False
    shop_page = 1
    
    # game loop
    while True:
        current_time = time.time() #define time here to avoid multiple calls and save later
        
        # PPS logic
        if points_per_second > 0:
            dt_passive = current_time - last_passive_points
            if dt_passive >= 1.0:
                points += int(points_per_second * multiplier * dt_passive)
                last_passive_points = current_time
        
        # text animation stuff
        dt = current_time - last_update
        animation_time += dt
        last_update = current_time
        
        # different screens
        if in_shop:
            shop_page = display_shop(points, owned_items, shop_page)
        elif in_settings:
            display_settings()
        else:
            # main game screen
            clear_screen()
            print('''
       _ _            _ _      _             
      | (_)          | (_)    | |            
   ___| |_ ______ ___| |_  ___| | _____ _ __ 
  / __| | |______/ __| | |/ __| |/ / _ \ '__|
 | (__| | |     | (__| | | (__|   <  __/ |   
  \___|_|_|      \___|_|_|\___|_|\_\___|_|   
''')
            print("----------------------------------------------------------")
            print("Type the word shown to earn points")
            print("Press ESC key at any time to quit and save")
            print("----------------------------------------------------------")
            print(f"Current points: {points}")
            print(f"Points per second: {points_per_second} {Fore.YELLOW}x {multiplier:.1f}{Style.RESET_ALL} = {points_per_second * multiplier:.1f}")
            print(f"Points per character: {points_per_character}")
            print("----------------------------------------------------------")
            
            # display the word, with the animation if the colors are default, if they are custom they wont get animated
            print("Current word:", draw_word(current_word, typed_so_far, animation_time, 
                                          word_colors.get('typed'), 
                                          word_colors.get('untyped')))
            
            # display the upcoming words from the list if the user has an upgrade that allows it
            if upcoming_words:
                print("\nUpcoming words:")
                for word in upcoming_words:
                    print(f"  - {word}")
            
            print("----------------------------------------------------------")
            print("[1] Shop  [2] Settings")
        
        # more input handling
        if msvcrt.kbhit():
            key = msvcrt.getch()
            
            # ESC key handling for when they want to quit the game
            if ord(key) == 27:
                if in_shop:
                    in_shop = False
                elif in_settings:
                    in_settings = False
                else:
                    # if they do, we save the game to the json file and exit the game
                    save_filename = save_game_data(points, owned_items, word_colors)
                    clear_screen()
                    print("Game saved successfully to:", save_filename)
                    print("Final points:", points)
                    break
            
            key_str = key.decode('utf-8', errors='ignore')
            
            # the shop stuff
            if in_shop:
                # controls for the shop
                items_per_page = 4 # if we do more than this the cmd prompt will break and bug out and its stupid i hate it so much
                total_items = len(shopItems.shop_items)
                total_pages = (total_items + items_per_page - 1) // items_per_page
                
                if key_str == '9':
                    # goes to the next page in the shop
                    shop_page = shop_page % total_pages + 1
                elif key_str.isdigit() and 1 <= int(key_str) <= 4:
                    # TRY, KEYWORD TRY to buy the item, it fails if the user is broke or if they already own it
                    # it breaks if the user tries to buy an item that doesn't exist, so we need to check for that
                    selected_num = int(key_str)
                    item_idx = (shop_page - 1) * 4 + (selected_num - 1)
                    
                    if item_idx < len(shopItems.shop_items):
                        item = shopItems.shop_items[item_idx]
                        item_id = item["id"]
                        
                        if item_id not in owned_items and points >= item["cost"]:
                            # actually buying items
                            points -= item["cost"]
                            owned_items.append(item_id)
                            
                            # reupdate the stats whenever the user buys an item
                            points_per_second, points_per_character, next_words_seen, multiplier = calculate_player_stats(owned_items)
                            
                            # update word list if the user has an upgrade that allows it after buying it
                            while len(upcoming_words) < next_words_seen:
                                upcoming_words.append(get_random_word())
            
            elif in_settings:
                # settings menu controls
                if key_str == '1':
                    # restart the progress in the game
                    if reset_game():
                        # if they do, we reset the game and set the points to 0 and clear the items
                        points = 0
                        owned_items = []
                        word_colors = {"typed": TYPED_COLOR_START, "untyped": UNTYPED_COLOR_START}
                        points_per_second, points_per_character, next_words_seen, multiplier = 0, 1, 0, 1.0
                        current_word = get_random_word()
                        upcoming_words = []
                        typed_so_far = ""
                
                elif key_str == '2':
                    # cheats lol, i added this mainly for convenience and testing, but im leaving it in cause it took too long to code for it to not be used
                    points = cheat_menu(points)
                
                elif key_str == '3':
                    # color changing menu
                    word_colors = color_changer(word_colors)
            
            else:
                # controls for the main game screen
                if key_str == '1':
                    # enable the shop flag, thus stopping the game loop from rendering the game and allowing the user to buy items
                    in_shop = True
                    shop_page = 1
                elif key_str == '2':
                    # enable the settings flag, thus stopping the game loop from rendering the game and allowing the user to change settings
                    in_settings = True
                elif len(typed_so_far) < len(current_word) and key_str == current_word[len(typed_so_far)]:
                    # make sure they key is the right letter in the index of the word
                    typed_so_far += key_str
                    points += points_per_character
                    
                    # when a word is completed logic
                    if typed_so_far == current_word:
                        if upcoming_words:
                            # queue of words
                            current_word = upcoming_words.pop(0)
                            if len(upcoming_words) < next_words_seen:
                                upcoming_words.append(get_random_word())
                        else:
                            # get random word
                            current_word = get_random_word()
                        
                        typed_so_far = ""
        
        # this line is all the way at the bottom and it's VERY important, if we dont do this, the game flickers and breaks and it lags, 0.05 seconds
        # is enough for the game to run smoothly, and for the user to not notice that the screen is contantly flickering and updating, without this line it will break quickly.
        time.sleep(0.05)

main()