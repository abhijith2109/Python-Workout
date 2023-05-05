class Car:
    def parts(self,model,year):
        self.model=model
        self.year=year
        print(self.model,self.year)

c1=Car()
c1.parts("Honda",2005)
