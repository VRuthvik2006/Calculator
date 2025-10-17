# Advanced Calculator - Quick Start Guide

## 🚀 Quick Start

### For GUI Version (Recommended):
1. Navigate to: `C:\Users\Ruthvik\Desktop\DEVOPS_PROJECT\CALCULATOR\dist\`
2. Double-click: `AdvancedCalculatorGUI.exe`
3. Enjoy the pop-up calculator window!

### For Console Version:
1. Navigate to: `C:\Users\Ruthvik\Desktop\DEVOPS_PROJECT\CALCULATOR\dist\`
2. Double-click: `AdvancedCalculator.exe`
3. Use the numbered menu system

## 🎯 Key Features Comparison

| Feature | GUI Version | Console Version |
|---------|-------------|-----------------|
| Interface | Pop-up window with buttons | Text-based menu |
| Ease of Use | Point & click | Type numbers/choices |
| Visual Appeal | Modern, colorful design | Simple text output |
| Memory Display | Always visible | On request |
| File Size | ~11MB | ~8MB |
| Best For | General users, visual learners | Developers, automation |

## 🔧 Advanced Functions Available

- **Trigonometry**: sin, cos, tan, asin, acos, atan
- **Logarithms**: natural log (ln), log base 10, custom base
- **Powers & Roots**: x², x^y, √x
- **Special**: factorial (!), absolute value (|x|)
- **Constants**: π (pi), e (Euler's number)
- **Memory**: Store, recall, clear
- **Angles**: Degrees or radians mode

## 💡 Pro Tips

### GUI Version:
- Use the angle mode radio buttons for trigonometric functions
- Watch the expression display to see your calculation building
- Memory and last result are always visible at the bottom
- Click any advanced function button, then enter your number

### Console Version:
- Use option 26 for complex expression evaluation
- Memory functions are options 23-25
- All trigonometric functions work in degrees by default
- Type expressions like: `sin(30) + cos(60) * sqrt(16)`

## 🛠️ Building Your Own

Want to modify or rebuild the calculator?

1. **Edit the source**: Modify `calculator_gui.py` (GUI) or `calculator.py` (console)
2. **Build GUI version**: Run `build_gui.bat` 
3. **Build console version**: Run `build.bat`
4. **Cross-platform**: Use `python build.py`

The calculator is built with pure Python and tkinter (GUI), making it easy to customize and extend!