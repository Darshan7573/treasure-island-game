@@ -0,0 +1,68 @@
print('''
,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          
                                                                           
                                                                           
                                                               
           88           88                                 88  
           ""           88                                 88  
                        88                                 88  
 ,adPPYba, 88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
a8P_____88 88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88  
8PP""""""" 88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88  
"8b,   ,aa 88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88  
 `"Ybbd8"' 88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8  
 ''')
print("welcome to Treasure Island")
print("Your mission is to find the treasure.")
choice1=input('you\'r at the cross road.Where do you want to go?Type "left" or "right" \n').lower()
if choice1 == "left":
	choice2 =input('You\'ve come to a lake.There is an island in the middle of the lake.Type "make" to build a boat.Type "swim" to swim across\n').lower()
	if choice2 == "make":
		print("U have Successfully build the boat")
		print('''
		 __/\__
  ~~~\____/~~~~~~
    ~  ~~~   ~.       
		''')
	else:
		print("You got attacked by an angry trout.Game Over")
	choice3=input('U make into the island.There is a house with 3 Doors.One "red","yellow" and "blue".Which colour do your choose?\n').lower()
	if choice3 == "red":
			print("You enter a room full of fire.Game Over")
	elif choice3 == "yellow":
			print("You Found the Treasure!You Win")
			print('''
			                                              __----~~~~~~~~~~~------___
                                   .  .   ~~//====......          __--~ ~~
                   -.            \_|//     |||\\  ~~~~~~::::... /~
                ___-==_       _-~ o  \/    |||  \\            _/~~-
        __---~~~.==~||\=_    -_--~/_-~|-   |\\   \\        _/~
    _-~~     .=~    |  \\-_    '-~7  /-   /  ||    \      /
  .~       .~       |   \\ -_    /  /-   /   ||      \   /
 /  ____  /         |     \\ ~-_/  /|- _/   .||       \ /
 |~~    ~~|--~~~~--_ \     ~    /\   /\   /\  =~~        .\
          '         ~-|    * \  ||   ||   || /)     __--~~
                      |-~~*   / ||   ||   ||   _-~
                          *  /  ||   ||   || /~
                         (* \ /--------------\ ~-
                         /// |  |  WINNER  |  |
                             | - - -- - -- - -|\  |
                 /\          |                | ) \
                  \          |- - -  - -  - - | _--~|
                   \\        |                |//.-~~-\
                    \X__x___ ==================*
                     ~---,____--~~*
''')
	elif choice3 == "blue":
			print("You enter the room full of beasts.Game Over")
	else:
			print("You choose the door that doesn't exist.GameOver")
	
else:
	print("You fell into Hole.Game Over")	