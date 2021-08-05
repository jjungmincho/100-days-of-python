print('''
*******************************************************************************
                                 ,ood8888booo,
                              ,od8           8bo,
                           ,od                   bo,
                         ,d8                       8b,
                        ,o                           o,    ,a8b
                       ,8                             8,,od8  8
                       8'                             d8'     8b
                       8                           d8'ba     aP'
                       Y,                       o8'         aP'
                        Y8,                      YaaaP'    ba
                         Y8o                   Y8'         88
                          `Y8               ,8"           `P
                            Y8o        ,d8P'              ba
                       ooood8888888P"""'                  P'
                    ,od                                  8
                 ,dP     o88o                           o'
                ,dP          8                          8
               ,d'   oo       8                       ,8
               $    d$"8      8           Y    Y  o   8
              d    d  d8    od  ""boooooooob   d"" 8   8
              $    8  d   ood' ,   8        b  8   '8  b
              $   $  8  8     d  d8        `b  d    '8  b
               $  $ 8   b    Y  d8          8 ,P     '8  b
               `$$  Yb  b     8b 8b         8 8,      '8  o,
                    `Y  b      8o  $$o      d  b        b   $o
                     8   '$     8$,,$"      $   $o      '$o$$
                      $o$$P"                 $$o$

*******************************************************************************
''')

print("Welcome to RUN.")
print("Your mission is to run away from the wolf.") 

choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".\n').lower()

if choice1 == "right":
  choice2 = input('Now can either "jump" the wall, "turn" around or "lie" down on the ground. Choose one.\n').lower()
  if choice2 =="jump":
    choice3 = input('Finally you see a building to hide. You can either hide inside the "room", "store" or "washroom". Where do you want to go?\n')
    if choice3 == "room":
      print("Oh, no...it's closed. Good bye.")
    elif choice3 == "store":
      print("YES! You are safe now!")
    elif choice3 == "washroom":
      print("Oops. Someone is having the number 2 now. The washroom is full. Game over")
    else:
      print("Not a good idea to go other places. They are all full of wolves already. RIP.")
  else:
    print("Wolves are smart. That will only make them more angry. Game over.")
else:
  print("You were chased by the wolf. RIP.")