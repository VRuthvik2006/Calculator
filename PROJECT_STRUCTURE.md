# 📁 Project Structure

## 🏗️ **Advanced Calculator - Organized File Structure**

```
CALCULATOR/
├── 📁 src/                     # Source Code
│   ├── calculator.py           # Console calculator with advanced functions
│   └── calculator_gui.py       # GUI calculator with tkinter interface
│
├── 📁 tests/                   # Test Suite
│   ├── test_calculator.py      # Comprehensive test suite
│   └── test_expressions.py     # Expression evaluation tests
│
├── 📁 docs/                    # Documentation
│   ├── README.md               # Main project documentation
│   ├── CI_CD_SETUP.md         # CI/CD pipeline documentation
│   ├── IMPLEMENTATION_COMPLETE.md # Implementation summary
│   ├── QUICK_START.md          # Quick start guide
│   ├── CURSOR_FEATURES.md      # Cursor positioning features
│   ├── DISPLAY_ENHANCEMENTS.md # Display improvements
│   ├── DISPLAY_FIX.md          # Display fixes
│   ├── DUAL_DISPLAY_UPDATE.md  # Display system updates
│   ├── FUNCTION_EXPRESSIONS.md # Function expression handling
│   ├── FUNCTION_FIX.md         # Function fixes
│   ├── GEOMETRY_FIX.md         # GUI geometry fixes
│   └── UPDATE_NOTES.md         # Update notes
│
├── 📁 scripts/                 # Setup & Utility Scripts
│   ├── setup_git.py            # Python Git setup script
│   └── setup_git.ps1           # PowerShell Git setup script
│
├── 📁 build_tools/             # Build Configuration
│   ├── build.py                # Python build script
│   ├── build.bat               # Batch build script
│   ├── build_gui.bat           # GUI build script
│   ├── AdvancedCalculator.spec # PyInstaller spec (console)
│   └── AdvancedCalculatorGUI.spec # PyInstaller spec (GUI)
│
├── 📁 .github/workflows/       # CI/CD Pipeline
│   ├── ci-cd.yml               # Main CI/CD workflow
│   ├── maintenance.yml         # Scheduled maintenance
│   └── pr-validation.yml       # Pull request validation
│
├── 📁 dist/                    # Built Executables (generated)
├── 📁 build/                   # Build Cache (generated)
├── 📁 __pycache__/             # Python Cache (generated)
├── 📁 .pytest_cache/           # Test Cache (generated)
│
├── .gitignore                  # Git ignore rules
├── requirements.txt            # Python dependencies
└── PROJECT_STRUCTURE.md        # This file
```

## 📖 **Directory Descriptions**

### **📁 src/** - Source Code
Contains the main application code:
- **calculator.py**: Console-based calculator with full mathematical functions
- **calculator_gui.py**: GUI calculator with advanced features and professional interface

### **📁 tests/** - Test Suite
Comprehensive testing framework:
- **test_calculator.py**: Main test suite with 11+ test cases
- **test_expressions.py**: Expression evaluation and function testing

### **📁 docs/** - Documentation
Complete project documentation:
- **README.md**: Main project overview and usage instructions
- **CI_CD_SETUP.md**: Detailed CI/CD pipeline documentation
- **IMPLEMENTATION_COMPLETE.md**: Complete implementation summary
- Feature-specific documentation files for development history

### **📁 scripts/** - Setup & Utilities
Automation and setup scripts:
- **setup_git.py**: Cross-platform Git repository setup
- **setup_git.ps1**: Windows PowerShell setup script

### **📁 build_tools/** - Build Configuration
Build system and configuration:
- **build.py**: Python-based build automation
- **build.bat / build_gui.bat**: Windows batch build scripts
- **\*.spec**: PyInstaller configuration files

### **📁 .github/workflows/** - CI/CD Pipeline
GitHub Actions workflows:
- **ci-cd.yml**: Main pipeline (testing, building, security, backup)
- **maintenance.yml**: Scheduled maintenance and dependency checks
- **pr-validation.yml**: Pull request validation and testing

## 🎯 **Benefits of This Structure**

### **✅ Clean Organization**
- Logical separation of concerns
- Easy navigation and file location
- Professional project structure

### **✅ Development Efficiency**
- Clear distinction between source code and documentation
- Separate testing environment
- Dedicated build tools section

### **✅ Maintainability**
- Easy to find and update specific components
- Clear separation of configuration files
- Organized documentation for easy reference

### **✅ CI/CD Integration**
- Workflows can target specific directories
- Testing scripts know where to find source code
- Build tools are centrally organized

### **✅ Scalability**
- Easy to add new source files
- Documentation can grow without cluttering
- Build system can be extended easily

## 🚀 **Usage**

### **Running the Calculator**
```bash
# Console version
python src/calculator.py

# GUI version (if running from source)
python src/calculator_gui.py
```

### **Running Tests**
```bash
# From project root
python -m pytest tests/ -v

# Specific test file
python -m pytest tests/test_calculator.py -v
```

### **Building Executables**
```bash
# Using build scripts
python build_tools/build.py

# Or batch files (Windows)
build_tools/build_gui.bat
```

### **Git Setup**
```bash
# Using setup scripts
python scripts/setup_git.py
# or
scripts/setup_git.ps1
```

## 📋 **Project Status**

- ✅ **Source Code**: Organized in src/
- ✅ **Testing**: Comprehensive test suite in tests/
- ✅ **Documentation**: Complete docs in docs/
- ✅ **Build System**: Automated build tools
- ✅ **CI/CD**: Full GitHub Actions pipeline
- ✅ **Structure**: Professional organization complete

This organized structure makes the Advanced Calculator project enterprise-ready and easy to maintain! 🎉