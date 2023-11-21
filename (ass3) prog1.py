import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from fancify_text import monospaced, sansSerif

# To operate -----------------------------------------------------------------------------------------------------------------------------------------------------------
def enter_data():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    full_name = (first_name + last_name)
    full_name2 = (first_name + " " + last_name)
    mode_transaction = mode_transaction_combobox.get()
    delivery_address = address_entry.get()

    if full_name and delivery_address and mode_transaction:
        alpha_validation = (full_name + mode_transaction)
        def valid_data(validation):
            for alpha in validation:
                if not (alpha.isalpha() or alpha.isspace()):
                    return False
            return True
        
        if all(valid_data(validation) for validation in (alpha_validation)):
            orange_qty = (simpledialog.askinteger("Input", "How many Oranges do you want? They are Php25 each :)", parent=base_window))
            orange_tot_price = orange_qty*25
            str_orange_tot_price = str(orange_tot_price)
            tk.messagebox.showinfo(title="Cost of Your Purchase", message= "The total cost of your purchase of orange is Php"+ str_orange_tot_price + ".")

            apple_qty = (simpledialog.askinteger("Input", "How many Apples do you want? They are Php20 each :)", parent=base_window))
            apple_tot_price = apple_qty*20
            str_apple_tot_price = str(apple_tot_price)
            tk.messagebox.showinfo(title="Cost of Your Purchase", message= "The total cost of your purchase of apple is Php"+ str_apple_tot_price + ".")

            tot_price = orange_tot_price + apple_tot_price
            str_tot_price = str(tot_price)
            tk.messagebox.showinfo(title="Cost of Your Purchase", message= "Hello! " + full_name2 + " . Your order has been received! The total cost of your whole purchase is Php"+ str_tot_price + ". Please wait 1-2 working days to receive your order. Thank you very much for your purchase!")

            first_name_entry.delete(0, 'end')
            last_name_entry.delete(0, 'end')
            mode_transaction_combobox.delete(0, 'end')
            address_entry.delete(0, 'end')
        else:
            tk.messagebox.showerror(title="ERROR", message="Pleasen use letters and space only on Full Name and Mode of Payment")
    else:
        tk.messagebox.showerror(title="ERROR", message="Please fill up the Full Name, Address, and Mode of Payment.")
# Base window ------------------------------------------------------------------------------------------------------------------------------------------------------
base_window = tk.Tk()
base_window.title("Purple Leaf Online Store")

frame_of_bw = tk.Frame(base_window)
frame_of_bw.pack()
frame_of_bw.configure(bg='#B2C248')

#First frame ----------------------------------------------------------------------------------------------------------------------------------------------------------------
first_frame = tk.LabelFrame(frame_of_bw, text=("W e l c o m e  to  P u r p l e  L e a f  S t o r e !"), font=("monospaced", 12, "bold"), fg="#E2E2E2")
first_frame.grid(row=0, column=0, padx=20, pady=10)
first_frame.configure(bg="#805533")

first_name_label = tk.Label(first_frame, text=("First Name"), font=("sansSerif" ,10), fg="#FDE64B")
first_name_label.grid(row=0, column=0)
first_name_label.configure(bg="#805533")
first_name_entry = tk.Entry(first_frame)
first_name_entry.grid(row=1,column=0, sticky="news", padx=20, pady=10)

last_name_label = tk.Label(first_frame, text="Last Name", font=("sansSerif" ,10), fg="#FDE64B")
last_name_label.grid(row=0, column=2)
last_name_label.configure(bg="#805533")
last_name_entry = tk.Entry(first_frame)
last_name_entry.grid(row=1, column=2, sticky="news", padx=20, pady=10)

mode_transaction_label = tk.Label(first_frame, text=("Mode of Payment"), font=("sansSerif" ,10), fg="#FDE64B")
mode_transaction_label.grid(row=2, column=2)
mode_transaction_label.configure(bg="#805533")
mode_transaction_combobox = ttk.Combobox(first_frame, values=["COD", "Online Banking"])
mode_transaction_combobox.grid(row=3, column=2)

address_label = tk.Label(first_frame, text=("Address"), font=("sansSerif" ,10), fg="#FDE64B")
address_label.grid(row=2, column=0)
address_label.configure(bg="#805533")
address_entry = tk.Entry(first_frame)
address_entry.grid(row=3, column=0, pady=10, padx=20)

#Check out button --------------------------------------------------------------------------------------------------------------------------------------------------------------
proceed_button = tk.Button(frame_of_bw, text="Proceed", fg="#FDE64B", command= enter_data)
proceed_button.grid(row=1, column=0, sticky="news", padx=20, pady=10)
proceed_button.configure(bg="#805533")

base_window.mainloop()