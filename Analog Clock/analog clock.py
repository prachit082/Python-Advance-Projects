import tkinter as tk
import math
import time

class ClockAnimation(tk.Tk):
        def __init__(self):
            super().__init__()
            self.x = 150  # Center Point x
            self.y = 150  # Center Point y
            self.length = 50  # Stick Length
            self.sticks = []
            self.create_canvas_for_shapes()
            self.creating_background_()
            self.creating_sticks()
            self.after(1000, self.update_class)  # Schedule the first update

        def create_canvas_for_shapes(self):
            self.canvas = tk.Canvas(self, bg='black')
            self.canvas.pack(expand=True, fill='both')
            return

        def creating_background_(self):
            self.image = tk.PhotoImage(file='clock.gif')
            self.canvas.create_image(150, 150, image=self.image)
            return

        def creating_sticks(self):
            for i in range(3):
                store = self.canvas.create_line(self.x, self.y, self.x + self.length, self.y + self.length, width=2, fill='red')
                self.sticks.append(store)
            return

        def update_class(self):
            now = time.localtime()
            t = time.strptime(str(now.tm_hour), "%H")
            hour = int(time.strftime("%I", t)) * 5
            now = (hour, now.tm_min, now.tm_sec)
            for n, i in enumerate(now):
                x, y = self.canvas.coords(self.sticks[n])[0:2]
                cr = [x, y]
                cr.append(self.length * math.cos(math.radians(i * 6) - math.radians(90)) + self.x)
                cr.append(self.length * math.sin(math.radians(i * 6) - math.radians(90)) + self.y)
                self.canvas.coords(self.sticks[n], tuple(cr))
            self.after(1000, self.update_class)  # Schedule the next update

if __name__ == '__main__':
        root = ClockAnimation()
        root.mainloop()
