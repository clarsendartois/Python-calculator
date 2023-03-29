import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
small_display_font_style = ("Bookman Old Style", 15)
large_display_font_style = ("Bookman Old Style", 45, "bold")
default_digit_font_style = ("Bookman Old Style", 20, "bold")

frame_fg_bg_color = "#202020"
digit_buttons_fg_color = "#3c3c3c"
other_buttons_fg_color = "#323232"


class Calculator:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("320x503")
        self.window.resizable(0, 0)
        self.window.title("CLARSEN: Calculator")

        self.logo_frame = self.create_logo_frame()
        self.create_button_logo()

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()
        self.total_label, self.label, self.space = self.create_display_label()

        self.top_buttons_frame = self.create_top_buttons_frame()
        self.create_top_buttons()
        self.top_buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 7):
            self.top_buttons_frame.rowconfigure(x, weight=1)
            self.top_buttons_frame.columnconfigure(x, weight=1)

        self.buttons_frame = self.create_buttons_frame()
        self.digits = {
            7: (2, 1), 8: (2, 2), 9: (2, 3),
            4: (3, 1), 5: (3, 2), 6: (3, 3),
            1: (4, 1), 2: (4, 2), 3: (4, 3),
            "\u00B1": (5, 1), 0: (5, 2), ".": (5, 3)
        }
        self.operations = {"/": "\u00f7", "*": "\u00d7", "-": "-", "+": "+"}
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 6):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

    def create_logo_frame(self):
        logo_frame = ctk.CTkFrame(
            self.window, bg_color=frame_fg_bg_color, fg_color=frame_fg_bg_color)
        logo_frame.pack(fill="both")
        return logo_frame

    def create_button_logo(self):
        photo = tk.PhotoImage(file=".\img\\clarsen_logo.png")
        button = ctk.CTkButton(self.logo_frame, text="",
                               image=photo, border_width=2)
        button.pack()

    def create_display_frame(self):
        display_frame = ctk.CTkFrame(
            self.window, bg_color=frame_fg_bg_color, fg_color=frame_fg_bg_color)
        display_frame.pack(fill="both")
        return display_frame

    def create_display_label(self):
        total_label = ctk.CTkLabel(
            self.display_frame, text=self.total_expression, anchor=tk.E,  padx=10, font=small_display_font_style)
        total_label.pack(fill="both")

        label = ctk.CTkLabel(self.display_frame, text=self.current_expression,
                             anchor=tk.E,  padx=10, font=large_display_font_style)
        label.pack(fill="both")

        space = ctk.CTkLabel(self.display_frame, text="")
        space.pack(fill="both")
        return total_label, label, space

    def create_top_buttons_frame(self):
        top_buttons_frame = ctk.CTkFrame(
            self.window, bg_color=frame_fg_bg_color, fg_color=frame_fg_bg_color)
        top_buttons_frame.pack(fill="both")
        return top_buttons_frame

    def create_top_buttons(self):
        self.create_mc_button()
        self.create_mr_button()
        self.create_m_plus_button()
        self.create_m_minus_button()
        self.create_ms_button()
        self.create_m_log_button()

    def create_mc_button(self):
        button = ctk.CTkButton(self.top_buttons_frame, text=(
            "MC"), border_width=1, border_color=frame_fg_bg_color, fg_color=frame_fg_bg_color, font=default_digit_font_style)
        button.grid(row=0, column=1, sticky=ctk.NSEW)

    def create_mr_button(self):
        button = ctk.CTkButton(self.top_buttons_frame, text=(
            "MR"), border_width=1, border_color=frame_fg_bg_color, fg_color=frame_fg_bg_color, font=default_digit_font_style)
        button.grid(row=0, column=2, sticky=ctk.NSEW)

    def create_m_plus_button(self):
        button = ctk.CTkButton(self.top_buttons_frame, text=(
            "M+"), border_width=1, border_color=frame_fg_bg_color, fg_color=frame_fg_bg_color, font=default_digit_font_style)
        button.grid(row=0, column=3, sticky=ctk.NSEW)

    def create_m_minus_button(self):
        button = ctk.CTkButton(self.top_buttons_frame, text=(
            "M-"), border_width=1, border_color=frame_fg_bg_color, fg_color=frame_fg_bg_color, font=default_digit_font_style)
        button.grid(row=0, column=4, sticky=ctk.NSEW)

    def create_ms_button(self):
        button = ctk.CTkButton(self.top_buttons_frame, text=(
            "MS"), border_width=1, border_color=frame_fg_bg_color, fg_color=frame_fg_bg_color, font=default_digit_font_style)
        button.grid(row=0, column=5, sticky=ctk.NSEW)

    def create_m_log_button(self):
        button = ctk.CTkButton(self.top_buttons_frame, text=(
            "M"), border_width=1, border_color=frame_fg_bg_color, fg_color=frame_fg_bg_color, font=default_digit_font_style)
        button.grid(row=0, column=6, sticky=ctk.NSEW)

    def create_buttons_frame(self):
        buttons_frame = ctk.CTkFrame(
            self.window, bg_color=frame_fg_bg_color, fg_color=frame_fg_bg_color)
        buttons_frame.pack(expand=True, fill="both")
        return buttons_frame

    def add_to_expresstion(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = ctk.CTkButton(self.buttons_frame, text=str(
                digit), border_width=1, border_color=frame_fg_bg_color, fg_color=digit_buttons_fg_color, font=default_digit_font_style, command=lambda x=digit: self.add_to_expresstion(x))
            button.grid(row=grid_value[0],
                        column=grid_value[1], sticky=ctk.NSEW)

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f"{symbol}")
        self.total_label.configure(text=expression)

    def update_label(self):
        self.label.configure(text=self.current_expression[:10])

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 1
        for operator, symbol in self.operations.items():
            button = ctk.CTkButton(self.buttons_frame, text=(
                symbol), border_width=1, border_color=frame_fg_bg_color, fg_color=other_buttons_fg_color, font=default_digit_font_style, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=ctk.NSEW)
            i += 1

    def create_special_buttons(self):
        self.create_perncent_button()
        self.create_clearE_button()
        self.create_clear_button()
        self.create_backspace_button()
        self.create_divide_by_button()
        self.create_sqr_button()
        self.create_sqr_root_button()
        self.create_equals_button()

    def create_perncent_button(self):
        button = ctk.CTkButton(self.buttons_frame, text=(
            "%"), border_width=1, border_color=frame_fg_bg_color, fg_color=other_buttons_fg_color, font=default_digit_font_style)
        button.grid(row=0, column=1, sticky=ctk.NSEW)

    def clearE(self):
        self.current_expression = ""
        self.update_label()

    def create_clearE_button(self):
        button = ctk.CTkButton(self.buttons_frame, text=(
            "CE"), border_width=1, border_color=frame_fg_bg_color, fg_color=other_buttons_fg_color, font=default_digit_font_style, command=self.clearE)
        button.grid(row=0, column=2, sticky=ctk.NSEW)

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = ctk.CTkButton(self.buttons_frame, text=(
            "C"), border_width=1, border_color=frame_fg_bg_color, fg_color=other_buttons_fg_color, font=default_digit_font_style, command=self.clear)
        button.grid(row=0, column=3, sticky=ctk.NSEW)

    def backspace(self):
        self.current_expression = self.current_expression[:-1]
        self.update_label()

    def create_backspace_button(self):
        button = ctk.CTkButton(self.buttons_frame, text=(
            "\u232B"), border_width=1, border_color=frame_fg_bg_color, fg_color=other_buttons_fg_color, font=default_digit_font_style, command=self.backspace)
        button.grid(row=0, column=4, sticky=ctk.NSEW)

    def create_divide_by_button(self):
        button = ctk.CTkButton(self.buttons_frame, text=(
            "\u215F""𝑥"), border_width=1, border_color=frame_fg_bg_color, fg_color=other_buttons_fg_color, font=default_digit_font_style)
        button.grid(row=1, column=1, sticky=ctk.NSEW)

    def sqr(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_sqr_button(self):
        button = ctk.CTkButton(self.buttons_frame, text=(
            "𝑥²"), border_width=1, border_color=frame_fg_bg_color, fg_color=other_buttons_fg_color, font=default_digit_font_style, command=self.sqr)
        button.grid(row=1, column=2, sticky=ctk.NSEW)

    def sqr_root(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def create_sqr_root_button(self):
        button = ctk.CTkButton(self.buttons_frame, text=(
            "²""\u221A""𝑥"), border_width=1, border_color=frame_fg_bg_color, fg_color=other_buttons_fg_color, font=default_digit_font_style, command=self.sqr_root)
        button.grid(row=1, column=3, sticky=ctk.NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""
            self.update_label()
        except Exception:
            self.current_expression = "Cannot \u00f7 0"
        finally:
            self.update_label()

    def create_equals_button(self):
        button = ctk.CTkButton(self.buttons_frame, text=(
            "="), border_width=1, border_color=frame_fg_bg_color, font=default_digit_font_style, command=self.evaluate)
        button.grid(row=5, column=4, sticky=ctk.NSEW)

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate)
        for key in self.digits:
            self.window.bind(str(key), lambda event,
                             digit=key: self.add_to_expression(digit))
        for key in self.operations:
            self.window.bind(key, lambda event,
                             operator=key: self.append_operator(operator))

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
