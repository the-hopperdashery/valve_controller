import datetime
from tkinter import *
import tkinter as ttk

LIGHTS = [
    {
        "display_name": "One",
        "default_on": "07:00",
        "default_off": "22:00",
    },
    {
        "display_name": "Two",
        "default_on": "07:00",
        "default_off": "22:00",
    },
    {
        "display_name": "Three",
        "default_on": "07:00",
        "default_off": "22:00",
    },
]

LIGHT_LABELS = [
    "Name",
    "On Time",
    "Off Time",
]


class ValveController:
    def __init__(self):
        self.lights = []
        self.running = False
        self.currently_running_valve_index = None

    def add_valve(self, container, valve, valve_index):
        # valve index from MainWindow is 1-indexed because of the labels column
        # also helps with some reasoning
        self.lights.append(Light(container, valve, valve_index))

class Light:
    def __init__(self, container, valve, valve_index):
        self.container = container
        self.valve = valve
        self.valve_index = valve_index

        self.display_name = valve["display_name"]
        self.on_minute = 0
        self.off_minute = 0
        self.running = False

        self.label = ttk.Label(container, text=self.display_name)
        self.label.grid(column=self.valve_index, row=1)

        self.on_time = ttk.Entry(container, width=10)
        self.on_time.insert(0, valve["default_on"])
        self.on_time.grid(column=self.valve_index, row=2)

        self.off_time = ttk.Entry(container, width=10)
        self.off_time.insert(0, valve["default_off"])
        self.off_time.grid(column=self.valve_index, row=3)

        self.start_button = ttk.Button(
            container, text="Start", command=self.turn_on)
        self.start_button.grid(column=self.valve_index, row=4)

        self.stop_button = ttk.Button(
            container, text="Stop", command=self.turn_off)
        self.stop_button.grid(column=self.valve_index, row=5)
        self.update_timer()


    def turn_on(self):
        print(f"Turning on light {self.display_name}")
        self.running = True

        on_parts = self.on_time.get()
        self.on_minute = int(on_parts[0]) * 60 + int(on_parts[1])
        
        off_parts = self.off_time.get()
        self.off_minute = int(off_parts[0]) * 60 + int(off_parts[1])

    def update_timer(self):
        if self.running:
            dt = datetime.datetime.now()
            current_minute = dt.hour * 60 + dt.minute


            if current_minute > self.off_minute and self.running:
                self.turn_off()
            
            if current_minute > self.on_minute and not self.running:
                self.turn_on()

            # this is calls back to the container to update the UI
            self.container.after(1000, self.update_timer)

    def turn_off(self):
        self.running = False
        print(f"Turning off light {self.display_name}")

class LightPage:
    def __init__(self, master):
        valve_frame = ttk.Frame(master)
        valve_frame.pack()

        bottom_frame = ttk.Frame(master)
        bottom_frame.pack(side=ttk.BOTTOM)

        for idx, name in enumerate(LIGHT_LABELS):
            self.label = ttk.Label(valve_frame, text=name)
            self.label.grid(column=0, row=idx + 1)

        valve_controller = ValveController()

        for idx, valve in enumerate(LIGHTS):
            valve_controller.add_valve(valve_frame, valve, idx + 1)

        self.close_button = ttk.Button(
            bottom_frame, text="Exit", command=master.quit)
        self.close_button.pack()

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Hopperdashery Valve Controller")
        ValvePage(master)


# root = ttk.Tk()
# my_gui = MainWindow(root)
# root.mainloop()
