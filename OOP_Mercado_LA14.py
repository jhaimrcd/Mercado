class Spiderman():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def describeSpiderman(self):
        print(f"{self.name} is {self.age}")
        
class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        self.movieTitle = movieTitle
        super().__init__(name, age)
        
man1 = Tobey("tobey", "37", "No way home")
print(man1.name.upper(), man1.movieTitle)
        
class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        self.movieTitle = movieTitle
        super().__init__(name, age)
man2 = Andrew("andrew", "29", "The Amazing Spider-man")
print(man2.name.upper(), man2.movieTitle)
        
class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        self.movieTitle = movieTitle
        super().__init__(name, age)
        
man3 = Tom("tom", "19", "Homecoming")
print(man3.name.upper(), man3.movieTitle)