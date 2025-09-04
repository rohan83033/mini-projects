import time
import tkinter as tk
from playsound import playsound
from threading import Thread

def start_timer():
    try:
        hrs = int(entry_hours.get()) if entry_hours.get() else 0
        mins = int(entry_minutes.get()) if entry_minutes.get() else 0
        secs = int(entry_seconds.get()) if entry_seconds.get() else 0
        seconds = hrs * 3600 + mins * 60 + secs
    except ValueError:
        label.config(text="Invalid input!")
        return

    if seconds <= 0:
        label.config(text="Enter time > 0")
        return

    def countdown():
        time_elapsed = 0
        while time_elapsed < seconds:
            remaining = seconds - time_elapsed
            hrs_left, rem = divmod(remaining, 3600)
            mins_left, secs_left = divmod(rem, 60)
            time_format = f"{hrs_left:02d}:{mins_left:02d}:{secs_left:02d}"
            label.config(text=time_format)
            time.sleep(1)
            time_elapsed += 1
        label.config(text="Time's up!")
        playsound("Alarm-2-chosic.com_.mp3")

    Thread(target=countdown, daemon=True).start()

root = tk.Tk()
root.title("Alarm Countdown")
root.geometry("400x250")
root.configure(bg="#222")

label = tk.Label(root, text="00:00:00", font=("Arial", 32), fg="white", bg="#222")
label.pack(pady=20)

frame = tk.Frame(root, bg="#222")
frame.pack(pady=10)

tk.Label(frame, text="Hours", font=("Arial", 12), fg="white", bg="#222").grid(row=0, column=0, padx=5)
tk.Label(frame, text="Minutes", font=("Arial", 12), fg="white", bg="#222").grid(row=0, column=1, padx=5)
tk.Label(frame, text="Seconds", font=("Arial", 12), fg="white", bg="#222").grid(row=0, column=2, padx=5)

entry_hours = tk.Entry(frame, font=("Arial", 14), width=5, justify="center")
entry_hours.grid(row=1, column=0, padx=5)
entry_hours.insert(0, "0")

entry_minutes = tk.Entry(frame, font=("Arial", 14), width=5, justify="center")
entry_minutes.grid(row=1, column=1, padx=5)
entry_minutes.insert(0, "0")

entry_seconds = tk.Entry(frame, font=("Arial", 14), width=5, justify="center")
entry_seconds.grid(row=1, column=2, padx=5)
entry_seconds.insert(0, "10")

button = tk.Button(root, text="Start Timer", command=start_timer,
                   font=("Arial", 14), bg="#444", fg="white", relief="raised")
button.pack(pady=15)

root.mainloop()
