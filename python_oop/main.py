class People:
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s says: my name is %s and I'm %d years old." %(
            self.name, self.name, self.age))


class Worker(People):
    def __init__(self, n, a, g, h, w):
        People.__init__(self, n, a, w)
        self.gender = g
        self.__height = h

    def speak(self):
        print("%s says: my name is %s and I'm %d years old, I'm a %s." %(
              self.name, self.name, self.age, self.gender))


class Homosex:
    def __init__(self, n, a, gender: str = "male", grade: int = 1):
        self.name = n
        self.age = a
        self.gender = gender
        self.grade = grade

    def speak(self):
        print("%s says: my name is %s, I'm a %s and I'm as gay as fuck." %(
              self.name, self.name, self.gender))


class GayWorker(Worker, Homosex):
    name = ""
    def __init__(self, n, a, g, h, w):
        Worker.__init__(self, n, a, g, h, w)
        Homosex.__init__(self, n, g, a)
        self.name = n
        
        print(self.__dict__)

    def speak(self):
        print("%s says: I'm a %d year-old %s and I'm as gay as fuck." %(
            self.name, self.age, self.gender))



if __name__ == "__main__":
    #x = People("Mike", 23, 70)
    #y = Worker("Jasmine", 25, "male", 180, 65)
    #Worker.speak(y)
    z = GayWorker("Tomas", 24, "male", 180, 65)
    z.speak()


