"""
    Pomodoro Timer Application

    A GUI-based Pomodoro Timer built using the tkinter module.

    Implements the Pomodoro Technique, a time management method developed
    by Francesco Cirillo in the late 1980s. The technique breaks work into
    focused intervals (typically 25 minutes) separated by short breaks,
    with a longer break after multiple work sessions.

    This application manages:
    - Work and break intervals
    - Countdown timer logic
    - Session tracking
    - GUI updates

    No external dependencies required.

    How to run:
        python main.py
"""

import tkinter as tk


class Pomodoro:
    # -CONSTANTS-
    PINK = "#e2979c"
    RED = "#e7305b"
    GREEN = "#9bdeac"
    YELLOW = "#f7f5dd"
    FONT_NAME = "Courier"
    WORK_MIN = 25
    SHORT_BREAK_MIN = 5
    LONG_BREAK_MIN = 20
    CHECKMARK = '✔'

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Pomodoro Timer")
        self.window.config(padx=100, pady=50, bg=Pomodoro.YELLOW)
        self.canvas = tk.Canvas(width=200, height=224, bg=Pomodoro.YELLOW, highlightthickness=0)
        self.bg_photo = tk.PhotoImage(file='tomato.png')
        self.canvas.create_image(100, 112, image=self.bg_photo)
        self.work = False
        self.break_iter = 0
        self.checkmarks = ''
        # fill is basically the color of the text
        # font = (font_name, font_size, ..) ..=bold, italic ...
        self.timer_text = self.canvas.create_text(100, 130, text="00.00", fill='white',
                                                  font=(Pomodoro.FONT_NAME, 35, "bold"))
        self.canvas.grid(column=1, row=1)

        self.timer_label = tk.Label(text="Timer", fg=Pomodoro.GREEN, bg=Pomodoro.YELLOW, font=(Pomodoro.FONT_NAME, 50))
        self.timer_label.grid(column=1, row=0)

        start_btn = tk.Button(text='start', command=self.on_start)
        start_btn.grid(column=0, row=2)

        self.checkmark_label = tk.Label(text='', fg=Pomodoro.GREEN, bg=Pomodoro.YELLOW)
        self.checkmark_label.grid(column=1, row=3)

        reset_btn = tk.Button(text='reset', command=self.reset_timer)
        reset_btn.grid(column=2, row=2)

        self.timer = None

    def reset_timer(self):
        self.window.after_cancel(self.timer)
        self.canvas.itemconfig(self.timer_text, text="00.00")
        self.timer_label.config(text="Timer", fg=Pomodoro.GREEN)
        self.checkmarks = ""
        self.checkmark_label.config(text="")

    def on_start(self):
        self.timer_label.config(text='Work Time!', fg=Pomodoro.GREEN)
        self.work = True
        self.countdown(Pomodoro.WORK_MIN * 60)

    def start_break(self):
        self.break_iter += 1
        self.work = False

        # Add checkmark to denote that a work session was just competed
        self.checkmarks += Pomodoro.CHECKMARK
        self.checkmark_label.config(text=self.checkmarks)

        if self.break_iter % 4 == 0:
            # long break
            self.timer_label.config(text='Long Break!', fg=Pomodoro.RED)
            print(f'Long break, iter = {self.break_iter}')
            self.countdown(Pomodoro.LONG_BREAK_MIN * 60)

        else:
            # short break
            self.timer_label.config(text='Short Break!', fg=Pomodoro.PINK)
            print(f'Short break, iter = {self.break_iter}')
            self.countdown(Pomodoro.SHORT_BREAK_MIN * 60)

    def countdown(self, count):
        if count >= 0:
            count_minute = (str(count // 60)).rjust(2, '0')
            count_seconds = (str(count % 60)).rjust(2, '0')
            formatted_count = f"{count_minute}:{count_seconds}"
            self.canvas.itemconfig(self.timer_text, text=formatted_count)
            self.timer = self.window.after(1000, self.countdown, count - 1)
        else:
            if self.work:
                self.start_break()
            else:
                self.on_start()

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    pomodoro_timer = Pomodoro()
    pomodoro_timer.run()
