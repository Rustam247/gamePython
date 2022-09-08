def convert():
    print(" ")
    print (">>------> Programmer Maniacs<------<<")
    print(" ")
    print(" ")
    print("################################################")
    print("           WELCOM TO PROGRAMMER MANIACS         ")
    print("################################################")
    print(" ")
    print("Do you have enough knowledge to play this game?")
    print(" ")
    print("                    Main Menu                   ")
    print("++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+      Enter (s) to start Programmer Maniacs   +")
    print("+        Enter (d) to start Dunguon Dragon     +")
    print("+              Enter (e) to exit               +")
    print("+              Enter (c) to credits            +")
    print("++++++++++++++++++++++++++++++++++++++++++++++++")
    print(" ")
    print(" ")
    main = input("What whould you like to do?")
    if main.lower() == 'e':
        print(" ")
        print ("Did you give up so easily?")
        exit()

    elif main.lower() == 'c':
        print(" ")
        print ("This game was created by:")
        print(" ")
        print("Iraj Ahang")
        print("Jack Daniels")
        print("Aaron Cadette")
        exit()
    elif main.lower() == "s":
        print(" ")
        print ("Lets start")
        print(" ")
        print("You ended up in an unknown room, you were kidnapped by programmer maniacs.")
        print(" ")
        print("You have nothing with you except your knowledge.")
        print(" ")
        print("Knowledge is light, light is the way out.")
        print(" ")
        print('You see a door, but to open that door you need to answer a question.')
        print(" ")
        print("--==*==--What is valuable?--==*==--")
        print("1.Statements that performs a specific task.")
        print("2. Characters or a number.")
        print("3. Repeating something over and over")
        print("4. Used to iterate over a block of code")
        print(" ")
        print(" ")
    else:
        
        print("Wrong, game over")
        exit()

        
    ans1 = input()
    if ans1 == '2':
        print(" ")
        print('~~*~~Your answer was correct, you move on.~~*~~')
        print(" ")
    else:
        print(" ")
        print ("You're wrong, you need to learn more programming. Game Over")
        print(" ")
        exit()
    if ans1 == '2':
        print('You go up the stairs and see 3 doors:')
        print(" ")
        print('(A) On the door number A it is written, then what crawls and stings.')
        print(" ")
        print('(B) On the door number B it is written, then you can die if your knowledge is not enough. ')
        print(" ")
        print('(C) On the door number C it is written, then what infects and kills.')
        print(" ")
        print(" ")
        room2 = input("What is your answer?")
        if room2.lower() == 'b':
            print(" ")
            print("--==*==-- What is function?--==*==--")
            print("1.Used to iterate over a block of code.")
            print("2. Statements that performs a specific task.")
            print("3. Characters or a number.")
            print("4. repeating something over and over")
            print(" ")
            print(" ")
        if room2.lower() == 'a':
            print('You entered and the door slammed behind you and closed,\n there is a huge number of snakes in front of you and they all attack you,\n you were bitten - you died.')
            exit()
        elif room2.lower() =='c':
            print ("You entered and the door slammed behind you and closed,\n there are a huge number of zombies in front of you,\n you were bitten - you became one of them. Game over")
            exit()    
    ans2 = input()
    if ans2 == '2':
        print ("~~*~~Your answer was correct, you move on.~~*~~")
        print(" ")
    else: 
        print ("You're wrong, you need to learn more programming. Game Over")
        exit()

    if ans2 == "2":
        print ("When you entered the next room you noticed 3 more doors, what will you choose now?")
        print(" ")
        print ("(A) On the door number A it is written, are you sure of your knowledge? If yes, here is your question.")
        print(" ")
        print ("(B) On the door number B it is written, you will enter and you will live forever.")
        print(" ")
        print ("(C) On the door number C it is written, if you enter you will become strong as a stone.")
        print(" ")
        room3 = input ("What is your answer?")
        if room3.lower() == 'a':
            print(" ")
            print ("--==*==-- What is loop?--==*==-- ")
            print("1.Repeating something over and over.")
            print("2. Statements that performs a specific task")
            print("3. Characters or a number.")
            print("4. Used to iterate over a block of code")
            print(" ")
            print(" ")
        elif room3.lower() == 'b':
            print ("You entered the room where you saw a vampire,\n he quickly approached you and bit you,\n now you are a vampire and now you will live here forever.")
            exit()
        elif room3.lower() == 'c':
            print(" ")
            print ("You entered the room where you saw the needle, you accidentally touched it and you started to turn into stone.")
            exit()
            
    ans3 = input()
    if ans3 == "1":
        print(" ")
        print ("~~*~~Your answer was correct, you move on.~~*~~")
    else:
        print("You're wrong, you need to learn more programming. Game Over")
        exit()

    if ans3 == "1":
        print(" ")
        print ("You pass further where you see 2 rooms.")
        print ("(A) Above the door number A you see the inscription, if you enter, you will meet magic and love.")
        print(" ")
        print ("(B) Above the door number B you see the inscription, how strong are you in knowledge,")
        room4 = input()
        if room4.lower() == 'a':
            print(" ")
            print ("You went into a room where an old witch meets you,\n she uses magic on you and you fall in love with her,\n forever serving her.")
            exit()
        elif room4.lower() == 'b':
            print ("--==*==-- What is while loop?--==*==--")
            print("1.Used to iterate over a block of code")
            print("2.Repeating something over and over.")
            print("3. Statements that performs a specific task.")
            print("4.Characters or a number")

    ans4 = input()
    if ans4 == "1":
        print(" ")
        print("~~*~~Your answer was correct, you move on.~~*~~")
        print(" ")
    else:
        print("You're wrong, you need to learn more programming. Game Over")
        exit()

    if ans4 == "1":
        print(" ")
        print (" You go further and see a huge door to freedom,\n but you notice that in order to open the door you need to press the code,\n you start looking for clues and you see what is written above the doors,\n A programmer is a person who has developed logic and memory,\n remember your answers and use the logic that would open the door")
        print(" ")
        print ("Remember your answers to open these doors!")
        print(" ")
    escape_code = int(input("Enter 4-digit code: "))

    while len(str(abs(escape_code))) != 4:
        escape_code = int(input("Enter 4-digit code: "))

    if escape_code == 2211:
        print(" ")
        print("You enter the code into the keypad and watch as the doors swing open to the outside.")
        print(" ")
        print("Congratulations! You are free!")
        print("You now know that the key to open any door in this world lies in programming!")
        print(" ")
        print(" ")
        print(" ")
        print("THE END!")
        print(" ")
        print(" ")
        print(" ")
    else:
        print("You enter the code and hear a sound as the keypad powers off.")
        print(" ")
        print("With no way to open the doors in front of you, they remain closed forever, trapping you in the building.")
        print(" ")
        print("GAME OVER!")
        exit()
convert()
while True:
    flag = input('One more time? [Y/N]: ')

    if flag.lower() == 'y':
        convert()
    else:
        break