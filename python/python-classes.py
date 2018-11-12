# creating python classes
class Polygon:
    def __init__(self, sides, shape = ""):
        '''
            @brief: constructor
        '''
        self.shape = shape
        self.count = sides
        self.side_lengths = [0 for i in range(self.count)]
   
    #defining a fuction in python - This is a getter
    def print_sides(self):
        print 'Sides of the shape are:'
        for i in range(self.count):
            print('Side:', i+1, 'is of length :', self.side_lengths[i])

    #defining a fuction in python - This is a setter
    def update_sides(self):
        for i in range(self.count) :
            self.length = raw_input("Enter the length for side")
            self.side_lengths[i] = self.length

# creating the python object
obj = Polygon(3,"Triangle")
print obj.count
print obj.shape
print obj.update_sides()
print obj.print_sides()

#modifying the class member variables
obj.count = 4
obj.shape = "Test shape"
print obj.count
print obj.shape
