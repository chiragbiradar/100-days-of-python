print('''
 █     █░▓█████  ██▓     ▄████▄   ▒█████   ███▄ ▄███▓▓█████    ▄▄▄█████▓ ▒█████                
▓█░ █ ░█░▓█   ▀ ▓██▒    ▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▓█   ▀    ▓  ██▒ ▓▒▒██▒  ██▒              
▒█░ █ ░█ ▒███   ▒██░    ▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▒███      ▒ ▓██░ ▒░▒██░  ██▒              
░█░ █ ░█ ▒▓█  ▄ ▒██░    ▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ▒▓█  ▄    ░ ▓██▓ ░ ▒██   ██░              
░░██▒██▓ ░▒████▒░██████▒▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒░▒████▒     ▒██▒ ░ ░ ████▓▒░              
░ ▓░▒ ▒  ░░ ▒░ ░░ ▒░▓  ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░░░ ▒░ ░     ▒ ░░   ░ ▒░▒░▒░               
  ▒ ░ ░   ░ ░  ░░ ░ ▒  ░  ░  ▒     ░ ▒ ▒░ ░  ░      ░ ░ ░  ░       ░      ░ ▒ ▒░               
  ░   ░     ░     ░ ░   ░        ░ ░ ░ ▒  ░      ░      ░        ░      ░ ░ ░ ▒                
    ░       ░  ░    ░  ░░ ░          ░ ░         ░      ░  ░                ░ ░                
                        ░                                                                      
▄▄▄█████▓ ██░ ██ ▓█████    ▄▄▄█████▓ ██▀███  ▓█████ ▄▄▄        ██████  █    ██  ██▀███  ▓█████ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓  ██▒ ▓▒▓██ ▒ ██▒▓█   ▀▒████▄    ▒██    ▒  ██  ▓██▒▓██ ▒ ██▒▓█   ▀ 
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒ ▓██░ ▒░▓██ ░▄█ ▒▒███  ▒██  ▀█▄  ░ ▓██▄   ▓██  ▒██░▓██ ░▄█ ▒▒███   
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ░ ▓██▓ ░ ▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██   ▒   ██▒▓▓█  ░██░▒██▀▀█▄  ▒▓█  ▄ 
  ▒██▒ ░ ░▓█▒░██▓░▒████▒     ▒██▒ ░ ░██▓ ▒██▒░▒████▒▓█   ▓██▒▒██████▒▒▒▒█████▓ ░██▓ ▒██▒░▒████▒
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░     ▒ ░░   ░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░░ ▒░ ░
    ░     ▒ ░▒░ ░ ░ ░  ░       ░      ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░░ ░▒  ░ ░░░▒░ ░ ░   ░▒ ░ ▒░ ░ ░  ░
  ░       ░  ░░ ░   ░        ░        ░░   ░    ░    ░   ▒   ░  ░  ░   ░░░ ░ ░   ░░   ░    ░   
          ░  ░  ░   ░  ░               ░        ░  ░     ░  ░      ░     ░        ░        ░  ░
                                                                                               
 ██░ ██  █    ██  ███▄    █ ▄▄▄█████▓                                                          
▓██░ ██▒ ██  ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒                                                          
▒██▀▀██░▓██  ▒██░▓██  ▀█ ██▒▒ ▓██░ ▒░                                                          
░▓█ ░██ ▓▓█  ░██░▓██▒  ▐▌██▒░ ▓██▓ ░                                                           
░▓█▒░██▓▒▒█████▓ ▒██░   ▓██░  ▒██▒ ░                                                           
 ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒   ▒ ░░                                                             
 ▒ ░▒░ ░░░▒░ ░ ░ ░ ░░   ░ ▒░    ░                                                              
 ░  ░░ ░ ░░░ ░ ░    ░   ░ ░   ░                                                                
 ░  ░  ░   ░              ░                                                                    
                                                                                               
''')

print("Your mission is to find treasure")

direction = input()
direction = direction.lower()
if direction == "right":
    print("Game Over")
elif direction == "left":
    answer = input()
    answer = answer.lower()
    if answer=="swim":
        print("Game Over")
    elif answer=="wait":
        door = input()
        door = door.lower()
        if door == "red":
            print("Game Over")
        elif door == "blue":
            print("Game Over")
        elif door == "Yellow":
            print("Congrats You found the Treasure!!!")
