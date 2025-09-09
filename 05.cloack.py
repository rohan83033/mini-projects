import tkinter as tk
from time import strftime

class DigitalClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Digital Clock")
        
        # Configure window
        self.root.geometry("400x150")
        self.root.configure(bg='black')
        self.root.resizable(False, False)
        
        # Center the window on screen
        self.center_window()
        
        # Create time label
        self.time_label = tk.Label(
            self.root,
            font=('Digital-7', 48, 'bold'),  # Fallback to Arial if Digital-7 not available
            background='black',
            foreground='cyan'
        )
        self.time_label.pack(expand=True)
        
        # Create date label
        self.date_label = tk.Label(
            self.root,
            font=('Arial', 14),
            background='black',
            foreground='white'
        )
        self.date_label.pack()
        
        # Start the clock
        self.update_time()
        
    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.root.winfo_screenheight() // 2) - (150 // 2)
        self.root.geometry(f"400x150+{x}+{y}")
        
    def update_time(self):
        """Update the time display"""
        # Get current time and format it
        current_time = strftime('%H:%M:%S')
        current_date = strftime('%A, %B %d, %Y')
        
        # Update labels
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        
        # Schedule next update after 1000ms (1 second)
        self.root.after(1000, self.update_time)
        
    def run(self):
        """Start the clock application"""
        self.root.mainloop()

# Alternative simple version without class
def simple_digital_clock():
    """Simple function-based digital clock"""
    root = tk.Tk()
    root.title("Simple Digital Clock")
    root.geometry("300x100")
    root.configure(bg='black')
    
    def update_time():
        time_string = strftime('%H:%M:%S')
        time_label.config(text=time_string)
        root.after(1000, update_time)
    
    time_label = tk.Label(
        root,
        font=('Arial', 24, 'bold'),
        background='black',
        foreground='green'
    )
    time_label.pack(expand=True)
    
    update_time()
    root.mainloop()

if __name__ == "__main__":
    # Run the main digital clock
    clock = DigitalClock()
    clock.run()