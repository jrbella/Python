Pokemon_type = {"Grass", "Water", "Fire"}




class Pokemon:
    num_of_moves =  4  #This is a class attribute
    
    #This is similar to memberwise initializer
    def __init__(self, name, type_1,
                    type_2):
                        
        #instance attribute
        #This is the instantiation of intializer (The values are assigned here)
        self.name = name
        self.type_1 = type_1
        self.type_2 = type_2
        
        
        

        