import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import math

def draw_clock(canvas, center_x, center_y, radius, time_obj):
    canvas.delete("all")

    canvas.create_oval(center_x - radius, center_y - radius,
                       center_x + radius, center_y + radius,
                       width=4, outline='black')

    for i in range(12):
        angle = math.radians(i * 30)
        tick_start = (center_x + (radius - 10) * math.cos(angle),
                      center_y + (radius - 10) * math.sin(angle))
        tick_end = (center_x + radius * math.cos(angle),
                    center_y + radius * math.sin(angle))
        canvas.create_line(tick_start, tick_end, width=2)

    hours, minutes, seconds = time_obj.hour, time_obj.minute, time_obj.second

    second_angle = math.radians(seconds * 6 - 90)
    minute_angle = math.radians(minutes * 6 - 90)
    hour_angle = math.radians((hours % 12) * 30 + minutes * 0.5 - 90)

    second_hand = (center_x + radius * 0.9 * math.cos(second_angle),
                   center_y + radius * 0.9 * math.sin(second_angle))
    minute_hand = (center_x + radius * 0.75 * math.cos(minute_angle),
                   center_y + radius * 0.75 * math.sin(minute_angle))
    hour_hand = (center_x + radius * 0.5 * math.cos(hour_angle),
                 center_y + radius * 0.5 * math.sin(hour_angle))

    canvas.create_line(center_x, center_y, second_hand[0], second_hand[1], fill="red", width=1)
    canvas.create_line(center_x, center_y, minute_hand[0], minute_hand[1], fill="black", width=3)
    canvas.create_line(center_x, center_y, hour_hand[0], hour_hand[1], fill="green", width=5)

def update_clocks():
    try:
        # Parse input times from entries
        time1 = datetime.strptime(f"{h1.get()}:{m1.get()}:{s1.get()}", "%H:%M:%S")
        time2 = datetime.strptime(f"{h2.get()}:{m2.get()}:{s2.get()}", "%H:%M:%S")
        time3 = datetime.strptime(f"{h3.get()}:{m3.get()}:{s3.get()}", "%H:%M:%S")

        total_seconds = (
            (time1.hour * 3600 + time1.minute * 60 + time1.second) +
            (time2.hour * 3600 + time2.minute * 60 + time2.second) +
            (time3.hour * 3600 + time3.minute * 60 + time3.second)
        ) // 3

        avg_time = datetime(1, 1, 1) + timedelta(seconds=total_seconds)

        draw_clock(clock1_canvas, 100, 100, 80, time1)
        draw_clock(clock2_canvas, 100, 100, 80, time2)
        draw_clock(clock3_canvas, 100, 100, 80, time3)
        draw_clock(avg_clock_canvas, 100, 100, 80, avg_time)

        avg_time_display.config(text=f"{avg_time.strftime('%H:%M:%S')}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid times in HH:MM:SS format.")

root = tk.Tk()
root.title("Average Time Calculator")
root.geometry("800x600")

left_frame = tk.Frame(root, width=300, padx=10, pady=10)
left_frame.pack(side=tk.LEFT, fill=tk.Y)

for i in range(3):
    tk.Label(left_frame, text=f"Time {i + 1} (HH:MM:SS)").grid(row=i, column=0, columnspan=2)

    globals()[f"h{i+1}"], globals()[f"m{i+1}"], globals()[f"s{i+1}"] = (
        tk.Entry(left_frame, width=3), tk.Entry(left_frame, width=3), tk.Entry(left_frame, width=3)
    )

    globals()[f"h{i+1}"].grid(row=i, column=2)
    globals()[f"m{i+1}"].grid(row=i, column=3)
    globals()[f"s{i+1}"].grid(row=i, column=4)

tk.Button(left_frame, text="Average", command=update_clocks).grid(row=3, columnspan=5, pady=10)

tk.Label(left_frame, text="Average Time:").grid(row=4, column=0, columnspan=2)
avg_time_display = tk.Label(left_frame, text="00:00:00", font=("Arial", 20))
avg_time_display.grid(row=4, column=2, columnspan=3)

right_frame = tk.Frame(root, width=500, padx=10, pady=10)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

clock1_canvas = tk.Canvas(right_frame, width=200, height=200, bg='white')
clock1_canvas.grid(row=0, column=0, padx=10, pady=10)
tk.Label(right_frame, text="Time 1").grid(row=1, column=0)

clock2_canvas = tk.Canvas(right_frame, width=200, height=200, bg='white')
clock2_canvas.grid(row=0, column=1, padx=10, pady=10)
tk.Label(right_frame, text="Time 2").grid(row=1, column=1)

clock3_canvas = tk.Canvas(right_frame, width=200, height=200, bg='white')
clock3_canvas.grid(row=0, column=2, padx=10, pady=10)
tk.Label(right_frame, text="Time 3").grid(row=1, column=2)

avg_clock_canvas = tk.Canvas(right_frame, width=200, height=200, bg='white')
avg_clock_canvas.grid(row=2, column=1, padx=10, pady=10)
tk.Label(right_frame, text="Average Time").grid(row=3, column=1)

root.mainloop()




