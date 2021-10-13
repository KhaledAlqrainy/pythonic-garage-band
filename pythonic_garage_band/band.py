class Band:
    
    list = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.list.append(self.name)

    def play_solos(self):
        solo = []
        for i in self.members:
            solo.append(i.play_solo())
        return solo

    def __str__(self):
        return f"The band name is {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    @classmethod
    def to_list(cls):
        return cls.list

        #########################

class Musician:

    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name : {self.name}"    

    def __str__(self):
        return f"My name is {self.name} , and I play {self.instrument}"


########## Musician Types ###########

class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, "guitar")  

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return "face melting guitar solo"

class Bassist(Musician):
    def __init__(self, name):    
        super().__init__(name, "bass")

    def get_instrument(self):
        return "bass"
    
    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, "drums")

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"