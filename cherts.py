import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BeamStressCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Расчет статического напряжения балки")

        # Входные параметры
        self.length_label = ttk.Label(self, text="Длина балки (м):")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)
        self.length_entry = ttk.Entry(self)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.load_label = ttk.Label(self, text="Нагрузка (Н):")
        self.load_label.grid(row=1, column=0, padx=10, pady=10)
        self.load_entry = ttk.Entry(self)
        self.load_entry.grid(row=1, column=1, padx=10, pady=10)

        self.calculate_button = ttk.Button(self, text="Рассчитать", command=self.calculate_stress)
        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().grid(row=3, column=0, columnspan=2)

    def calculate_stress(self):
        length = float(self.length_entry.get())
        load = float(self.load_entry.get())

        # Рассчитываем изгибающий момент (максимальное напряжение будет в середине балки)
        x = np.linspace(0, length, 100)
        M = load * (length - x) * x / length  # Распределенная нагрузка

        # Строим график
        self.ax.clear()
        self.ax.plot(x, M, label='Изгибающий момент')
        self.ax.set_xlabel('Длина балки (м)')
        self.ax.set_ylabel('Момент (Н*м)')
        self.ax.legend()
        self.ax.grid(True)
        
        self.canvas.draw()

if __name__ == "__main__":
    app = BeamStressCalculator()
    app.mainloop()