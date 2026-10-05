import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# ============================================================
# CUSTOMTKINTER SETTINGS
# ============================================================

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


# ============================================================
# CONVERSION DATA
# ============================================================

CONVERSIONS = {
    "Length": {
        "Meter (m)": 1,
        "Kilometer (km)": 1000,
        "Centimeter (cm)": 0.01,
        "Millimeter (mm)": 0.001,
        "Mile (mi)": 1609.344,
        "Yard (yd)": 0.9144,
        "Foot (ft)": 0.3048,
        "Inch (in)": 0.0254,
    },

    "Weight": {
        "Kilogram (kg)": 1,
        "Gram (g)": 0.001,
        "Milligram (mg)": 0.000001,
        "Pound (lb)": 0.45359237,
        "Ounce (oz)": 0.0283495,
        "Tonne (t)": 1000,
    },

    "Area": {
        "Square Meter (m²)": 1,
        "Square Kilometer (km²)": 1000000,
        "Square Centimeter (cm²)": 0.0001,
        "Square Foot (ft²)": 0.092903,
        "Square Yard (yd²)": 0.836127,
        "Acre": 4046.856422,
        "Hectare": 10000,
    },

    "Volume": {
        "Liter (L)": 1,
        "Milliliter (mL)": 0.001,
        "Cubic Meter (m³)": 1000,
        "Cubic Centimeter (cm³)": 0.001,
        "Gallon (US)": 3.78541,
        "Quart (US)": 0.946353,
        "Pint (US)": 0.473176,
    },

    "Speed": {
        "Meter/Second (m/s)": 1,
        "Kilometer/Hour (km/h)": 0.277777778,
        "Mile/Hour (mph)": 0.44704,
        "Foot/Second (ft/s)": 0.3048,
        "Knot (kn)": 0.514444,
    },

    "Time": {
        "Second (s)": 1,
        "Minute (min)": 60,
        "Hour (hr)": 3600,
        "Day": 86400,
        "Week": 604800,
        "Month (30 days)": 2592000,
        "Year (365 days)": 31536000,
    },

    "Data Storage": {
        "Byte (B)": 1,
        "Kilobyte (KB)": 1024,
        "Megabyte (MB)": 1024 ** 2,
        "Gigabyte (GB)": 1024 ** 3,
        "Terabyte (TB)": 1024 ** 4,
        "Bit (bit)": 0.125,
    },

    "Pressure": {
        "Pascal (Pa)": 1,
        "Kilopascal (kPa)": 1000,
        "Bar": 100000,
        "Atmosphere (atm)": 101325,
        "PSI": 6894.757,
        "Torr": 133.322,
    },

    "Energy": {
        "Joule (J)": 1,
        "Kilojoule (kJ)": 1000,
        "Calorie (cal)": 4.184,
        "Kilocalorie (kcal)": 4184,
        "Watt-hour (Wh)": 3600,
        "Kilowatt-hour (kWh)": 3600000,
    },

    "Temperature": {
        "Celsius (°C)": "C",
        "Fahrenheit (°F)": "F",
        "Kelvin (K)": "K",
    }
}

# ============================================================
# COLORS
# ============================================================

BG = "#F5F8FC"
BORDER = "#DCE5F2"
TEXT = "#111111"
SUBTEXT = "#64748B"
SECONDARY = "#64748B"
BLUE = "#2878F0"
BLUE_HOVER = "#1765D1"
GREEN = "#36C978"
GREEN_LIGHT = "#F0FBF5"

# ============================================================
# MAIN APPLICATION
# ============================================================

