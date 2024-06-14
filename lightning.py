import picture
import random

class lightning_strike:
    def __init__(self, size):
        picture.set_fill_color("darkgoldenrod")
        picture.set_outline_color("lightsteelblue")
        self.size = size
        self.rod_size = (9*size)//10
        self.rod_width = random.randint(size//20, size//10)
        #height calculator of all three components
        self.height = random.randint(self.rod_size//6, (2*self.rod_size)//3)
        remainder = self.rod_size-self.height
        self.height_2 = random.randint(0, remainder)
        self.height_3 = remainder - self.height_2
        #skew calculation
        total_skew = size // 2
        proportion_1 = self.height/self.rod_size
        proportion_2 = self.height_2/self.rod_size
        proportion_3 = self.height_3/self.rod_size
        skew_1 = total_skew * proportion_1
        skew_2 = total_skew * proportion_2
        skew_3 = total_skew * proportion_3
        self.draw_triangle(total_skew, self.rod_size, self.height, self.rod_width, skew_1)
        #these functions are returning values that im not using; I will rethink the utility of this decision when I look back at this
        self.draw_quadrilateral((total_skew+skew_1)+self.rod_width//2, self.rod_size-self.height, self.height_2, self.rod_width, skew_2)
        self.draw_quadrilateral(((total_skew+skew_1)+self.rod_width//2)+skew_2+self.rod_width//2, self.rod_size-self.height-self.height_2, self.height_3, self.rod_width, skew_3)
    
    def draw_quadrilateral(self, x_1, y_1, height, width, skew):
        x_2 = x_1+width
        y_2 = y_1-height
        picture.draw_filled_polygon([(x_1, y_1), (x_2, y_1), (x_2+skew, y_2), (x_1+skew, y_2)])
        return_value = [x_1+skew, y_2]
        return return_value
    
    def draw_triangle(self, x_1, y_1, height, width, skew):
        x_2 = x_1+width
        y_2 = y_1-height
        picture.draw_filled_polygon([(x_1, y_1), (x_2+skew, y_2), (x_1+skew, y_2)])
        return_value = [x_1+skew, y_2]
        return return_value
    
    def become_flames(self):
        
        flame_count = random.randint(5, 10)
        for flame in range(flame_count):
            color = random.randint(1,2)
            if color == 1:
                picture.set_fill_color("red")
                picture.set_outline_color("red")
            else:
                picture.set_fill_color("orange")
                picture.set_outline_color("orange")
            radius = random.randint(1,self.size//10)
            radius_2 = random.randint(radius//2, radius)
            x_point = random.randint(1, self.size)
            y_point = random.randint(1, self.size)
            flamesize = random.randint(3, 5)
            for miniflame in range (flamesize):
                picture.draw_filled_oval(x_point+random.randint(0, 2*radius//3), y_point+random.randint(0, 2*radius_2//3), radius, radius_2)
            picture.draw_filled_oval(x_point+2*radius//3, y_point, radius, radius_2)