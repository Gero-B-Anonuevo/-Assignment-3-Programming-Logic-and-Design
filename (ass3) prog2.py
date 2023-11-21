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
            max_money = (simpledialog.askinteger("Input", "How much money do you want to spend?", parent=base_window))
            payment_price = (simpledialog.askinteger("Input", "How much money would you pay for an apple? (Starts at Php20)", minvalue=16, parent=base_window))

            money_remainder = max_money%payment_price
            qty_apple_to_buy = max_money//payment_price
            tot_cost = qty_apple_to_buy*payment_price
            str_total_cost = str(tot_cost)
            str_payment_price = str(payment_price)
            str_max_money = str(max_money)
            str_qty_apple_to_buy = str(qty_apple_to_buy)
            str_money_remainder = str(money_remainder)
        
            value_data = tk.messagebox.askokcancel(title="Hello customer!", message= "The total money that you have is Php"+ str_max_money + ". If you want to buy an apple for Php" + str_payment_price + ", and buy as many apple as you can. Then you will have to pay Php" + str_total_cost + ", for " + str_qty_apple_to_buy + " apple\s. Which will leave you with Php" + str_money_remainder + ". Do you want to proceed?")
            if value_data == True:
                tk.messagebox.showinfo(title="Thank you for your purchase!", message= "Thank you for your purchase! The total is Php" + str_total_cost + " for " + str_qty_apple_to_buy + " apple\s. The product will be delivered within 2 working days. Please be our customer again! :)")
            else:
                tk.messagebox.showinfo(title="Thank you customer!", message= "May our journey be quick, I still enjoyed it. Till next time " + full_name2)

            first_name_entry.delete(0, 'end')
            last_name_entry.delete(0, 'end')
            mode_transaction_combobox.delete(0, 'end')
            address_entry.delete(0, 'end')

        else:
            tk.messagebox.showerror(title="ERROR", message="Please use letters and space only on Full Name and Mode of Payment")
    else:
        tk.messagebox.showerror(title="ERROR", message="Please fill up the Full Name, Address, and Mode of Payment.")
# Base window ------------------------------------------------------------------------------------------------------------------------------------------------------
base_window = tk.Tk()
base_window.title("Purple Leaf Online Store")

frame_of_bw = tk.Frame(base_window)
frame_of_bw.pack()
frame_of_bw.configure(bg='#8878C3')
#First frame ----------------------------------------------------------------------------------------------------------------------------------------------------------------
first_frame = tk.LabelFrame(frame_of_bw, text=("Welcome to Purple Leaf Store!"), font=("monospaced", 17, "bold"), fg="#E2E2E2")
first_frame.grid(row=0, column=0, padx=20, pady=10)
first_frame.configure(bg='#570861')

first_name_label = tk.Label(first_frame, text=("First Name"), font=("sansSerif" ,13,"bold"), fg="#E2E2E2")
first_name_label.grid(row=0, column=0)
first_name_label.configure(bg="#570861")
first_name_entry = tk.Entry(first_frame)
first_name_entry.grid(row=1,column=0, sticky="news", padx=20, pady=10)
first_name_entry.configure(bg="#E2E2E2")

last_name_label = tk.Label(first_frame, text="Last Name", font=("sansSerif" ,13,"bold"), fg="#E2E2E2")
last_name_label.grid(row=0, column=2)
last_name_label.configure(bg="#570861")
last_name_entry = tk.Entry(first_frame)
last_name_entry.grid(row=1, column=2, sticky="news", padx=20, pady=10)
last_name_entry.configure(bg="#E2E2E2")

mode_transaction_label = tk.Label(first_frame, text=("Mode of Payment"), font=("sansSerif" ,13,"bold"), fg="#E2E2E2")
mode_transaction_label.grid(row=2, column=2)
mode_transaction_label.configure(bg="#570861")
mode_transaction_combobox = ttk.Combobox(first_frame, values=["COD", "Online Banking"])
mode_transaction_combobox.grid(row=3, column=2)

address_label = tk.Label(first_frame, text=("Address"), font=("sansSerif" ,13,"bold"), fg="#E2E2E2")
address_label.grid(row=2, column=0)
address_label.configure(bg="#570861")
address_entry = tk.Entry(first_frame)
address_entry.grid(row=3, column=0, pady=10, padx=20)
address_entry.configure(bg="#E2E2E2")

#Check out button --------------------------------------------------------------------------------------------------------------------------------------------------------------
proceed_button = tk.Button(frame_of_bw, text="Proceed", fg="#E2E2E2", command= enter_data)
proceed_button.grid(row=1, column=0, sticky="news", padx=20, pady=10)
proceed_button.configure(bg='#570861')

base_window.mainloop()
