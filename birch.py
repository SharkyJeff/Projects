import picture
import random
import background


class Birch():
    def __init__(self, size):
        self.size = size
        self.height = random.randint(size//2, (3*size)//4)
        self.width = random.randint(size//7, size//5)
        self.branches = []
        self.black_spots = []
        self.leaves = []
        self.season = "summer"
        x_1 = (size//2)-self.width//2
        y_1 = size-(size // 20) 
        skew = random.randint(-(size//40), size//40)
        self.draw_tree(x_1, y_1, self.height, self.width, skew, 0)

    def draw_tree(self, x_1, y_1, height, width, skew, branch_counter):
        if branch_counter >= random.randint(1,4):
            leaf_data = self.draw_branch (x_1, y_1, height, width, skew)
            #leaf drawer
            self.draw_green_leaves(leaf_data, width)
        else:
            branch_counter=int(branch_counter)
            height_of_split = random.randint(height//6, ((branch_counter+1)*height)//5)
            point = self.draw_branch (x_1, y_1, height_of_split, width, skew)
            is_branch = random.randint(0, 1)
            new_height = height-height_of_split
            new_skew = random.randint(-new_height//4, height//4)
            if is_branch == 0:
                self.draw_tree(point[0], point[1], new_height, width, new_skew, branch_counter+1)
            else:
                width_1 = random.randint(width//8, 7*width//8)
                width_2 = width-width_1
                whose_the_tree=random.randint(1, 2)
                newer_height = random.randint(new_height//2, new_height)
                if whose_the_tree == 1:
                    leaf_data = self.draw_branch (point[0], point[1], newer_height, width_1, new_skew)
                    #leaf drawer
                    self.draw_green_leaves(leaf_data, width_1)
                    self.leaves.append([leaf_data, width_1])
                    new_skew = random.randint(new_skew, new_skew+(self.size//(3*(branch_counter+1))))
                    self.draw_tree(point[0]+width_1, point[1], new_height, width_2, new_skew, branch_counter+1)
                else:
                    leaf_data = self.draw_branch(point[0]+width_1, point[1], newer_height, width_2, new_skew)
                    self.draw_green_leaves(leaf_data, width_2)
                    self.leaves.append([leaf_data, width_1])
                    new_skew = random.randint(new_skew-(self.size//4), new_skew)
                    self.draw_tree (point[0], point[1], new_height, width_1, new_skew, branch_counter+1)
    

    def draw_green_leaves(self, return_value, width):
        picture.set_fill_color("forestgreen")
        picture.set_outline_color("forestgreen")
        width = random.randint(width, int(width*1.5))
        self.leaves.append([return_value, width])
        self.draw_circle(return_value, width)
    
    def draw_circle(self, return_value, width):
        picture.draw_filled_circle(return_value[0]+(width//2), return_value[1], width)

    def draw_branch(self, x_1, y_1, height, width, skew):
        picture.set_fill_color("white")
        picture.set_outline_color("white")
        return_value = self.draw_polygon(x_1, y_1, height, width, skew)
        self.branches.append([x_1, y_1, height, width, skew]) #the below portion generates black spots on the birch branches (alliteration unintentional)
        spot_count = int(height//(self.size/10))
        picture.set_fill_color("black")
        picture.set_outline_color("black")
        for spot in range(spot_count):
            spot_height = random.randint(0, self.size//20)
            if spot_height >= height:
                spot_height = height
            spot_y_1 = random.randint((y_1-height+spot_height), y_1)
            skew_at_y = int(((y_1-spot_y_1)/height)*skew)
            spot_width = random.randint(width//3, width)
            spot_x_1 = random.randint(x_1 + skew_at_y, (x_1 + skew_at_y)+(width-spot_width))
            spot_skew = int(skew*(spot_height/height))
            self.draw_polygon(spot_x_1, spot_y_1, spot_height, spot_width, spot_skew)
            self.black_spots.append([spot_x_1, spot_y_1, spot_height, spot_width, spot_skew])
        return return_value

    def draw_polygon(self, x_1, y_1, height, width, skew):
        x_2 = x_1+width
        y_2 = y_1-height
        picture.draw_filled_polygon([(x_1, y_1), (x_2, y_1), (x_2+skew, y_2), (x_1+skew, y_2)])
        return_value = [x_1+skew, y_2]
        return return_value
    
    def reconstruct(self, season):
        picture.set_fill_color("white")
        if season == "winter":
            picture.set_outline_color("black")
        else:
            picture.set_outline_color("white")
        for bababooey in self.branches:
            self.draw_polygon(bababooey[0], bababooey[1], bababooey [2], bababooey [3], bababooey [4])
        picture.set_fill_color("black")
        picture.set_outline_color("black")
        for bababooey in self.black_spots:
            self.draw_polygon(bababooey[0], bababooey[1], bababooey [2], bababooey [3], bababooey [4])
        for bababooey in self.leaves:
            if season == "summer":
                picture.set_fill_color("forestgreen")
                picture.set_outline_color("forestgreen")
                self.draw_circle(bababooey[0], bababooey[1])
            elif season == "fall":
                color = random.randint(1, 4)
                if color == 1:
                    picture.set_fill_color("red")
                    picture.set_outline_color("red")
                elif color == 2:
                    picture.set_fill_color("orange")
                    picture.set_outline_color("orange")
                elif color == 3:
                    picture.set_fill_color("yellow")
                    picture.set_outline_color("yellow")
                else:
                    picture.set_fill_color("yellowgreen")
                self.draw_circle(bababooey[0], random.randint((bababooey[1]//2), bababooey[1]))
            elif season == "spring":
                picture.set_fill_color("yellowgreen")
                picture.set_outline_color("yellowgreen")
                self.draw_circle(bababooey[0], random.randint((bababooey[1]//2), bababooey[1]))


    






def main():
    size = 400
    background.draw_background(size, "spring")
    birch = Birch(size)
    picture.save_picture("SimTree.png")
    print(birch.branches)
    background.draw_background(size, "spring")
    birch.reconstruct("fall")
    picture.save_picture("SimTree.png")


if __name__ == '__main__':
    main()