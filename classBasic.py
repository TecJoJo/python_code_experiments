class Programmer:
    def __init__(self,name,experience,education,location):
        self.name = name
        self.experience = experience
        self.education = education
        self.location =location
    
    def __str__(self):
        return f"{self.name} project"

    def coding(self):
        print(f"{self.name} starts coding in {self.location}")



class FrontEndDeveloper(Programmer):
    def __init__(self,name,exeperience,education,location,stack):
        super().__init__(name,exeperience,education,location)
        self.techStack = stack
        
    
    def buildWebsite(self):
        print(f"{self.name}, a {self.experience} programmer starts to build website with {self.techStack} ")

    def coding(self):
        # print(f"{self.name} coding with {self.techStack}")
        print("Call parent class method coding() next ")
        super().coding()

yao = FrontEndDeveloper("Yao","intern","bachelor","Finland","React.js")

# yao.buildWebsite()
yao.coding()

