

class Macro():
    pass


class Wall(Macro):
    
    def render(self):
        yield Fill(self.x1, self.y1, self.z1, )

