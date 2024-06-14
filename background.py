import picture
import random

def draw_background(size, season):
    picture.new_picture(size, size)
    if season != "summer":
        picture.set_fill_color("lightblue")
    else:
        picture.set_fill_color("deepskyblue")
    picture.draw_filled_square(0, 0, size)
    cloud_count = random.randint(1, 10)
    #The below portion randomly generates clouds in the sky
    for cloud in range(cloud_count):
        picture.set_fill_color("whitesmoke")
        picture.set_outline_color("whitesmoke")
        radius = random.randint(1,size//10)
        radius_2 = random.randint(radius//2, radius)
        x_point = random.randint(1, size)
        y_point = random.randint(1, size)
        cloudsize = random.randint(3, 5)
        for minicloud in range (cloudsize):
            picture.draw_filled_oval(x_point+random.randint(0, 2*radius//3), y_point+random.randint(0, 2*radius_2//3), radius, radius_2)
        picture.draw_filled_oval(x_point+2*radius//3, y_point, radius, radius_2)
    if season == "summer" or season == "spring":
        picture.set_fill_color("green")
        picture.set_outline_color("green")
    elif season == "fall":
        picture.set_fill_color("darkgreen")
        picture.set_outline_color("darkgreen")
    elif season == "winter":
        picture.set_fill_color("white")
        picture.set_outline_color("black")
    picture.draw_filled_square(0,(3*size)//4, size)