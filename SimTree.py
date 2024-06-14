import background
import birch
import picture
import lightning

def season_step(season_counter):
    season_counter += 1
    if season_counter >= 5:
        season_counter = 1
    if season_counter == 1:
        season = "spring"
    elif season_counter == 2:
        season = "summer"
    elif season_counter == 3:
        season = "fall"
    else:
        season = "winter"
    return [season_counter, season]

firstloop=1
while firstloop==1:
    size = (input("How many pixels would you like the square display to be? "))
    try:
        testint = 100/int(size)
    except:
        print("please type in a number greater than zero and less than infinity")
    else:
        firstloop = 0
        size = int(size)
picture.new_picture(size, size)
picture.set_font("Roboto-Black.ttf", 60)
picture.draw_text(size//2, size//2, "Welcome to SimTree")
picture.save_picture("SimTree.png")
input("To access the program's display, open SimTree.png. Continue by pressing enter.")
species = input("What species would you like your tree to be? ")
if species != "Birch" and species != "birch":
    print("Unfortunately this program can only create birch trees")
season = "summer"
season_counter = 2
day_counter = 0
background.draw_background(size, season)
picture.save_picture("SimTree.png")
input("On one bright summer day...")
tree = birch.Birch(size)
picture.save_picture("SimTree.png")
input("A beautiful birch tree was born")

lightning_struck = 0
loop_interface = 1
while loop_interface == 1:
    print (" 1: I do not like my tree \n 2: I would like to move forward by a day \n 3: I would like to move forward by a season \n 4: I would like to strike my tree down with lightning \n 5: I would like to see a special message from the developer \n 6: I have had enough of SimTree")
    request = (input("Type a number here: "))
    if request == "1":
        if lightning_struck == 0:
            input("too bad")
        if lightning_struck == 1:
            input("what tree?")
    elif request == "2":
        day_counter+=1
        if day_counter == 90:
            return_data = season_step(season_counter)
            season_counter = return_data[0]
            season = return_data[1]
            day_counter = 0
        background.draw_background(size, season)
        if lightning_struck == 0:
            tree.reconstruct(season)
        picture.save_picture("SimTree.png")
        if lightning_struck == 0:
            input("One day later, it still stood.")
        else:
            input("One day passed, and the memory of that beautiful birch tree became more distant.")
    elif request == "3":
        
        return_data = season_step(season_counter)
        season_counter = return_data[0]
        season = return_data[1]
        background.draw_background(size, season)
        if lightning_struck == 0:
            tree.reconstruct(season)
        picture.save_picture("SimTree.png")
        if lightning_struck == 0:
            input("One season later, there it stood.")
        else:
            input("One season passed, and the memory of the beautiful birch tree became more distant.")

    elif request == "4":
        
        if lightning_struck == 0:
            lightning_bolt = lightning.lightning_strike(size)
            lightning_struck = 1
            picture.save_picture("SimTree.png")
            input("A sudden bolt of lightning strikes the center of the tree base!")
            background.draw_background(size, season)
            tree.reconstruct(season)
            lightning_bolt.become_flames()
            picture.save_picture("SimTree.png")
            input("First there were flames.")
            lightning_bolt.become_flames()
            picture.save_picture("SimTree.png")
            input("Then flames upon flames.")
            lightning_bolt.become_flames()
            picture.save_picture("SimTree.png")
            input("Then flames upon flames upon flames.")
            lightning_bolt.become_flames()
            picture.save_picture("SimTree.png")
            input("But what was most stiking of all was what came afterwards.")
            background.draw_background(size, season)
            picture.save_picture("SimTree.png")
            input("Silence.")
        else:
            lightning_bolt = lightning.lightning_strike(size)
            picture.save_picture("SimTree.png")
            input("A cruel bolt of lightning struck the flat ground, and finding nothing to destroy, thereafter disappeared.")
            background.draw_background(size, season)
            picture.save_picture("SimTree.png")



    elif request == "6":
        print("BYE BYE")
        loop_interface = 0
    elif request == "5":
        input("Please give me an A+ in this class :)")
    else:
        print("Please type in a number between 1 and 6. It's not that hard.")