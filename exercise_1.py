
# Exercise 1
class House:
    
    def __init__(self, wall_area):
        self.wall_area = wall_area
        self.buckets = self.wall_area/2.5

    def paint_needed(self):
        return self.wall_area * 2.5

class Paint:

    def __init__(self, buckets, color):
        self.buckets = buckets
        self.color = color

    def total_price(self):
        if self.color == "white":
            price_bucket = 1.99
        else: 
            price_bucket = 2.19
               
        return self.buckets * price_bucket


class DiscountedPaint(Paint):
    def discounted_price(self, discount_percentage):
        price = self.total_price()
        discount = price * discount_percentage / 100
        return price - discount
   

my_wall = House(10)
my_wall.paint_needed()

my_paint = DiscountedPaint(my_wall.buckets, "white")
my_paint.total_price()

my_paint.discounted_price(10)









# ----------------------------------
#Exercise 2

class Point:

    def __init__(self, x, y):
        print("Hey, I am __init__!")
        self.x = x
        self.y = y
    
    def falls_in_rectangle(self, lowleft, upright):
        print("I am ordinary!")
        if lowleft[0] < self.x < upright[0]\
            and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False

    def distance_from_point(self, point):
        distance = ((self.x - point.x)**2 + (self.y - point.y)**2)**(0.5)
        return distance

point1 = Point(1,1)  
point2 = Point(2,2)

point1.distance_from_point(point2)
