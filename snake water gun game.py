def num1():
    num_of_play = 1
    computer_point = 0
    human_point = 0
    print("Welcome to the Snake, Water, Gun Game\n")
    print("3 times is more then enough to find who is best\n")
    while (num_of_play <= 3):
        play_num = int(input(" type 1 for Snake \n type 2 for Water \n type 3 for Gun \n"))
        if play_num == 1:
            print("you choose :- Snake\n")
        elif play_num == 2:
            print("you choose :- Water\n")
        elif play_num == 3:
            print("you choose :- Gun\n")
        else:
            print("you choose wrong number refresh and try again")
        import random
        list = ["Snake", "Water", "Gun"]
        _random = random.choice(list)
        if _random == play_num:
            print("tie both get 0 point")
        elif play_num == 1 and _random == "Gun":
            computer_point = computer_point+1
            print("user defeat computer wins")
            print("computer wins a point")
        elif play_num == 1 and _random == "Water":
            human_point = human_point+1
            print("user wins computer defeat")
            print("user wins a point")
        elif play_num == 2 and _random == "Gun":
            human_point = human_point + 1
            print("user wins computer defeat")
            print("user wins a point")
        elif play_num == 2 and _random == "Snake":
            computer_point = computer_point + 1
            print("user defeat computer wins")
            print("computer wins a point")
        elif play_num == 3 and _random == "Water":
            computer_point = computer_point + 1
            print("user defeat computer wins")
            print("computer wins a point")
        elif play_num == 3 and _random == "Snake":
            human_point = human_point + 1
            print("user wins computer defeat")
            print("user wins a point")
        else:
            print("wrong variable refresh and play again ")
        print(3 - num_of_play, "num. of times you left")
        num_of_play = num_of_play + 1
    if (num_of_play > 3):
        print("You finish your three chances")
    if computer_point > human_point:
        print("Computer wins and you loose")

    if computer_point < human_point:
        print("you win and computer loose")
    again()
def again():
    cal_again = input('''
    do you want to play again y for Yes and 
    N for noo
    ''')
    if cal_again == "y":
        num1()
    elif cal_again == "n":
        print("see you later")
    else:
        again()
num1()