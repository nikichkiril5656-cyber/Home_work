import tkinter as tk

def calculate_tips(*args):

    bill_amount = float(entry_bill.get()) if entry_bill.get() else 0

    tip_percent = scale_tip.get()

    tip_amount = bill_amount * (tip_percent / 100)

    total_amount = bill_amount + tip_amount

    result_text = f"Чаевые ({tip_percent}%): {tip_amount:.2f} руб.\nОбщая сумма: {total_amount:.2f} руб."
    label_result.config(text=result_text)



root = tk.Tk()
root.title("Личный кассир - Расчет чаевых")
root.geometry("400x300")
root.resizable(False, False)

label_title = tk.Label(root, text="Расчет чаевых", font=("Arial", 16, "bold"))
label_title.pack(pady=15)

frame_bill = tk.Frame(root)
frame_bill.pack(pady=10)

label_bill = tk.Label(frame_bill, text="Сумма счета:", font=("Arial", 12))
label_bill.pack(side=tk.LEFT, padx=5)

entry_bill = tk.Entry(frame_bill, font=("Arial", 12), width=15)
entry_bill.pack(side=tk.LEFT, padx=5)
entry_bill.bind('<KeyRelease>', calculate_tips)  # Пересчет при вводе суммы

frame_scale = tk.Frame(root)
frame_scale.pack(pady=15)

label_scale = tk.Label(frame_scale, text="Процент чаевых:", font=("Arial", 12))
label_scale.pack(side=tk.LEFT, padx=5)

scale_tip = tk.Scale(
    frame_scale,
    from_=5,
    to=25,
    orient=tk.HORIZONTAL,
    length=200,
    tickinterval=5,
    resolution=1,
    command=lambda x: calculate_tips()
)
scale_tip.set(15)
scale_tip.pack(side=tk.LEFT, padx=5)
label_percent = tk.Label(frame_scale, text=f"{scale_tip.get()}%", font=("Arial", 12))
label_percent.pack(side=tk.LEFT, padx=5)


def update_percent_label(value):
    label_percent.config(text=f"{int(float(value))}%")
    calculate_tips()

scale_tip.config(command=update_percent_label)
label_result = tk.Label(
    root,
    text="Чаевые (15%): 0.00 руб.\nОбщая сумма: 0.00 руб.",
    font=("Arial", 12),
    justify=tk.CENTER,
    bg="#e8f4f8",
    relief=tk.RAISED,
    padx=20,
    pady=15
)
label_result.pack(pady=20, fill=tk.X, padx=20)
calculate_tips()

root.mainloop()