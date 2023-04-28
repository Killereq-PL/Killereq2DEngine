import turtle

class KillereqEngine(turtle._Screen):
    def __init__(self, WindowSize: tuple, BackgroundColor="white"):
        self.tr = turtle.Turtle()
        self.setup(WindowSize[0], WindowSize[1])
        self.bgcolor(BackgroundColor)
        self.mainloop()

    def DrawImage(self, image, position):
        pass

if __name__ == "__main__":
    Screen = KillereqEngine(WindowSize=(500, 500))
    print("KillereqEngine")