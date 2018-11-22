import random
import threading
import datetime

print("It is late in the evening and you wake up coughing and by the shrieking sound of your smoke detector you "
          "\nopen your eyes. Through the flashing LED light of your smoke detector you see your ceiling engulfed in "
          "\na black sea of smoke raging around like a storm. In a sudden spike of adrenaline you throw your blanket "
          "\naside, Rudi! Last you checked the cat was sleeping in one of the U haul boxes. You crawl out of bed "
          "\nremembering to stay low, all those years of training in fire-safety did help have paid off in a way. As"
          "\nyou make your way through your two room condo, you see the kitchen lit up like the gates of hell. To your"
          "\nright, you see the boxes. You realise there are only 10 seconds left and have to hurry.")

number_of_searches = 0
not_found_cat = True
cat_trace = []
box_containing_cat = random.randint(1, 5)
cat_trace.append(box_containing_cat)

print("Press 'enter' to start!")
start = input()
if start:
    print("Let's do this!")

t_start = datetime.datetime.now()
t_limit = datetime.timedelta(seconds=5)

while not_found_cat == True:
    print("Which box do you go through?")
    user_input = int(input())
    between_box_list = [-1, 1]
    number_of_searches += 1
    print(box_containing_cat)
    if user_input != box_containing_cat:
        print("You see a shadow flying by and one of the boxes moves.")
        if (datetime.datetime.now() - t_start) > t_limit:
            not_found_cat = False
            print("You feel light in the head and pass out. You are burned alive. Rudi was waiting outside and will be"
                  " taken to an animal shelter.")
        elif box_containing_cat == 1:
            box_containing_cat = box_containing_cat + 1
            cat_trace.append(box_containing_cat)
        elif box_containing_cat == 2:
            box_containing_cat = box_containing_cat + random.choice(between_box_list)
            cat_trace.append(box_containing_cat)
        elif box_containing_cat == 3:
            box_containing_cat = box_containing_cat + random.choice(between_box_list)
            cat_trace.append(box_containing_cat)
        elif box_containing_cat == 4:
            box_containing_cat = box_containing_cat + random.choice(between_box_list)
            cat_trace.append(box_containing_cat)
        elif box_containing_cat == 5:
            box_containing_cat = box_containing_cat - 1
            cat_trace.append(box_containing_cat)
    else:
        print('Congratulations!' "\nYou found the cat!" +
              "\nDon't be that irresponsible owner again!"
              "\nWith Rudi in your arms you dash to the front door, into safety.")
        not_found_cat = False
        print("You looked for your cat: ", number_of_searches, " number of times!")
        print("Rudi meows you it jumped to the following boxes: " + str(cat_trace))

