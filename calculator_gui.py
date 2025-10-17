#!/usr/bin/env python3
"""
Advanced Calculator with GUI Interface
A calculator with pop-up window and advanced mathematical functions
"""

import tkinter as tk
from tkinter import ttk, messagebox, font
import math
import re
from typing import Union

class AdvancedCalculatorGUI:
    """
    A GUI calculator class with advanced mathematical functions
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_variables()
        self.setup_styles()
        self.create_widgets()
        self.memory = 0
        self.history = []
        
    def setup_window(self):
        """Configure the main window"""
        self.root.title("Advanced Calculator")
        self.root.geometry("600x700")
        self.root.resizable(True, True)
        self.root.configure(bg='#2c3e50')
        
        # Center the window on screen
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (600 // 2)
        y = (self.root.winfo_screenheight() // 2) - (700 // 2)
        self.root.geometry(f"600x700+{x}+{y}")
        
        # Set icon (optional - will use default if no icon file)
        try:
            self.root.iconbitmap('calculator.ico')
        except:
            pass
    
    def setup_variables(self):
        """Initialize variables"""
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        self.result_var = tk.StringVar()
        self.result_var.set("")
        self.expression = ""
        self.current_input = "0"
        self.last_result = 0
        self.degrees_mode = tk.BooleanVar(value=True)
        self.showing_result = False
        self.cursor_pos = 1  # Cursor position in display (after the "0")
        
    def setup_styles(self):
        """Configure custom styles"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure button styles with hover effects
        # Number buttons (dark blue-gray)
        self.style.configure('Number.TButton', 
                           background='#34495e', 
                           foreground='white',
                           font=('Arial', 12, 'bold'),
                           padding=10,
                           relief='raised',
                           borderwidth=2)
        self.style.map('Number.TButton',
                      background=[('active', '#4a6082'),  # Lighter blue-gray on hover
                                ('pressed', '#2c3e50')])   # Darker when pressed
        
        # Operator buttons (red)
        self.style.configure('Operator.TButton', 
                           background='#e74c3c', 
                           foreground='white',
                           font=('Arial', 12, 'bold'),
                           padding=10,
                           relief='raised',
                           borderwidth=2)
        self.style.map('Operator.TButton',
                      background=[('active', '#ec7063'),  # Lighter red on hover
                                ('pressed', '#c0392b')])   # Darker when pressed
        
        # Function buttons (blue)
        self.style.configure('Function.TButton', 
                           background='#3498db', 
                           foreground='white',
                           font=('Arial', 10, 'bold'),
                           padding=8,
                           relief='raised',
                           borderwidth=2)
        self.style.map('Function.TButton',
                      background=[('active', '#5dade2'),  # Lighter blue on hover
                                ('pressed', '#2980b9')])   # Darker when pressed
        
        # Equal button (green)
        self.style.configure('Equal.TButton', 
                           background='#27ae60', 
                           foreground='white',
                           font=('Arial', 16, 'bold'),
                           padding=15,
                           relief='raised',
                           borderwidth=2)
        self.style.map('Equal.TButton',
                      background=[('active', '#52c882'),  # Lighter green on hover
                                ('pressed', '#229954')])   # Darker when pressed
    
    def create_widgets(self):
        """Create and layout all widgets"""
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = tk.Label(main_frame, 
                              text="Advanced Calculator", 
                              font=('Arial', 18, 'bold'),
                              bg='#2c3e50', fg='white')
        title_label.pack(pady=(0, 10))
        
        # Display
        self.create_display(main_frame)
        
        # Mode selector
        self.create_mode_selector(main_frame)
        
        # Buttons
        self.create_button_grid(main_frame)
        
        # Memory and history
        self.create_memory_history(main_frame)
    
    def create_display(self, parent):
        """Create the calculator display"""
        display_frame = ttk.Frame(parent)
        display_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Single integrated display container
        display_container = tk.Frame(display_frame, bg='#ecf0f1', relief='sunken', bd=3)
        display_container.pack(fill=tk.X, ipady=8)
        
        # Input display (Entry widget for cursor support)
        self.input_display = tk.Entry(display_container,
                                    textvariable=self.display_var,
                                    font=('Arial', 18, 'bold'),
                                    bg='#ffffff',
                                    fg='#2c3e50',
                                    justify='left',  # Changed to left for better readability
                                    bd=0,
                                    relief='flat',
                                    highlightthickness=0,
                                    highlightcolor='#3498db',
                                    insertwidth=3,
                                    insertbackground='#2c3e50',
                                    selectbackground='#3498db',
                                    selectforeground='white',
                                    state='normal')
        self.input_display.pack(fill=tk.X, padx=10, pady=5)
        
        # Bind events for cursor positioning and editing
        self.input_display.bind('<Button-1>', self.on_display_click)
        self.input_display.bind('<KeyPress>', self.on_key_press)
        self.input_display.bind('<KeyRelease>', self.on_key_release)
        self.input_display.bind('<FocusIn>', self.on_focus_in)
        
        # Give focus to the input display initially
        self.input_display.focus_set()
        
        # Result display (smaller font, below input)
        self.result_display = tk.Label(display_container,
                                     textvariable=self.result_var,
                                     font=('Arial', 14, 'normal'),
                                     bg='#ecf0f1',
                                     fg='#7f8c8d',
                                     anchor='e',
                                     padx=10,
                                     pady=3)
        self.result_display.pack(fill=tk.X)
        
        # Expression display (for debugging/history)
        self.expression_label = tk.Label(display_frame,
                                       text="",
                                       font=('Arial', 9),
                                       bg='#2c3e50',
                                       fg='#bdc3c7',
                                       anchor='e')
        self.expression_label.pack(fill=tk.X, pady=(3, 0))
    
    def create_mode_selector(self, parent):
        """Create angle mode selector"""
        mode_frame = ttk.Frame(parent)
        mode_frame.pack(fill=tk.X, pady=(0, 10))
        
        mode_label = tk.Label(mode_frame, 
                             text="Angle Mode:", 
                             font=('Arial', 10),
                             bg='#2c3e50', fg='white')
        mode_label.pack(side=tk.LEFT)
        
        degrees_radio = tk.Radiobutton(mode_frame, 
                                     text="Degrees", 
                                     variable=self.degrees_mode,
                                     value=True,
                                     bg='#2c3e50', fg='white',
                                     selectcolor='#34495e',
                                     font=('Arial', 10))
        degrees_radio.pack(side=tk.LEFT, padx=(10, 5))
        
        radians_radio = tk.Radiobutton(mode_frame, 
                                     text="Radians", 
                                     variable=self.degrees_mode,
                                     value=False,
                                     bg='#2c3e50', fg='white',
                                     selectcolor='#34495e',
                                     font=('Arial', 10))
        radians_radio.pack(side=tk.LEFT)
    
    def create_button_grid(self, parent):
        """Create the button grid"""
        button_frame = ttk.Frame(parent)
        button_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Button layout
        buttons = [
            # Row 1: Advanced functions
            [('sin', 'Function.TButton'), ('cos', 'Function.TButton'), ('tan', 'Function.TButton'), ('log', 'Function.TButton'), ('ln', 'Function.TButton')],
            # Row 2: More functions
            [('asin', 'Function.TButton'), ('acos', 'Function.TButton'), ('atan', 'Function.TButton'), ('√', 'Function.TButton'), ('x²', 'Function.TButton')],
            # Row 3: Memory and operations
            [('MC', 'Function.TButton'), ('MR', 'Function.TButton'), ('MS', 'Function.TButton'), ('(', 'Operator.TButton'), (')', 'Operator.TButton')],
            # Row 4: Numbers and operators
            [('C', 'Operator.TButton'), ('CE', 'Operator.TButton'), ('⌫', 'Operator.TButton'), ('÷', 'Operator.TButton'), ('x^y', 'Function.TButton')],
            # Row 5: Numbers
            [('7', 'Number.TButton'), ('8', 'Number.TButton'), ('9', 'Number.TButton'), ('×', 'Operator.TButton'), ('!', 'Function.TButton')],
            # Row 6: Numbers
            [('4', 'Number.TButton'), ('5', 'Number.TButton'), ('6', 'Number.TButton'), ('-', 'Operator.TButton'), ('|x|', 'Function.TButton')],
            # Row 7: Numbers
            [('1', 'Number.TButton'), ('2', 'Number.TButton'), ('3', 'Number.TButton'), ('+', 'Operator.TButton'), ('π', 'Function.TButton')],
            # Row 8: Zero and decimal
            [('±', 'Operator.TButton'), ('0', 'Number.TButton'), ('.', 'Number.TButton'), ('=', 'Equal.TButton'), ('e', 'Function.TButton')]
        ]
        
        for row_idx, row in enumerate(buttons):
            for col_idx, (text, style) in enumerate(row):
                btn = ttk.Button(button_frame, 
                               text=text, 
                               style=style,
                               command=lambda t=text: self.button_click(t))
                btn.grid(row=row_idx, column=col_idx, 
                        sticky='nsew', padx=2, pady=2)
        
        # Configure grid weights
        for i in range(len(buttons)):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(5):
            button_frame.grid_columnconfigure(i, weight=1)
    
    def create_memory_history(self, parent):
        """Create memory and history display"""
        bottom_frame = ttk.Frame(parent)
        bottom_frame.pack(fill=tk.X)
        
        # Memory display
        memory_frame = ttk.LabelFrame(bottom_frame, text="Memory", padding=5)
        memory_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        self.memory_label = tk.Label(memory_frame, 
                                   text="Memory: 0", 
                                   font=('Arial', 10),
                                   bg='#ecf0f1', fg='#2c3e50',
                                   relief='sunken', bd=1)
        self.memory_label.pack(fill=tk.X)
        
        # History display
        history_frame = ttk.LabelFrame(bottom_frame, text="Last Result", padding=5)
        history_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        self.history_label = tk.Label(history_frame, 
                                    text="Last: 0", 
                                    font=('Arial', 10),
                                    bg='#ecf0f1', fg='#2c3e50',
                                    relief='sunken', bd=1)
        self.history_label.pack(fill=tk.X)
    
    def button_click(self, char):
        """Handle button clicks"""
        try:
            if char.isdigit() or char == '.' or char in ['(', ')']:
                self.append_to_display(char)
            elif char in ['+', '-', '×', '÷']:
                self.handle_operator(char)
            elif char == '=':
                self.calculate_result()
            elif char == 'C':
                self.clear_all()
            elif char == 'CE':
                self.clear_entry()
            elif char == '⌫':
                self.backspace()
            elif char == '±':
                self.toggle_sign()
            elif char in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan']:
                self.handle_trig_function(char)
            elif char in ['log', 'ln']:
                self.handle_log_function(char)
            elif char == '√':
                self.handle_sqrt()
            elif char == 'x²':
                self.handle_square()
            elif char == 'x^y':
                self.handle_power()
            elif char == '!':
                self.handle_factorial()
            elif char == '|x|':
                self.handle_abs()
            elif char == 'π':
                self.handle_pi()
            elif char == 'e':
                self.handle_e()
            elif char == 'MC':
                self.memory_clear()
            elif char == 'MR':
                self.memory_recall()
            elif char == 'MS':
                self.memory_store()
        except Exception as e:
            self.show_error(str(e))
        finally:
            # Always ensure focus returns to input display after button click
            self.input_display.focus_set()
    
    def on_display_click(self, event):
        """Handle mouse click on display - sets cursor position"""
        try:
            # Update cursor position based on click
            self.cursor_pos = self.input_display.index(tk.INSERT)
            # Allow the click to proceed normally
            return "break"
        except:
            pass
    
    def on_key_press(self, event):
        """Handle key press on display - allow navigation and some editing"""
        # Allow cursor movement keys and some editing
        allowed_keys = ['Left', 'Right', 'Home', 'End', 'Up', 'Down', 
                       'BackSpace', 'Delete', 'Control_L', 'Control_R']
        
        # Allow Ctrl+A (Select All), Ctrl+C (Copy), Ctrl+V (Paste), Ctrl+X (Cut)
        if event.state & 0x4:  # Ctrl key is pressed
            if event.keysym in ['a', 'c', 'v', 'x', 'A', 'C', 'V', 'X']:
                # Update cursor position after the key is processed
                self.root.after(1, self.update_cursor_position)
                return
        
        if event.keysym in allowed_keys:
            # Handle backspace and delete manually for proper cursor tracking
            if event.keysym == 'BackSpace':
                self.backspace()
                return "break"
            elif event.keysym == 'Delete':
                self.delete_forward()
                return "break"
            else:
                # Update cursor position after the key is processed
                self.root.after(1, self.update_cursor_position)
                return
        
        # Allow direct number and operator input via keyboard
        elif event.char.isdigit() or event.char in '.+-*/()':
            self.append_to_display(event.char)
            return "break"
        else:
            # Prevent other direct typing in the Entry widget
            return "break"
    
    def update_cursor_position(self):
        """Update internal cursor position from Entry widget"""
        try:
            self.cursor_pos = self.input_display.index(tk.INSERT)
        except:
            pass
    
    def on_key_release(self, event):
        """Handle key release events"""
        # Update cursor position after key release
        self.update_cursor_position()
    
    def on_focus_in(self, event):
        """Handle focus in events"""
        # Update cursor position when focus is gained
        self.update_cursor_position()
    
    def append_to_display(self, char):
        """Append character to display at cursor position"""
        if self.showing_result:
            # If showing result, start new calculation
            self.clear_all()
            self.showing_result = False
        
        current = self.display_var.get()
        
        # Handle initial "0" replacement
        if current == "0" and char != '.':
            self.display_var.set(char)
            self.cursor_pos = 1
        else:
            # Insert character at cursor position
            new_text = current[:self.cursor_pos] + char + current[self.cursor_pos:]
            self.display_var.set(new_text)
            self.cursor_pos += 1
        
        # Update Entry cursor position and maintain focus
        self.input_display.icursor(self.cursor_pos)
        self.input_display.focus_set()
        
        self.current_input = self.display_var.get()
        self.update_live_calculation()
    
    def insert_function(self, function_name):
        """Insert function call with cursor positioned inside parentheses"""
        if self.showing_result:
            # If showing result, start new calculation
            self.clear_all()
            self.showing_result = False
        
        current = self.display_var.get()
        function_text = f"{function_name}()"
        
        # Handle initial "0" replacement
        if current == "0":
            self.display_var.set(function_text)
            self.cursor_pos = len(function_name) + 1  # Position inside parentheses
        else:
            # Insert function at cursor position
            new_text = current[:self.cursor_pos] + function_text + current[self.cursor_pos:]
            self.display_var.set(new_text)
            self.cursor_pos += len(function_name) + 1  # Position inside parentheses
        
        # Update Entry cursor position and maintain focus
        self.input_display.icursor(self.cursor_pos)
        self.input_display.focus_set()
        
        self.current_input = self.display_var.get()
        self.update_live_calculation()
    
    def update_live_calculation(self):
        """Update the secondary display with live calculation preview"""
        try:
            current_expr = self.expression + self.current_input
            if current_expr and current_expr != "0":
                # Try to evaluate current expression for preview
                if self.can_evaluate(current_expr):
                    result = self.evaluate_expression(current_expr)
                    self.result_var.set(f"= {result}")
                else:
                    self.result_var.set("")
            else:
                self.result_var.set("")
        except:
            self.result_var.set("")
    
    def can_evaluate(self, expr):
        """Check if expression can be safely evaluated"""
        if not expr or expr == "0":
            return False
        
        # Don't evaluate if expression ends with operator
        if expr.strip().endswith(('+', '-', '*', '/', '(', '^', '×', '÷')):
            return False
        
        # Don't evaluate if parentheses are unbalanced
        if expr.count('(') != expr.count(')'):
            return False
        
        # Check if it's just a simple number
        try:
            float(expr)
            return True
        except:
            pass
        
        # For complex expressions with functions, we'll let evaluate_expression handle the validation
        # Just do basic checks for obvious invalid patterns
        
        # Check for empty parentheses
        if '()' in expr:
            return False
        
        # Check for double operators
        invalid_patterns = ['++', '--', '**', '//', '××', '÷÷', '+-', '-+', '*+', '+*', '/+', '+/', '×+', '+×', '÷+', '+÷']
        for pattern in invalid_patterns:
            if pattern in expr:
                return False
        
        # If it contains function names, operators, numbers, or constants, it's probably valid
        # Let evaluate_expression do the detailed validation
        return True
    
    def handle_operator(self, op):
        """Handle operator input"""
        if self.showing_result:
            # If showing result, use result as start of new calculation
            self.expression = str(self.last_result)
            self.showing_result = False
        
        # Convert display symbols to calculation symbols
        op_map = {'×': '*', '÷': '/'}
        calc_op = op_map.get(op, op)
        
        current = self.display_var.get()
        if current != "0":
            self.expression += current + calc_op
            self.display_var.set("0")
            self.current_input = ""
            self.result_var.set("")
            self.update_expression_display()
    
    def calculate_result(self):
        """Calculate and display result with animation"""
        try:
            # Get the complete expression from the display
            current = self.display_var.get()
            
            # Skip if it's just "0" or empty
            if current == "0" or not current:
                return
            
            # Evaluate the complete expression
            result = self.evaluate_expression(current)
            
            # Animate the transition
            self.animate_result_transition(current, result)
            
            self.last_result = result
            self.history_label.config(text=f"Last: {result}")
            
            # Reset for next calculation
            self.expression = ""
            self.current_input = ""
            self.showing_result = True
            self.update_expression_display()
        except ValueError as e:
            self.show_error(f"Math Error: {str(e)}")
        except ZeroDivisionError:
            self.show_error("Division by zero")
        except OverflowError:
            self.show_error("Result too large")
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
    
    def animate_result_transition(self, expression, result):
        """Animate the transition from input to result"""
        # Step 1: Show both expression and result briefly
        self.result_var.set(f"= {result}")
        self.root.update()
        self.root.after(400)  # Brief pause to show the calculation
        
        # Step 2: Swap prominence - make result larger, expression smaller
        # Shrink input display and show the expression that was calculated
        self.input_display.config(font=('Arial', 12, 'normal'), fg='#7f8c8d')
        self.display_var.set(expression)
        
        # Enlarge result display to make it prominent
        self.result_display.config(font=('Arial', 22, 'bold'), fg='#2c3e50')
        self.result_var.set(str(result))
        
        self.root.update()
    
    def evaluate_expression(self, expression):
        """Safely evaluate mathematical expression"""
        # Replace function names with their Python equivalents
        expression = expression.replace('^', '**')
        expression = expression.replace('×', '*')
        expression = expression.replace('÷', '/')
        
        # Handle trigonometric functions
        if self.degrees_mode.get():
            expression = re.sub(r'(?<!math\.)\bsin\(([^)]+)\)', r'math.sin(math.radians(\1))', expression)
            expression = re.sub(r'(?<!math\.)\bcos\(([^)]+)\)', r'math.cos(math.radians(\1))', expression)
            expression = re.sub(r'(?<!math\.)\btan\(([^)]+)\)', r'math.tan(math.radians(\1))', expression)
            expression = re.sub(r'(?<!math\.)\basin\(([^)]+)\)', r'math.degrees(math.asin(\1))', expression)
            expression = re.sub(r'(?<!math\.)\bacos\(([^)]+)\)', r'math.degrees(math.acos(\1))', expression)
            expression = re.sub(r'(?<!math\.)\batan\(([^)]+)\)', r'math.degrees(math.atan(\1))', expression)
        else:
            expression = re.sub(r'(?<!math\.)\bsin\(([^)]+)\)', r'math.sin(\1)', expression)
            expression = re.sub(r'(?<!math\.)\bcos\(([^)]+)\)', r'math.cos(\1)', expression)
            expression = re.sub(r'(?<!math\.)\btan\(([^)]+)\)', r'math.tan(\1)', expression)
            expression = re.sub(r'(?<!math\.)\basin\(([^)]+)\)', r'math.asin(\1)', expression)
            expression = re.sub(r'(?<!math\.)\bacos\(([^)]+)\)', r'math.acos(\1)', expression)
            expression = re.sub(r'(?<!math\.)\batan\(([^)]+)\)', r'math.atan(\1)', expression)
        
        # Handle other functions (order matters - specific patterns first)
        expression = re.sub(r'√\(([^)]+)\)', r'math.sqrt(\1)', expression)
        expression = re.sub(r'(?<!math\.)\bsqrt\(([^)]+)\)', r'math.sqrt(\1)', expression)  # Negative lookbehind to avoid double replacement
        expression = re.sub(r'\bln\(([^)]+)\)', r'math.log(\1)', expression)
        expression = re.sub(r'(?<!math\.)\blog\(([^)]+)\)', r'math.log10(\1)', expression)  # Negative lookbehind
        expression = re.sub(r'\|([^|]+)\|', r'abs(\1)', expression)  # |x| notation
        expression = re.sub(r'(?<!math\.)\babs\(([^)]+)\)', r'abs(\1)', expression)  # Negative lookbehind
        expression = re.sub(r'\bfact\(([^)]+)\)', r'math.factorial(int(\1))', expression)
        
        # Replace constants
        expression = re.sub(r'\bπ\b', str(math.pi), expression)
        expression = re.sub(r'\bpi\b', str(math.pi), expression)
        expression = re.sub(r'\be\b', str(math.e), expression)
        
        # Add implicit multiplication
        expression = re.sub(r'(\d)(\()', r'\1*\2', expression)
        expression = re.sub(r'(\))(\d)', r'\1*\2', expression)
        expression = re.sub(r'(\))(\()', r'\1*\2', expression)
        
        # Safe evaluation
        allowed_names = {
            'math': math,
            'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
            'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
            'sqrt': math.sqrt, 'log': math.log, 'log10': math.log10,
            'abs': abs, 'pi': math.pi, 'e': math.e,
            'factorial': math.factorial, 'degrees': math.degrees, 'radians': math.radians
        }
        
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return float(result)
    
    def handle_trig_function(self, func):
        """Handle trigonometric function - insert function call"""
        self.insert_function(func)
    
    def handle_log_function(self, func):
        """Handle logarithmic function - insert function call"""
        self.insert_function(func)
    
    def handle_sqrt(self):
        """Handle square root - insert function call"""
        self.insert_function("√")
    
    def handle_square(self):
        """Handle square (x²)"""
        try:
            # Get current value - either from display or evaluate expression
            if self.showing_result:
                current_value = self.last_result
            else:
                current_expr = self.display_var.get()
                if current_expr == "0" or current_expr == "":
                    return
                
                # Try to evaluate the expression first
                try:
                    if self.can_evaluate(current_expr):
                        current_value = self.evaluate_expression(current_expr)
                    else:
                        current_value = float(current_expr)
                except:
                    current_value = float(current_expr)
            
            result = current_value ** 2
            
            # Show the result immediately
            self.clear_all()
            self.display_var.set(str(result))
            self.result_var.set(f"({current_value})² = {result}")
            self.last_result = result
            self.showing_result = True
            
            # Update the larger font for result display
            self.input_display.config(font=('Arial', 12, 'normal'), fg='#7f8c8d')
            self.result_display.config(font=('Arial', 22, 'bold'), fg='#2c3e50')
            
        except Exception as e:
            self.show_error(f"Error in square: {str(e)}")
    
    def handle_power(self):
        """Handle power operation"""
        self.handle_operator('^')
    
    def handle_factorial(self):
        """Handle factorial"""
        try:
            # Get current value - either from display or evaluate expression
            if self.showing_result:
                current_value = self.last_result
            else:
                current_expr = self.display_var.get()
                if current_expr == "0" or current_expr == "":
                    return
                
                # Try to evaluate the expression first
                try:
                    if self.can_evaluate(current_expr):
                        current_value = self.evaluate_expression(current_expr)
                    else:
                        current_value = float(current_expr)
                except:
                    current_value = float(current_expr)
            
            # Convert to integer for factorial
            int_value = int(current_value)
            if int_value != current_value:
                raise ValueError("Factorial requires an integer")
            if int_value < 0:
                raise ValueError("Factorial of negative number")
            if int_value > 170:  # Factorial limit to prevent overflow
                raise ValueError("Number too large for factorial")
            
            result = math.factorial(int_value)
            
            # Show the result immediately
            self.clear_all()
            self.display_var.set(str(result))
            self.result_var.set(f"{int_value}! = {result}")
            self.last_result = result
            self.showing_result = True
            
            # Update the larger font for result display
            self.input_display.config(font=('Arial', 12, 'normal'), fg='#7f8c8d')
            self.result_display.config(font=('Arial', 22, 'bold'), fg='#2c3e50')
            
        except Exception as e:
            self.show_error(f"Error in factorial: {str(e)}")
    
    def handle_abs(self):
        """Handle absolute value"""
        try:
            # Get current value - either from display or evaluate expression
            if self.showing_result:
                current_value = self.last_result
            else:
                current_expr = self.display_var.get()
                if current_expr == "0" or current_expr == "":
                    return
                
                # Try to evaluate the expression first
                try:
                    if self.can_evaluate(current_expr):
                        current_value = self.evaluate_expression(current_expr)
                    else:
                        current_value = float(current_expr)
                except:
                    current_value = float(current_expr)
            
            result = abs(current_value)
            
            # Show the result immediately
            self.clear_all()
            self.display_var.set(str(result))
            self.result_var.set(f"|{current_value}| = {result}")
            self.last_result = result
            self.showing_result = True
            
            # Update the larger font for result display
            self.input_display.config(font=('Arial', 12, 'normal'), fg='#7f8c8d')
            self.result_display.config(font=('Arial', 22, 'bold'), fg='#2c3e50')
            
        except Exception as e:
            self.show_error(f"Error in absolute value: {str(e)}")
    
    def handle_pi(self):
        """Insert pi constant"""
        self.display_var.set(str(math.pi))
    
    def handle_e(self):
        """Insert e constant"""
        self.display_var.set(str(math.e))
    
    def clear_all(self):
        """Clear everything and reset display"""
        self.display_var.set("0")
        self.result_var.set("")
        self.expression = ""
        self.current_input = "0"
        self.showing_result = False
        self.cursor_pos = 1  # Reset cursor position after "0"
        
        # Reset display formatting to default (input mode)
        self.input_display.config(font=('Arial', 18, 'bold'), fg='#2c3e50')
        self.result_display.config(font=('Arial', 14, 'normal'), fg='#7f8c8d')
        
        # Set cursor position and restore focus
        self.input_display.icursor(self.cursor_pos)
        self.input_display.focus_set()
        
        self.update_expression_display()
    
    def clear_entry(self):
        """Clear current entry"""
        if self.showing_result:
            self.clear_all()
        else:
            self.display_var.set("0")
            self.current_input = "0"
            self.result_var.set("")
            self.cursor_pos = 1
            self.input_display.icursor(self.cursor_pos)
    
    def backspace(self):
        """Remove character at cursor position"""
        if self.showing_result:
            self.clear_all()
            return
            
        current = self.display_var.get()
        if self.cursor_pos > 0 and len(current) > 0:
            if self.cursor_pos <= len(current):
                # Remove character before cursor
                new_value = current[:self.cursor_pos-1] + current[self.cursor_pos:]
                if new_value == "":
                    new_value = "0"
                    self.cursor_pos = 1
                else:
                    self.cursor_pos -= 1
                    if self.cursor_pos < 0:
                        self.cursor_pos = 0
                
                self.display_var.set(new_value)
                self.current_input = new_value
                self.input_display.icursor(self.cursor_pos)
        
        self.update_live_calculation()
    
    def delete_forward(self):
        """Remove character after cursor position (Delete key)"""
        if self.showing_result:
            self.clear_all()
            return
            
        current = self.display_var.get()
        if self.cursor_pos < len(current):
            # Remove character after cursor
            new_value = current[:self.cursor_pos] + current[self.cursor_pos+1:]
            if new_value == "":
                new_value = "0"
                self.cursor_pos = 1
            
            self.display_var.set(new_value)
            self.current_input = new_value
            self.input_display.icursor(self.cursor_pos)
        
        self.update_live_calculation()
    
    def toggle_sign(self):
        """Toggle sign of current number"""
        if self.showing_result:
            # Toggle sign of result and start new calculation
            try:
                value = -float(self.result_var.get())
                self.clear_all()
                self.display_var.set(str(value))
                self.current_input = str(value)
            except:
                pass
            return
            
        current = self.display_var.get()
        if current != "0":
            try:
                value = float(current)
                new_value = str(-value)
                self.display_var.set(new_value)
                self.current_input = new_value
                self.update_live_calculation()
            except:
                pass
    
    def memory_clear(self):
        """Clear memory"""
        self.memory = 0
        self.memory_label.config(text="Memory: 0")
    
    def memory_recall(self):
        """Recall from memory"""
        self.clear_all()
        self.display_var.set(str(self.memory))
        self.current_input = str(self.memory)
    
    def memory_store(self):
        """Store to memory"""
        if self.showing_result:
            self.memory = self.last_result
        else:
            current = self.display_var.get()
            try:
                self.memory = float(current)
            except:
                return
        self.memory_label.config(text=f"Memory: {self.memory}")
    
    def update_expression(self):
        """Update expression for complex calculations"""
        pass  # This method is now replaced by update_live_calculation
    
    def update_expression_display(self):
        """Update expression display"""
        if self.expression:
            self.expression_label.config(text=f"Expression: {self.expression}")
        else:
            self.expression_label.config(text="")
    
    def show_error(self, message):
        """Show error message"""
        messagebox.showerror("Error", message)
        self.display_var.set("0")
    
    def run(self):
        """Start the calculator"""
        self.root.mainloop()

def main():
    """Main function to start the calculator"""
    try:
        calculator = AdvancedCalculatorGUI()
        calculator.run()
    except Exception as e:
        # Create a temporary root for error display
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        messagebox.showerror("Calculator Error", f"Failed to start calculator: {str(e)}")
        root.destroy()

if __name__ == "__main__":
    main()