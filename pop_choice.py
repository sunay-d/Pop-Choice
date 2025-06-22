import tkinter as tk
from helper_functions.supabase_functions import search_similar
from helper_functions.chat_completions import get_chat_completion

def process_input():
    user_input = entry.get()
    query_response = search_similar(user_input)
    response = get_chat_completion(user_input, query_response)
    if user_input.strip():
        output_label.config(
            text=response
        )
    else:
        output_label.config(text=response)

def clear_output(event):
    output_label.config(text="")

# Ana pencere
root = tk.Tk()
root.title("Pop Choice")
root.geometry("1000x500")
root.configure(bg="#000000")  # siyah arka plan

# Ortalamak için çerçeve
frame = tk.Frame(root, bg="#000000")
frame.pack(expand=True)


# Title
title = tk.Label(
    frame,
    text='🎬 Pop Choice',
    font=("Arial", 50),
    fg="white",
    bg="#000000"
)
title.pack(pady=20)


# Selamlama
greeting = tk.Label(
    frame,
    text="Hello my friend! What kind of movie you are looking for?",
    font=("Arial", 20),
    fg="white",
    bg="#000000"
)
greeting.pack(pady=20)

# Girdi alanı
entry = tk.Entry(
    frame,
    width=50,
    font=("Arial", 16),
    justify="center",
    bg="#1e1e1e",      # koyu gri input
    fg="white",
    insertbackground="white"  # imleç rengi
)
entry.pack(pady=10)
entry.bind("<KeyRelease>", clear_output)

# Buton
button = tk.Button(
    frame,
    text="🔍 Search",
    command=process_input,
    font=("Arial", 16),
    bg="#005f99",     # lacivert
    fg="white",
    activebackground="#007acc",
    activeforeground="white",
    padx=10,
    pady=5
)
button.pack(pady=20)

# Çıktı alanı
output_label = tk.Label(
    frame,
    text="",
    font=("Arial", 16),
    fg="#00ccff",      # açık mavi
    bg="#000000",
    wraplength=500
)
output_label.pack(pady=10)

# Başlat
root.mainloop()
