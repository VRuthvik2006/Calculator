# Advanced Calculator

A comprehensive calculator application with advanced mathematical functions available in both **Console** and **GUI (Pop-up Window)** versions, built in Python and compiled to standalone executables.

# It is named Advanced Calculator because I am not creative with names

### 1. **GUI Version (Recommended)** - `AdvancedCalculatorGUI.exe`
- **Pop-up window interface** with buttons and visual display
- Modern, user-friendly graphical interface
- Point-and-click operation
- Memory and history display
- Real-time expression preview

## Features

### Basic Operations
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Power (^)
- Square Root (√)

### Trigonometric Functions
- Sine (sin) - in degrees
- Cosine (cos) - in degrees  
- Tangent (tan) - in degrees
- Arc Sine (asin) - returns degrees
- Arc Cosine (acos) - returns degrees
- Arc Tangent (atan) - returns degrees

### Logarithmic Functions
- Natural Logarithm (ln)
- Base-10 Logarithm (log10)
- Custom Base Logarithm (log)

### Other Mathematical Functions
- Factorial (!)
- Absolute Value (abs)
- Ceiling (ceil)
- Floor (floor)
- Round to decimal places
- Degrees ↔ Radians conversion

### Memory Functions
- Store in Memory (MS)
- Recall Memory (MR)
- Clear Memory (MC)

### Expression Calculator
Supports complex mathematical expressions with functions like:
- `sin(30) + cos(60) * sqrt(16)`
- `ln(10) + log10(100) - abs(-5)`
- Constants: `pi`, `e`
- Operators: `+`, `-`, `*`, `/`, `^` (power), `()`

## 🎨 GUI Features (Pop-up Window)

### Visual Interface
- **Professional calculator design** with modern styling
- **Large, clear display** showing current number and expression
- **Organized button layout** with color-coded functions:
  - **Blue buttons**: Advanced functions (sin, cos, log, etc.)
  - **Red buttons**: Basic operators (+, -, ×, ÷)
  - **Dark buttons**: Numbers (0-9, decimal point)
  - **Green button**: Equals (=) for final calculation

### Interactive Elements
- **Angle Mode Selector**: Radio buttons to switch between degrees and radians
- **Memory Display**: Shows current memory value
- **History Display**: Shows the last calculated result
- **Expression Preview**: See your calculation as you build it

### Smart Features
- **Error Handling**: Pop-up error messages for invalid operations
- **Window Centering**: Calculator opens in the center of your screen
- **Resizable Window**: Adjust size as needed
- **Professional Appearance**: Clean, modern interface design

## File Structure

```
CALCULATOR/
├── calculator.py              # Console calculator source code
├── calculator_gui.py          # GUI calculator source code
├── requirements.txt           # Python dependencies
├── build.bat                  # Windows build script (console)
├── build_gui.bat             # Windows build script (GUI)
├── build.py                  # Cross-platform build script
├── dist/
│   ├── AdvancedCalculator.exe     # Console executable (~8MB)
│   └── AdvancedCalculatorGUI.exe  # GUI executable (~11MB)
├── build/                     # Build artifacts (can be deleted)
└── README.md                 # This file
```

## Running the Calculator

### Option 1: Run the GUI Executable (Recommended)
Simply double-click on `dist/AdvancedCalculatorGUI.exe` or run it from command line:
```bash
.\dist\AdvancedCalculatorGUI.exe
```
- **Features a beautiful pop-up window interface**
- **No console window appears**
- **Point-and-click operation with buttons**
- **Visual display with memory and history**

### Option 2: Run the Console Executable
Double-click on `dist/AdvancedCalculator.exe` or run from command line:
```bash
.\dist\AdvancedCalculator.exe
```

### Option 3: Run from Source
If you have Python installed:

**GUI Version:**
```bash
python calculator_gui.py
```

**Console Version:**
```bash
python calculator.py
```

## Building from Source

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Build Instructions

#### Windows
**Console Version:**
```bash
.\build.bat
```

**GUI Version (Recommended):**
```bash
.\build_gui.bat
```

#### Cross-platform
**Console Version:**
```bash
python build.py
```

**GUI Version:**
```bash
# Update build.py (already configured for GUI)
python build.py
```

#### Manual Build
**Console Version:**
```bash
pip install pyinstaller
pyinstaller --onefile --name "AdvancedCalculator" calculator.py
```

**GUI Version:**
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "AdvancedCalculatorGUI" calculator_gui.py
```

## Usage Examples

### GUI Version (Pop-up Window)
1. **Launch the executable** - A professional calculator window opens
2. **Click number and operation buttons** - Like a real calculator
3. **View results in the display** - Real-time calculation display
4. **Use advanced functions** - Click sin, cos, log, etc. buttons
5. **Memory operations** - MC (clear), MR (recall), MS (store)
6. **Angle mode** - Switch between degrees and radians
7. **Visual feedback** - See your expression and memory status

### Console Version (Menu Navigation)
The calculator presents a numbered menu (0-26) where you can:
1. Select an operation by entering its number
2. Follow the prompts to enter values
3. View the result
4. Continue with more calculations

### Expression Mode (Option 26)
Enter mathematical expressions directly:
- `2 + 3 * 4` → 14
- `sin(30) + cos(60)` → 1.0
- `sqrt(16) + log10(100)` → 6.0
- `pi * 2^3` → 25.133

### Memory Operations
- Store a result: Choose option 23, enter value
- Recall stored value: Choose option 24
- Clear memory: Choose option 25

## Error Handling

The calculator includes comprehensive error handling for:
- Division by zero
- Invalid input for mathematical functions
- Out-of-range values for trigonometric functions
- Negative inputs for square root and logarithms
- Invalid expressions in expression mode

## Technical Details

### GUI Version
- **Language**: Python 3.13.7 with tkinter
- **Size**: ~11MB standalone executable
- **Interface**: Modern pop-up window with buttons
- **Dependencies**: None (standalone executable)
- **Platform**: Windows (can be compiled for other platforms)
- **Architecture**: 64-bit
- **Features**: Visual calculator interface, no console window

### Console Version
- **Language**: Python 3.13.7
- **Size**: ~8MB standalone executable
- **Interface**: Text-based menu system
- **Dependencies**: None (standalone executable)
- **Platform**: Windows (can be compiled for other platforms)
- **Architecture**: 64-bit
- **Features**: Command-line interface with expression calculator

## Development

The calculator is built using:
- Pure Python with `math` module for mathematical functions
- PyInstaller for creating standalone executable
- Object-oriented design with `AdvancedCalculator` class
- Comprehensive input validation and error handling

## License

This project is open source and available under the MIT License.

## Author

Built as part of a DevOps project demonstrating Python application development and deployment.