class UnitConverter(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Unit Converter")
        self.geometry("820x620")
        self.minsize(820, 620)

        self.configure(fg_color=BG)

        self.current_category = "Length"  # Default category


# ========================================================
# MAIN UI
# ========================================================

        self.main_frame = ctk.CTkFrame(
            self,
            width=800,
            height=600,
            fg_color=BG,
            border_color=BORDER,
            border_width=2,
            corner_radius=20
        )
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

#=====================HEADER SECTION========================

        #-------- LOGO IMAGE --------

        self.logo_image = ctk.CTkImage(
            light_image=Image.open("arrows.png"),
            dark_image=Image.open("arrows.png"),
            size=(60, 60)
        )

        self.logo = ctk.CTkLabel(
            self.main_frame,
            image=self.logo_image,
            text=""
        )
        self.logo.place(x=20, y=40)

        self.heading = ctk.CTkLabel(
            self.main_frame,
            text="Unit Converter",
            text_color=TEXT,
            fg_color="transparent",
            font=("Arial", 40, "bold")
        )
        self.heading.place(x=220, y=60, anchor="center")

        self.sub_heading = ctk.CTkLabel(
                    self.main_frame,
                    text="Convert length, weight, and temperature instantly. Fully client-side.",
                    text_color=SUBTEXT,
                    fg_color="transparent",
                    font=("Arial", 15)
                )
        self.sub_heading.place(x=300, y=90, anchor="center")

#=====================BUTTON SECTION========================

        self.buttons = []

        def select_button(selected_button, category):
            # Reset every button
            for button in self.buttons:
                button.configure(
                    fg_color="#FFFFFF",
                    text_color="#000000",
                    hover_color="#E6E6E6"
                )

            # Highlight selected button
            selected_button.configure(
                fg_color=BLUE,
                text_color="#FFFFFF",
                hover_color=BLUE_HOVER
            )

            # Change units according to category
            self.select_category(category)



        for i, conversion in enumerate(CONVERSIONS.keys()):

            # 6 buttons in each row
            row = i // 6
            column = i % 6

            self.button = ctk.CTkButton(
                self.main_frame,
                text=conversion,
                width=100,
                height=40,
                font=("Arial", 14, ),
                fg_color="#FFFFFF",
                border_color=BORDER,
                border_width=1,
                corner_radius=10,
                text_color="#000000",
                hover_color="#E6E6E6"
            )

            self.button.configure(
                command=lambda b=self.button, c=conversion: select_button(b, c)
            )

            self.button.place(
                x=25 + (column * 110),
                y=150 + (row * 50)
            )

            self.buttons.append(self.button)

          

#=====================CONVERSION SECTION========================

        self.conversion_frame = ctk.CTkFrame(
            self.main_frame,
            width=750,
            height=300,
            fg_color="#FFFFFF",
            border_width=1,
            border_color="#DCE5F2",
            corner_radius=10
        )
        self.conversion_frame.place(x=25, y=250)

#===================== OPTION MENU ========================

        self.input_leble = ctk.CTkLabel(
            self.conversion_frame,
            text="From",
            font=("Arial", 14, "bold"),
            text_color=SUBTEXT,
            fg_color="transparent"
        )
        self.input_leble.place(x=55, y=10)

        self.output_leble = ctk.CTkLabel(
            self.conversion_frame,
            text="To",
            font=("Arial", 14, "bold"),
            text_color=SUBTEXT,
            fg_color="transparent"
        )
        self.output_leble.place(x=455, y=10)

        self.input_options = ctk.CTkOptionMenu(
            self.conversion_frame,
            width=250,
            height=50,
            values=list(CONVERSIONS["Length"].keys()),
            font=("Arial", 18), 
            fg_color=BG,
            text_color="#111111",
            button_color=BG,
            button_hover_color="#E6E6E6",
            corner_radius=10,
        )
        self.input_options.place(x=50, y=40)

        self.output_options = ctk.CTkOptionMenu(
            self.conversion_frame,
            width=250,
            height=50,
            values=list(CONVERSIONS["Length"].keys()),
            font=("Arial", 18), 
            fg_color=BG,
            text_color="#111111",
            button_color=BG,
            corner_radius=10,
            button_hover_color="#E6E6E6",
        )
        self.output_options.place(x=450, y=40)

#===================== INPUT VALUE ========================
        self.value_label = ctk.CTkLabel(
            self.conversion_frame,
            text="Value",
            font=("Arial", 14, "bold"),
            text_color=SUBTEXT,
            fg_color="transparent"
        )
        self.value_label.place(x=55, y=120)

        self.result_label = ctk.CTkLabel(
            self.conversion_frame,
            text="Result",
            font=("Arial", 14, "bold"),
            text_color=SUBTEXT,
            fg_color="transparent"
        )  
        self.result_label.place(x=455, y=120)

        self.input_value = ctk.CTkEntry(
            self.conversion_frame,
            width=250,
            height=50,
            placeholder_text="Enter value",
            font=("Arial", 18), 
            fg_color=BG,
            text_color="#111111",
            border_width=1,
            border_color=BORDER,
            corner_radius=5
        )
        self.input_value.bind("<Return>", lambda event: self.convert_units())
        self.input_value.place(x=50, y=150)

        self.output_value = ctk.CTkEntry(
            self.conversion_frame,
            width=250,
            height=50,
            placeholder_text="Converted value",
            font=("Arial", 18),
            fg_color=BG,
            text_color="#111111",
            border_width=1,
            border_color=BORDER,
            corner_radius=5
        )
        self.output_value.place(x=450, y=150)

#===================== SWAP BUTTON ========================

        self.swap_button = ctk.CTkButton(
            self.conversion_frame,
            text="⇋",
            width=50,
            height=50,
            fg_color=BG,
            text_color="#111111",
            font=("Arial", 40, "bold"),
            border_width=1,
            border_color=BORDER,
            hover_color="#D9D9D9",
            corner_radius=10,
            command=self.swap_units
        )
        self.swap_button.place(x=350, y=40)

        self.convert_button = ctk.CTkButton(
            self.conversion_frame,
            text="Convert",
            width=100,
            height=50,
            fg_color=BLUE,
            text_color="#FFFFFF",
            font=("Arial", 18, "bold"),
            border_width=0,
            hover_color=BLUE_HOVER,
            corner_radius=10,
            command=self.convert_units
        )
        self.convert_button.place(x=325, y=150)

#===================== COPY BUTTON ========================

        self.copyframe = ctk.CTkFrame(
            self.conversion_frame,
            width=650,
            height=50,
            fg_color=GREEN_LIGHT,
            border_width=0,
            corner_radius=10
        )

        self.copyframe.place(x=50, y=230)

        self.tick = ctk.CTkLabel(
            self.copyframe,
            text="✓",
            width=30,
            height=30,
            padx=0,
            pady=0,
            font=("Arial", 18, "bold"),
            text_color="#006FE6",
            fg_color=GREEN_LIGHT,
            border_width=2,
            border_color="#006FE6",
            corner_radius=10
        )
        self.tick.place(x=10, y=10)


        self.copy_label = ctk.CTkLabel(
            self.copyframe,
            text="Precise conversion, calculated locally",
            font=("Arial", 16),
            text_color=SUBTEXT,
            fg_color="transparent"
        )

        self.copy_label.place(x=60, y=10)


        self.copy_button = ctk.CTkButton(
            self.copyframe,
            text="⧉ Copy",
            width=100,
            height=35,
            fg_color=BLUE,
            text_color="#FFFFFF",
            font=("Arial", 14, "bold"),
            border_width=0,
            hover_color=BLUE_HOVER,
            corner_radius=10,
            command=self.copy_to_clipboard
        )

        self.copy_button.place(x=530, y=8)

        # Select the first button by default
        self.buttons[0].configure(
            fg_color=BLUE,
            text_color="#FFFFFF",
            hover_color=BLUE_HOVER
        )

        self.select_category("Length")

#===================================================================
# LOGICAL FUNCTIONALITY
#===================================================================

    def select_category(self, category):
        """Change From/To unit options according to selected category."""

        self.current_category = category

        units = list(CONVERSIONS[category].keys())

        self.input_options.configure(values=units)
        self.output_options.configure(values=units)

        self.input_options.set(units[0])

        if len(units) > 1:
            self.output_options.set(units[1])
        else:
            self.output_options.set(units[0])

        self.input_value.delete(0, "end")
        self.output_value.delete(0, "end")


    def convert_units(self):
        """Convert the entered value."""

        value_text = self.input_value.get().strip()

        # Nothing entered
        if not value_text:
            self.output_value.delete(0, "end")
            return

        # Check number
        try:
            value = float(value_text)

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid number."
            )
            return

        source = self.input_options.get()
        target = self.output_options.get()

        # Current selected category
        category = self.current_category

        try:
            result = self.convert_value(
                value,
                category,
                source,
                target
            )

            result = self.format_number(result)

            # Display result
            self.output_value.delete(0, "end")
            self.output_value.insert(0, result)

        except Exception as error:
            messagebox.showerror(
                "Conversion Error",
                f"Unable to convert value.\n\n{error}"
            )


    def swap_units(self):
        """Swap From and To units."""

        from_unit = self.input_options.get()
        to_unit = self.output_options.get()

        self.input_options.set(to_unit)
        self.output_options.set(from_unit)

        # Automatically convert after swapping
        self.convert_units()


    def copy_to_clipboard(self):
        """Copy result to clipboard."""

        value = self.output_value.get().strip()

        if not value:
            messagebox.showwarning(
                "Nothing to Copy",
                "Please convert a value first."
            )
            return

        self.clipboard_clear()
        self.clipboard_append(value)
        self.update()

        # Change message
        self.copy_label.configure(
            text="✓ Result copied to clipboard!",
            text_color=GREEN
        )

        # Change back after 2 seconds
        self.after(
            2000,
            lambda: self.copy_label.configure(
                text="Precise conversion, calculated locally",
                text_color=SUBTEXT
            )
        )


