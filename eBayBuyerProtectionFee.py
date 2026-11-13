import tkinter as tk
from tkinter import messagebox


#calculating fees
def calculate_fee():
    try:
        # 1. Fetch values and handle empty inputs
        val_amount = entry_amount.get().strip()
        val_source = source_amount.get().strip()
        val_ad_rate = ad_rate.get().strip()
        
        if not val_amount or not val_source or not val_ad_rate:
            raise ValueError("All fields are required.")
            
        amount = float(val_amount)
        source_price = float(val_source)
        listed_ad_rate = float(val_ad_rate)
        
        # 2. Correct validation logic
        if amount < 0 or source_price < 0 or listed_ad_rate < 0:
            raise ValueError("Numbers must be positive.")
        
        # 3. Calculate asking price
        tier_1_base_fee = 0.10
        tier_2_base_fee = 0.70
        tier_3_base_fee = 6.70
        tier_4_base_fee = 86.70
        tier_1_percentage_rate = 1.07
        tier_2_percentage_rate = 1.04
        tier_3_percentage_rate = 1.02
        tier_4_percentage_rate = 1.00

        # 2.1 Calculating the exact BPF for different Price Ranges
        asking_price = 0
        if(amount>0 and amount<=21.50):
            asking_price = (amount - tier_1_base_fee)/tier_1_percentage_rate
        elif(amount>21.50 and amount<=312.70):
            asking_price = (amount - tier_2_base_fee)/tier_2_percentage_rate
        elif(amount>312.70 and amount<=4086.70):
            asking_price = (amount - tier_3_base_fee)/tier_3_percentage_rate
        elif(amount>4086.70):
            asking_price = (amount - tier_4_base_fee)/tier_4_percentage_rate
        
        # Calculating ad amount according to ad rate
        ad_fee = asking_price*(listed_ad_rate/100)

        #Adding 20% VAT on ad fee
        vat_ad_fee = ad_fee*0.2

        #calculating total ad fee
        total_ad_fee = ad_fee + vat_ad_fee
        
                
        # 4. Calculate PnL string safely
        pnl_value = asking_price - source_price - total_ad_fee
        total_fee = amount - asking_price
            
        # 5. Update UI
        label_ad_fee.config(text=f"Ad Fee: £{total_ad_fee:.2f}")
        label_total_fee.config(text=f"Buyer Protection Fee: £{total_fee:.2f}")
        label_total.config(text=f"Asking Price excl. BPF: £{asking_price:.2f}")
        label_fee.config(text=f"PnL: £{pnl_value:.2f}")
        
    except ValueError as e:
        messagebox.showerror("Error", str(e) if str(e) else "Please enter valid positive numbers.")

# Window Setup
root = tk.Tk()

root.title("eBay Fee Calculator")
root.geometry("380x420") # Expanded slightly to fit all fields comfortably
root.configure(background='#f7f7f7')


# Widgets layout
tk.Label(root, text="Enter Target Price incl. BPF (£):", font=("Arial", 11, 'bold'), background='#f7f7f7').pack(pady=5, padx= 15)
entry_amount = tk.Entry(root, font=("Arial", 11))
entry_amount.pack(pady=5)

tk.Label(root, text="Enter Source Price (£):", font=("Arial", 11, 'bold'), background='#f7f7f7').pack(pady=5)
source_amount = tk.Entry(root, font=("Arial", 11))
source_amount.pack(pady=5)

tk.Label(root, text="Enter Your Ad Rate (%):", font=("Arial", 11, 'bold'), background='#f7f7f7').pack(pady=5)
ad_rate = tk.Entry(root, font=("Arial", 11))
ad_rate.pack(pady=5)

btn_calc = tk.Button(root, text="Calculate", font=("Arial", 11, "bold"), command=calculate_fee, bg="#007bff", fg="white")
btn_calc.pack(pady=15)

label_ad_fee = tk.Label(root, text="Ad Fee: £0.00", font=("Arial", 11, "bold"), background='#f7f7f7')
label_ad_fee.pack(pady=5)

label_total_fee = tk.Label(root, text="Buyer Protection Fee: £0.00", font=("Arial", 11, "bold"), background='#f7f7f7')
label_total_fee.pack(pady=5)

label_total = tk.Label(root, text="Listing Price excl. BPF: £0.00", font=("Arial", 11, "bold"), background='#f7f7f7')
label_total.pack(pady=5)

label_fee = tk.Label(root, text="PnL: £0.00", font=("Arial", 11, "bold"), background='#f7f7f7')
label_fee.pack(pady=5)

root.mainloop()