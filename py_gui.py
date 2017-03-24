import Tkinter as tk

class RootWindow:
    def __init__(self, master):
        self.master = master # self.master is self.root
        self.f1 = tk.Frame(self.master)
        self.f2 = tk.Frame(self.master)
        # f3 = tk.Frame(self.master)
        # f4 = tk.Frame(self.master)

        # for frame in (f1, f2, f3, f4):
        #     frame.grid(row=0, column=0, sticky='news')

        # self.frames = {}
        # self.frames["frame1"] = f1
        # self.frames["frame2"] = f2
        # self.frames["frame3"] = f3
        # self.frames["frame4"] = f4

        # # in order to pass information into button callback function (e.g. "frame1"), lambda: is required
        # self.button1 = tk.Button(f1, text="go to frame 2", command=lambda:self.new_frame("frame2")).pack()
        # self.button2 = tk.Button(f2, text="go to frame 3", command=lambda:self.new_frame("frame3")).pack()
        # self.button3 = tk.Button(f3, text="go to frame 4", command=lambda:self.new_frame("frame4")).pack()
        # self.button4 = tk.Button(f4, text="go to frame 1", command=lambda:self.new_frame("frame1")).pack()
        # self.new_frame("PageOne")

        PageOne(self.f1, self)
        PageTwo(self.f2, self)
    def new_frame(self, frame):
        frame.tkraise()

class PageOne:
    def __init__(self, master, controller):
        master.grid(row=0, column=0, sticky='news')
        self.button = tk.Button(master, text="go to frame 2", command=lambda:controller.new_frame(controller.f2)).pack()

class PageTwo:
    def __init__(self, master, controller):
        master.grid(row=0, column=0, sticky='news')
        self.button = tk.Button(master, text="go to frame 1", command=lambda:controller.new_frame(controller.f1)).pack()

def main(): 
    root = tk.Tk()
    app = RootWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()