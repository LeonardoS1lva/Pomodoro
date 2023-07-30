import tkinter as tk
from tkinter import messagebox
import time

class Pomodoro:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Método Pomodoro")

        self.minutes = 25
        self.seconds = 0
        self.is_break = False
        self.is_running = False
        self.count = 0

        self.time_label = tk.Label(text="25:00", font=("Arial", 50))
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(text="Iniciar", font=("Arial", 20), command=self.start_timer)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(text="Parar", font=("Arial", 20), command=self.stop_timer, state="disabled")
        self.stop_button.pack(pady=10)

        self.root.mainloop()

    def start_timer(self):
        self.is_running = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")

        while self.minutes >= 0 and self.is_running:
            if self.seconds == 0:
                self.minutes -= 1
                self.seconds = 59
            else:
                self.seconds -= 1

            time_left = f"{self.minutes:02d}:{self.seconds:02d}"
            self.time_label.config(text=time_left)
            self.root.update()

            time.sleep(1)

        if self.is_running:
            if self.is_break:
                self.minutes = 25
                self.seconds = 0
                self.is_break = False
                self.count += 1
            else:
                if self.count == 3:
                    self.minutes = 30
                    self.seconds = 0
                else:
                    self.minutes = 5
                    self.seconds = 0

                self.is_break = True

            if self.count < 4:
                messagebox.showinfo("Método Pomodoro", "Pausa de 5 minutos")
            else:
                messagebox.showinfo("Método Pomodoro", "Pausa longa")

            self.time_label.config(text="25:00")
            self.start_timer()

    def stop_timer(self):
        self.is_running = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

if __name__ == "__main__":
    pomodoro = Pomodoro()
