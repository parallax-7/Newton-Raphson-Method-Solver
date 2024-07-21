import tkinter as tk
from tkinter import ttk, messagebox
import math

# function that calculates YTM using Newton raphson method 
def calculate_ytm(face_value, coupon_rate, price, years, guess=0.05):     #funtion takes face value,coupon rate (interest rate),current price of the bond,years of maturity,initial guess?
    # inputs 
    face_value = float(face_value)
    coupon_rate = float(coupon_rate)
    price = float(price)
    years = int(years)
    guess = float(guess)


    # Coupon payment
    coupon_payment = face_value * (coupon_rate / 100)           

    # formula to calculate YTM using newton raphson method


    # function for YTM calculation
    def f(ytm):
        total = 0
        for t in range(1, years + 1):
            total += coupon_payment / (1 + ytm) ** t
        total += face_value / (1 + ytm) ** years
        return total - price

    # derivative of the function
    def f_prime(ytm):
        total = 0
        for t in range(1, years + 1):
            total -= t * coupon_payment / (1 + ytm) ** (t + 1)
        total -= years * face_value / (1 + ytm) ** (years + 1)
        return total

    # Newton-Raphson method
    ytm = guess
    epsilon = 1e-6            #tolerance for precision
    max_iterations = 1000      #no. of iterations for more accuracy
    for i in range(max_iterations):
        ytm_new = ytm - f(ytm) / f_prime(ytm)
        if abs(ytm_new - ytm) < epsilon:
            return ytm_new * 100
        ytm = ytm_new

    raise ValueError("Failed to converge")


# calling funtion to evaluate and return result 
def on_calculate():
    try:
        face_value = face_value_entry.get()
        coupon_rate = coupon_rate_entry.get()
        price = price_entry.get()
        years = years_entry.get()
        ytm = calculate_ytm(face_value, coupon_rate, price, years)
        result_label.config(text=f"YTM: {ytm:.2f}%")
    except Exception as e:
        messagebox.showerror("Error", str(e))




#GUI code using tkinter

# main window
root = tk.Tk()
root.title("YTM Calculator")

# input box
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# input labels
ttk.Label(frame, text="Face Value:").grid(row=0, column=0, padx=5, pady=5)
face_value_entry = ttk.Entry(frame)
face_value_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame, text="Coupon Rate (%):").grid(row=1, column=0, padx=5, pady=5)
coupon_rate_entry = ttk.Entry(frame)
coupon_rate_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame, text="Current Price:").grid(row=2, column=0, padx=5, pady=5)
price_entry = ttk.Entry(frame)
price_entry.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame, text="Years to Maturity:").grid(row=3, column=0, padx=5, pady=5)
years_entry = ttk.Entry(frame)
years_entry.grid(row=3, column=1, padx=5, pady=5)

# calculate button and calling on_calculate function
calculate_button = ttk.Button(frame, text="Calculate", command=on_calculate)
calculate_button.grid(row=4, column=0, columnspan=2, pady=5)

# outputing result
result_label = ttk.Label(frame, text="YTM: ")
result_label.grid(row=5, column=0, columnspan=2, pady=5)

# Run the main loop
root.mainloop()
