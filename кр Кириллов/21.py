import tkinter as tk


def calculate_price():

    base_prices = {
        "small": 100,
        "medium": 200,
        "large": 300
    }

    size = size_var.get()
    if not size:
        label_result.config(text="Выберите размер пиццы!")
        return

    total_price = base_prices[size]

    toppings_text = []

    if cheese_var.get():
        total_price += 30
        toppings_text.append("Сыр")

    if mushrooms_var.get():
        total_price += 30
        toppings_text.append("Грибы")

    if sausage_var.get():
        total_price += 30
        toppings_text.append("Колбаса")

    size_names = {
        "small": "Маленькая",
        "medium": "Средняя",
        "large": "Большая"
    }

    result_text = f"Размер: {size_names[size]}\n"
    result_text += f"Базовая цена: {base_prices[size]}₽\n"

    if toppings_text:
        result_text += f"Добавки: {', '.join(toppings_text)}\n"
        result_text += f"Стоимость добавок: {len(toppings_text) * 30}₽\n"
    else:
        result_text += "Добавки: нет\n"

    result_text += f"\nИТОГО: {total_price}₽"

    label_result.config(text=result_text)

root = tk.Tk()
root.title("Пицерия - Форма заказа")
root.geometry("450x500")
root.resizable(False, False)

label_title = tk.Label(root, text="🍕 Заказ пиццы", font=("Arial", 18, "bold"))
label_title.pack(pady=15)

frame_size = tk.Frame(root)
frame_size.pack(pady=10, fill=tk.X, padx=20)

label_size = tk.Label(frame_size, text="Выберите размер:", font=("Arial", 12, "bold"))
label_size.pack(anchor=tk.W)

size_var = tk.StringVar(value="")

rb_small = tk.Radiobutton(
    frame_size,
    text="Маленькая (100₽)",
    variable=size_var,
    value="small",
    font=("Arial", 11),
    anchor=tk.W
)
rb_small.pack(anchor=tk.W, pady=2)

rb_medium = tk.Radiobutton(
    frame_size,
    text="Средняя (200₽)",
    variable=size_var,
    value="medium",
    font=("Arial", 11),
    anchor=tk.W
)
rb_medium.pack(anchor=tk.W, pady=2)

rb_large = tk.Radiobutton(
    frame_size,
    text="Большая (300₽)",
    variable=size_var,
    value="large",
    font=("Arial", 11),
    anchor=tk.W
)
rb_large.pack(anchor=tk.W, pady=2)

separator1 = tk.Frame(root, height=2, bg="#cccccc")
separator1.pack(fill=tk.X, padx=20, pady=15)

frame_toppings = tk.Frame(root)
frame_toppings.pack(pady=10, fill=tk.X, padx=20)

label_toppings = tk.Label(frame_toppings, text="Выберите добавки (+30₽ каждая):",
                          font=("Arial", 12, "bold"))
label_toppings.pack(anchor=tk.W)

cheese_var = tk.BooleanVar(value=False)
mushrooms_var = tk.BooleanVar(value=False)
sausage_var = tk.BooleanVar(value=False)

cb_cheese = tk.Checkbutton(
    frame_toppings,
    text="Сыр (+30₽)",
    variable=cheese_var,
    font=("Arial", 11),
    anchor=tk.W
)
cb_cheese.pack(anchor=tk.W, pady=2)

cb_mushrooms = tk.Checkbutton(
    frame_toppings,
    text="Грибы (+30₽)",
    variable=mushrooms_var,
    font=("Arial", 11),
    anchor=tk.W
)
cb_mushrooms.pack(anchor=tk.W, pady=2)

cb_sausage = tk.Checkbutton(
    frame_toppings,
    text="Колбаса (+30₽)",
    variable=sausage_var,
    font=("Arial", 11),
    anchor=tk.W
)
cb_sausage.pack(anchor=tk.W, pady=2)

separator2 = tk.Frame(root, height=2, bg="#cccccc")
separator2.pack(fill=tk.X, padx=20, pady=15)

button_calculate = tk.Button(
    root,
    text="Рассчитать стоимость",
    command=calculate_price,
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=20,
    pady=10,
    cursor="hand2"
)
button_calculate.pack(pady=15)

label_result = tk.Label(
    root,
    text="Выберите параметры заказа и нажмите кнопку",
    font=("Arial", 11),
    justify=tk.LEFT,
    bg="#fff9e6",
    relief=tk.RAISED,
    padx=20,
    pady=15,
    anchor=tk.W
)
label_result.pack(pady=10, fill=tk.X, padx=20)

root.mainloop()