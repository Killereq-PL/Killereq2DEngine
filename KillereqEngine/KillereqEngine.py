import tkinter
import _thread

# TODO: Fix
class KillereqCanvas(tkinter.Canvas): # modified tkinter canvas
    def __init__(self, CanvasSize: tuple, bgcolor="white"):
        self.Wsize = CanvasSize
        self.configure(bg=bgcolor, width=CanvasSize[0], height=CanvasSize[1])

    def DrawImage(self, image, position):
        return self.create_image(position[0], position[1], anchor=tkinter.NE, image=image)
    
    def WindowSize(self, NewSize: tuple):
        self.Wsize = NewSize

    def WindowSize(self) -> tuple:
        return self.Wsize

class KillereqEngine: # main engine
    def __init__(self, WindowSize=(800, 600), BackgroundColor="white", ScreenName="KillereqEngine"):
        self.canvas = KillereqCanvas(WindowSize, BackgroundColor)
        self.root = tkinter.Tk(screenName=ScreenName)
        self.canvas.pack()

    def loop_thread(self):
        self.root.mainloop()
    
    def loop(self):
        _thread.start_new_thread(self.loop_thread)

if __name__ == "__main__":
    Screen = KillereqEngine(WindowSize=(500, 500))
    print("KillereqEngine")
    Screen.loop()