#------------------------ Temperature Conversion -------------------------

    def convert_temperature(self, value, source, target):
        """Convert temperature through Celsius."""

        source_code = CONVERSIONS["Temperature"][source]
        target_code = CONVERSIONS["Temperature"][target]

        # Convert source → Celsius
        if source_code == "C":
            celsius = value

        elif source_code == "F":
            celsius = (value - 32) * 5 / 9

        elif source_code == "K":
            celsius = value - 273.15

        # Convert Celsius → target
        if target_code == "C":
            return celsius

        elif target_code == "F":
            return (celsius * 9 / 5) + 32

        elif target_code == "K":
            return celsius + 273.15


#------------------------ General Conversion -----------------------------

    def convert_value(self, value, category, source, target):
        """Perform the actual conversion."""

        if category == "Temperature":
            return self.convert_temperature(
                value,
                source,
                target
            )

        # Source → base unit
        base_value = value * CONVERSIONS[category][source]

        # Base unit → target
        result = base_value / CONVERSIONS[category][target]

        return result


#------------------------ Number Formatting ------------------------------

    def format_number(self, value):
        """Format result without unnecessary zeros."""

        # Avoid very small floating-point errors
        if abs(value) < 1e-12:
            value = 0.0

        return f"{value:,.10f}".rstrip("0").rstrip(".")




app = UnitConverter()
app.mainloop()