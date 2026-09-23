import math
import time
import tkinter as tk
from datetime import datetime
from tkinter import messagebox, ttk

# --- Theme Definitions ---
THEMES = {
    "Cyberpunk": {
        "bg": "#111118",
        "fg": "#00ffff",
        "accent": "#ff007f",
        "panel": "#1a1a24",
        "canvas_bg": "#0a0a0f",
    },
    "Dark": {
        "bg": "#1e1e1e",
        "fg": "#ffffff",
        "accent": "#007acc",
        "panel": "#252526",
        "canvas_bg": "#121212",
    },
    "Light": {
        "bg": "#f0f0f0",
        "fg": "#1a1a1a",
        "accent": "#0056b3",
        "panel": "#e0e0e0",
        "canvas_bg": "#ffffff",
    },
    "Matrix": {
        "bg": "#000000",
        "fg": "#00ff00",
        "accent": "#008800",
        "panel": "#051105",
        "canvas_bg": "#020a02",
    },
}

WORLD_ZONES = {
    "London (UTC+0)": 0,
    "New York (UTC-4)": -4,
    "Tokyo (UTC+9)": 9,
    "Sydney (UTC+10)": 10,
    "Mumbai (UTC+5.5)": 5.5,
}


class MultiClockApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Multi-Function Clock Suite")
        self.geometry("600x550+100+50")

        self.current_theme = THEMES["Cyberpunk"]

        # Stopwatch / Timer States
        self.sw_running = False
        self.sw_elapsed = 0.0
        self.sw_start_time = 0.0

        self.timer_running = False
        self.timer_seconds = 0
        self.timer_target_time = 0.0

        # Alarm State
        self.alarm_time = None
        self.alarm_triggered = False

        self.setup_ui()
        self.apply_theme("Cyberpunk")
        self.update_clock()

    # --- UI Setup ---
    def setup_ui(self):
        # Configure Tab Styles
        self.style = ttk.Style()
        self.style.theme_use("default")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        # Tab Frames
        self.tab_clock = tk.Frame(self.notebook)
        self.tab_alarm = tk.Frame(self.notebook)
        self.tab_world = tk.Frame(self.notebook)
        self.tab_stopwatch = tk.Frame(self.notebook)
        self.tab_timer = tk.Frame(self.notebook)

        self.notebook.add(self.tab_clock, text="Clock")
        self.notebook.add(self.tab_alarm, text="Alarm")
        self.notebook.add(self.tab_world, text="World Clock")
        self.notebook.add(self.tab_stopwatch, text="Stopwatch")
        self.notebook.add(self.tab_timer, text="Timer")

        self.build_clock_tab()
        self.build_alarm_tab()
        self.build_world_tab()
        self.build_stopwatch_tab()
        self.build_timer_tab()

    #  Hybrid Clock & Themes
    def build_clock_tab(self):
        # Theme Selector Dropdown
        theme_frame = tk.Frame(self.tab_clock)
        theme_frame.pack(fill="x", padx=10, pady=5)
        tk.Label(theme_frame, text="Theme: ", font=("Helvetica", 10)).pack(
            side="left"
        )

        self.theme_var = tk.StringVar(value="Cyberpunk")
        theme_menu = ttk.Combobox(
            theme_frame,
            textvariable=self.theme_var,
            values=list(THEMES.keys()),
            state="readonly",
            width=12,
        )
        theme_menu.pack(side="left")
        theme_menu.bind(
            "<<ComboboxSelected>>",
            lambda e: self.apply_theme(self.theme_var.get()),
        )

        # Analog Canvas
        self.analog_canvas = tk.Canvas(
            self.tab_clock, width=240, height=240, highlightthickness=0
        )
        self.analog_canvas.pack(pady=10)

        # Digital Clock Label
        self.digital_label = tk.Label(
            self.tab_clock, font=("Courier", 26, "bold")
        )
        self.digital_label.pack(pady=10)

    # --- Tab 2: Alarm ---
    def build_alarm_tab(self):
        tk.Label(
            self.tab_alarm,
            text="Set Alarm (24-Hour HH:MM)",
            font=("Helvetica", 12, "bold"),
        ).pack(pady=15)

        time_frame = tk.Frame(self.tab_alarm)
        time_frame.pack(pady=10)

        self.alarm_hour = ttk.Spinbox(
            time_frame, from_=0, to=23, width=3, format="%02.0f", font=("Helvetica", 16)
        )
        self.alarm_hour.set("07")
        self.alarm_hour.pack(side="left", padx=5)

        tk.Label(time_frame, text=":", font=("Helvetica", 16, "bold")).pack(
            side="left"
        )

        self.alarm_min = ttk.Spinbox(
            time_frame, from_=0, to=59, width=3, format="%02.0f", font=("Helvetica", 16)
        )
        self.alarm_min.set("00")
        self.alarm_min.pack(side="left", padx=5)

        btn_frame = tk.Frame(self.tab_alarm)
        btn_frame.pack(pady=15)

        tk.Button(
            btn_frame,
            text="Set Alarm",
            command=self.set_alarm,
            width=10,
            font=("Helvetica", 10, "bold"),
        ).pack(side="left", padx=5)
        tk.Button(
            btn_frame,
            text="Cancel",
            command=self.cancel_alarm,
            width=10,
            font=("Helvetica", 10),
        ).pack(side="left", padx=5)

        self.alarm_status_label = tk.Label(
            self.tab_alarm,
            text="Alarm: Not Set",
            font=("Helvetica", 11, "italic"),
        )
        self.alarm_status_label.pack(pady=10)

    # --- Tab 3: World Clock ---
    def build_world_tab(self):
        tk.Label(
            self.tab_world,
            text="World Clocks",
            font=("Helvetica", 14, "bold"),
        ).pack(pady=10)
        self.world_labels = {}

        for zone, offset in WORLD_ZONES.items():
            frame = tk.Frame(self.tab_world)
            frame.pack(fill="x", padx=40, pady=5)

            city_lbl = tk.Label(
                frame,
                text=zone,
                font=("Helvetica", 11, "bold"),
                anchor="w",
                width=18,
            )
            city_lbl.pack(side="left")

            time_lbl = tk.Label(
                frame, text="--:--:--", font=("Courier", 12, "bold")
            )
            time_lbl.pack(side="right")

            self.world_labels[zone] = (time_lbl, offset)

    # --- Tab 4: Stopwatch ---
    def build_stopwatch_tab(self):
        self.sw_label = tk.Label(
            self.tab_stopwatch, text="00:00:00.0", font=("Courier", 32, "bold")
        )
        self.sw_label.pack(pady=30)

        btn_frame = tk.Frame(self.tab_stopwatch)
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame,
            text="Start",
            command=self.start_stopwatch,
            width=8,
            font=("Helvetica", 10, "bold"),
        ).pack(side="left", padx=5)
        tk.Button(
            btn_frame,
            text="Pause",
            command=self.pause_stopwatch,
            width=8,
            font=("Helvetica", 10),
        ).pack(side="left", padx=5)
        tk.Button(
            btn_frame,
            text="Reset",
            command=self.reset_stopwatch,
            width=8,
            font=("Helvetica", 10),
        ).pack(side="left", padx=5)

    # --- Tab 5: Timer ---
    def build_timer_tab(self):
        tk.Label(
            self.tab_timer,
            text="Set Countdown (MM:SS)",
            font=("Helvetica", 12, "bold"),
        ).pack(pady=15)

        input_frame = tk.Frame(self.tab_timer)
        input_frame.pack(pady=5)

        self.timer_min_entry = ttk.Spinbox(
            input_frame, from_=0, to=99, width=3, format="%02.0f", font=("Helvetica", 14)
        )
        self.timer_min_entry.set("01")
        self.timer_min_entry.pack(side="left", padx=2)

        tk.Label(input_frame, text=":", font=("Helvetica", 14, "bold")).pack(
            side="left"
        )

        self.timer_sec_entry = ttk.Spinbox(
            input_frame, from_=0, to=59, width=3, format="%02.0f", font=("Helvetica", 14)
        )
        self.timer_sec_entry.set("00")
        self.timer_sec_entry.pack(side="left", padx=2)

        self.timer_display = tk.Label(
            self.tab_timer, text="01:00", font=("Courier", 36, "bold")
        )
        self.timer_display.pack(pady=20)

        btn_frame = tk.Frame(self.tab_timer)
        btn_frame.pack(pady=5)

        tk.Button(
            btn_frame,
            text="Start",
            command=self.start_timer,
            width=8,
            font=("Helvetica", 10, "bold"),
        ).pack(side="left", padx=5)
        
        tk.Button(
            btn_frame,
            text="Pause",
            command=self.pause_timer,
            width=8,
            font=("Helvetica", 10),
        ).pack(side="left", padx=5)
     
        tk.Button(
            btn_frame,
            text="Reset",
            command=self.reset_timer,
            width=8,
            font=("Helvetica", 10),
        ).pack(side="left", padx=5)

    # --- Theme Engine ---
    def apply_theme(self, theme_name):
        theme = THEMES[theme_name]
        self.current_theme = theme

        bg, fg, panel, c_bg = (
            theme["bg"],
            theme["fg"],
            theme["panel"],
            theme["canvas_bg"],
        )

        # Style main frames
        self.configure(bg=bg)
        for tab in [
            self.tab_clock,
            self.tab_alarm,
            self.tab_world,
            self.tab_stopwatch,
            self.tab_timer,
        ]:
            tab.configure(bg=bg)

        # Apply widget colors
        self.analog_canvas.configure(bg=c_bg)
        self.digital_label.configure(bg=bg, fg=fg)
        self.sw_label.configure(bg=bg, fg=fg)
        self.timer_display.configure(bg=bg, fg=fg)

        # Apply to sub-labels/frames
        for widget in self.winfo_children():
            self._recursive_style(widget, bg, fg, panel)

    def _recursive_style(self, widget, bg, fg, panel):
        w_type = widget.winfo_class()
        if w_type in ("Frame", "TLabelframe"):
            widget.configure(bg=bg)
        elif w_type == "Label":
            widget.configure(bg=bg, fg=fg)
        for child in widget.winfo_children():
            self._recursive_style(child, bg, fg, panel)

    # --- Draw Analog Clock ---
    def draw_analog_clock(self, now):
        c = self.analog_canvas
        c.delete("all")
        cx, cy, r = 120, 120, 100
        fg = self.current_theme["fg"]
        accent = self.current_theme["accent"]

        # Outer ring & Dial ticks
        c.create_oval(
            cx - r,
            cy - r,
            cx + r,
            cy + r,
            outline=fg,
            width=3,
        )
        for i in range(12):
            angle = math.radians(i * 30)
            x1 = cx + (r - 10) * math.sin(angle)
            y1 = cy - (r - 10) * math.cos(angle)
            x2 = cx + r * math.sin(angle)
            y2 = cy - r * math.cos(angle)
            c.create_line(x1, y1, x2, y2, fill=fg, width=2)

        # Hand angles
        hr_angle = math.radians(
            (now.hour % 12 + now.minute / 60) * 30
        )
        min_angle = math.radians((now.minute + now.second / 60) * 6)
        sec_angle = math.radians(
            (now.second + now.microsecond / 1e6) * 6
        )

        # Draw Hour Hand
        c.create_line(
            cx,
            cy,
            cx + (r - 45) * math.sin(hr_angle),
            cy - (r - 45) * math.cos(hr_angle),
            fill=fg,
            width=4,
        )
        # Draw Minute Hand
        c.create_line(
            cx,
            cy,
            cx + (r - 25) * math.sin(min_angle),
            cy - (r - 25) * math.cos(min_angle),
            fill=fg,
            width=3,
        )
        # Draw Second Hand
        c.create_line(
            cx,
            cy,
            cx + (r - 15) * math.sin(sec_angle),
            cy - (r - 15) * math.cos(sec_angle),
            fill=accent,
            width=1.5,
        )

        c.create_oval(cx - 4, cy - 4, cx + 4, cy + 4, fill=accent, outline="")

    # --- Main Loop Logic ---
    def update_clock(self):
        now = datetime.now()

        # Update Main Digital & Analog Display
        self.digital_label.config(text=now.strftime("%d %b %Y\n%H:%M:%S"))
        self.draw_analog_clock(now)

        # Update Alarm Logic
        if self.alarm_time and not self.alarm_triggered:
            if now.strftime("%H:%M") == self.alarm_time:
                self.alarm_triggered = True
                messagebox.showinfo("Alarm", f"Wake up! It is {self.alarm_time}")

        # Update World Clocks
        utc_now = datetime.utcnow()
        for zone, (lbl, offset) in self.world_labels.items():
            tz_time = utc_now.timestamp() + (offset * 3600)
            time_str = datetime.utcfromtimestamp(tz_time).strftime("%H:%M:%S")
            lbl.config(text=time_str)

        # Update Stopwatch Logic
        if self.sw_running:
            self.sw_elapsed = time.time() - self.sw_start_time
            m, s = divmod(self.sw_elapsed, 60)
            h, s = divmod(s, 60)
            self.sw_label.config(
                text=f"{int(h):02d}:{int(m):02d}:{int(s):02d}.{int((s%1)*10)}"
            )

        # Update Timer Logic
        if self.timer_running:
            remaining = int(round(self.timer_target_time - time.time()))
            if remaining <= 0:
                self.timer_running = False
                self.timer_display.config(text="00:00")
                messagebox.showinfo("Timer", "Time's up!")
            else:
                m, s = divmod(remaining, 60)
                self.timer_display.config(text=f"{m:02d}:{s:02d}")

        # Schedule high-frequency update for smooth second hands/stopwatch
        self.after(100, self.update_clock)

    # --- Alarm Control ---
    def set_alarm(self):
        self.alarm_time = f"{int(self.alarm_hour.get()):02d}:{int(self.alarm_min.get()):02d}"
        self.alarm_triggered = False
        self.alarm_status_label.config(
            text=f"Alarm Set: {self.alarm_time}", fg=self.current_theme["accent"]
        )

    def cancel_alarm(self):
        self.alarm_time = None
        self.alarm_status_label.config(
            text="Alarm: Not Set", fg=self.current_theme["fg"]
        )

    # --- Stopwatch Controls ---
    def start_stopwatch(self):
        if not self.sw_running:
            self.sw_start_time = time.time() - self.sw_elapsed
            self.sw_running = True

    def pause_stopwatch(self):
        self.sw_running = False

    def reset_stopwatch(self):
        self.sw_running = False
        self.sw_elapsed = 0.0
        self.sw_label.config(text="00:00:00.0")

    # --- Timer Controls ---
    def start_timer(self):
        if not self.timer_running:
            try:
                mins = int(self.timer_min_entry.get())
                secs = int(self.timer_sec_entry.get())
                total = mins * 60 + secs
                if total > 0:
                    self.timer_target_time = time.time() + total
                    self.timer_running = True
            except ValueError:
                pass

    def pause_timer(self):
        if self.timer_running:
            self.timer_seconds = int(
                round(self.timer_target_time - time.time())
            )
            self.timer_running = False

    def reset_timer(self):
        self.timer_running = False
        self.timer_display.config(
            text=f"{int(self.timer_min_entry.get()):02d}:{int(self.timer_sec_entry.get()):02d}"
        )


if __name__ == "__main__":
    app = MultiClockApp()
    app.mainloop()