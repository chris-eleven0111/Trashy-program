import os
import random

difficulty = {"Easy": 1, "Normal": 2, "Hard": 3, "Extreme": 4}
diff_now = 0
diff_input = 0
rand_num = 0
num_answer = 0
keep_going = True
limit = 15

while keep_going == True:
    os.system("cls")
    print("\n\t* Warning : I used translator in some of the sentence and words, So the grammar can be incorrect! *\n\tNormal Number Game\n\tChoose a difficulty!\n")
    print("\tEasy(1~50), Normal(1~100), Hard(1~250), Extreme(1~500)\n")
    diff_input = input("\t>>> ")
    print("\n\tSelected Difficulty :", diff_input + ".")
    diff_now = difficulty[diff_input]
    os.system("pause")

    if diff_now == 1:
        os.system("cls")
        rand_num = random.randrange(1,51)
        print("Chance :", limit, "times remaining\n")
        print("Match the numbers! (UP/DOWN)")
        while num_answer != rand_num:
            num_answer = int(input("\n\t>>> "))
            if num_answer > 50:
                os.system("cls")
                print("Ouch, So many numbers! (50+) - -2 chances")
                limit -= 2
                print("Chance :", limit, "times remaining\n")
            elif num_answer > rand_num:
                os.system("cls")
                print("DOWN!")
                limit -= 1
                print("Chance :", limit, "times remaining\n")
            elif num_answer < rand_num:
                os.system("cls")
                print("UP!")
                limit -= 1
                print("Chance :", limit, "times remaining\n")
            else:
                break
        os.system("cls")
        print("\n\tCongratulations! You matched the numbers correctly!\n\t")
        repeat_input = input("Will you continue? (Yes/No)\n\t>>> ")
        if repeat_input == "No":
            keep_going = False
            break
        else:
            limit = 15
    elif diff_now == 2:
        os.system("cls")
        rand_num = random.randrange(1,101)
        print("Chance :", limit, "times remaining\n")
        print("Match the numbers! (UP/DOWN)")
        while num_answer != rand_num:
            num_answer = int(input("\n\t>>> "))
            if num_answer > 50:
                os.system("cls")
                print("Ouch, So many numbers! (100+) - -2 chances")
                limit -= 2
                print("Chance :", limit, "times remaining\n")
            elif num_answer > rand_num:
                os.system("cls")
                print("DOWN!")
                limit -= 1
                print("Chance :", limit, "times remaining\n")
            elif num_answer < rand_num:
                os.system("cls")
                print("UP!")
                limit -= 1
                print("Chance :", limit, "times remaining\n")
            else:
                break
        os.system("cls")
        print("\n\tCongratulations! You matched the numbers correctly!\n\t")
        repeat_input = input("Will you continue? (Yes/No)\n\t>>> ")
        if repeat_input == "No":
            keep_going = False
            break
        else:
            limit = 15
    elif diff_now == 3:
        limit -= 1
        os.system("cls")
        rand_num = random.randrange(1,251)
        print("Chance :", limit, "times remaining (Hard Difficulty - -1 chance)\n")
        print("Match the numbers! (UP/DOWN)")
        while num_answer != rand_num:
            num_answer = int(input("\n\t>>> "))
            if num_answer > 50:
                os.system("cls")
                print("Ouch, So many numbers! (250+) - -2 chances")
                limit -= 2
                print("Chance :", limit, "times remaining\n")
            elif num_answer > rand_num:
                os.system("cls")
                print("DOWN!")
                limit -= 1
                print("Chance :", limit, "times remaining\n")
            elif num_answer < rand_num:
                os.system("cls")
                print("UP!")
                limit -= 1
                print("Chance :", limit, "times remaining\n")
            else:
                break
        os.system("cls")
        print("\n\tCongratulations! You matched the numbers correctly!\n\t")
        repeat_input = input("Will you continue? (Yes/No)\n\t>>> ")
        if repeat_input == "No":
            keep_going = False
            break
        else:
            limit = 15
            print("going ahead...")
    elif diff_now == 4:
        limit -= 2
        os.system("cls")
        rand_num = random.randrange(1,501)
        print("Chance :", limit, "times remaining (Extreme Difficulty - -2 chances)\n")
        print("Match the numbers! (UP/DOWN)")
        while num_answer != rand_num:
            num_answer = int(input("\n\t>>> "))
            if num_answer > 50:
                os.system("cls")
                print("Ouch, So many numbers! (500+) - -2 chances")
                limit -= 2
                print("Chance :", limit, "times remaining\n")
            elif num_answer > rand_num:
                os.system("cls")
                print("DOWN!")
                limit -= 1
                print("Chance :", limit, "times remaining\n")
            elif num_answer < rand_num:
                os.system("cls")
                print("UP!")
                limit -= 1
                print("Chance :", limit, "times remaining\n")
            else:
                break
        os.system("cls")
        print("\n\tCongratulations! You matched the numbers correctly!\n\t")
        repeat_input = input("\tWill you continue? (Yes/No)\n\t>>> ")
        if repeat_input == "No":
            keep_going = False
            break
        else:
            limit = 15
            
        # I think I am absolutely genius!!!!!!