import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# ---------------- DATABASE ----------------
conn = sqlite3.connect("vehicles.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehicles (
    number TEXT PRIMARY KEY,
    owner TEXT,
    model TEXT
)
""")
conn.commit()

# ---------------- LOGIN SYSTEM ----------------
def login():
    if entry_user.get() == "sharshitha" and entry_pass.get() == "1220":
        login_window.destroy()
        main_app()
    else:
        messagebox.showerror("Error", "Invalid Login")

# ---------------- MAIN APP ----------------
def main_app():
    global root, entry_number, entry_owner, entry_model, tree

    root = tk.Tk()
    root.title("Vehicle Manager Pro")
    root.geometry("750x600")
    root.configure(bg="#1e1e2f")

    # Title
    tk.Label(root, text="🚗 Vehicle Manager Dashboard", font=("Arial", 18, "bold"),
             bg="#1e1e2f", fg="#00ffcc").pack(pady=10)

    # Dashboard count
    count_label = tk.Label(root, text="Total Vehicles: 0",
                           bg="#1e1e2f", fg="white", font=("Arial", 12))
    count_label.pack()

    def update_count():
        cursor.execute("SELECT COUNT(*) FROM vehicles")
        count = cursor.fetchone()[0]
        count_label.config(text=f"Total Vehicles: {count}")

    # Input Frame
    frame = tk.Frame(root, bg="#2e2e3f")
    frame.pack(pady=10)

    tk.Label(frame, text="Vehicle No", bg="#2e2e3f", fg="white").grid(row=0, column=0, padx=10, pady=5)
    entry_number = ttk.Entry(frame)
    entry_number.grid(row=0, column=1)

    tk.Label(frame, text="Owner Name", bg="#2e2e3f", fg="white").grid(row=1, column=0, padx=10, pady=5)
    entry_owner = ttk.Entry(frame)
    entry_owner.grid(row=1, column=1)

    tk.Label(frame, text="Model", bg="#2e2e3f", fg="white").grid(row=2, column=0, padx=10, pady=5)
    entry_model = ttk.Entry(frame)
    entry_model.grid(row=2, column=1)

    # Functions
    def add_vehicle():
        try:
            cursor.execute("INSERT INTO vehicles VALUES (?, ?, ?)",
                           (entry_number.get(), entry_owner.get(), entry_model.get()))
            conn.commit()
            messagebox.showinfo("Success", "Added Successfully")
            view_vehicles()
            update_count()
        except:
            messagebox.showerror("Error", "Vehicle already exists")

    def view_vehicles():
        for row in tree.get_children():
            tree.delete(row)
        cursor.execute("SELECT * FROM vehicles")
        for row in cursor.fetchall():
            tree.insert("", tk.END, values=row)

    def delete_vehicle():
        cursor.execute("DELETE FROM vehicles WHERE number=?", (entry_number.get(),))
        conn.commit()
        view_vehicles()
        update_count()

    def update_vehicle():
        cursor.execute("UPDATE vehicles SET owner=?, model=? WHERE number=?",
                       (entry_owner.get(), entry_model.get(), entry_number.get()))
        conn.commit()
        view_vehicles()

    def select_item(event):
        selected = tree.focus()
        values = tree.item(selected, 'values')
        if values:
            entry_number.delete(0, tk.END)
            entry_owner.delete(0, tk.END)
            entry_model.delete(0, tk.END)
            entry_number.insert(0, values[0])
            entry_owner.insert(0, values[1])
            entry_model.insert(0, values[2])

    # Buttons
    btn_frame = tk.Frame(root, bg="#1e1e2f")
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Add", bg="#00cc66", fg="white", width=10, command=add_vehicle).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Update", bg="#ffaa00", fg="white", width=10, command=update_vehicle).grid(row=0, column=1, padx=5)
    tk.Button(btn_frame, text="Delete", bg="#ff3333", fg="white", width=10, command=delete_vehicle).grid(row=0, column=2, padx=5)
    tk.Button(btn_frame, text="Refresh", bg="#3399ff", fg="white", width=10, command=view_vehicles).grid(row=0, column=3, padx=5)

    # Table
    tree = ttk.Treeview(root, columns=("Number", "Owner", "Model"), show="headings")
    tree.heading("Number", text="Vehicle No")
    tree.heading("Owner", text="Owner")
    tree.heading("Model", text="Model")
    tree.pack(pady=20)

    tree.bind("<ButtonRelease-1>", select_item)

    view_vehicles()
    update_count()

    root.mainloop()

# ---------------- LOGIN WINDOW ----------------
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x200")
login_window.configure(bg="#1e1e2f")

tk.Label(login_window, text="Login", font=("Arial", 16),
         bg="#1e1e2f", fg="#00ffcc").pack(pady=10)

tk.Label(login_window, text="Username", bg="#1e1e2f", fg="white").pack()
entry_user = tk.Entry(login_window)
entry_user.pack()

tk.Label(login_window, text="Password", bg="#1e1e2f", fg="white").pack()
entry_pass = tk.Entry(login_window, show="*")
entry_pass.pack()

tk.Button(login_window, text="Login", bg="#00cc66", fg="white", command=login).pack(pady=10)

login_window.mainloop()