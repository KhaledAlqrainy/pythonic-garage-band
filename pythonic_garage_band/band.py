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

    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        pass   

    def __str__(self):
        pass


########## Musician Types ###########

class Guitarist(Musician):

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}" 

    def get_instrument(self):
        return 'guitar'

    def play_solo(self):
        return "face melting guitar solo"

class Bassist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return "bass"
    
    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):

    def __str__(self):
        return f"My name is {self.name} and I play drums"
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"

if __name__ == "__main__":
    Joan = Guitarist('Joan Jett')
    Sheila = Drummer('Sheila E.')
    Meshell = Bassist('Meshell Ndegeocello')

    print(Joan)
    print(Sheila)
    print(Meshell)