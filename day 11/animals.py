class Animal:
    noise="rrr"
    color="red"
    def make_noise(self): # this
        print(f"{self.noise}")
 
    def set_noise(self,new_noise):
        self.noise=new_noise
    def get_noise(self):
        return self.noise
    def set_noise(self,new_noise):
        self.new_noise=new_noise
        return self.noise
    def get_color(self):
        return self.color
    def set_color(self,new_color):
        self.new_noise=new_color
        return self.color      

class Wolf(Animal):
    noise="reeeee" 

        
class Babywolf(Wolf):  
    color="yellow" 
