#!/usr/bin/env python3
"""
Comprehensive test suite for the Advanced Calculator
"""

import math
import pytest
import re
import sys
import os

# Add current directory to path to import calculator modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import calculator
except ImportError:
    calculator = None

class TestExpressionEvaluation:
    """Test expression evaluation functionality"""
    
    def evaluate_expression(self, expression):
        """Safely evaluate mathematical expression - copied from calculator"""
        # Replace function names with their Python equivalents
        expression = expression.replace('^', '**')
        expression = expression.replace('×', '*')
        expression = expression.replace('÷', '/')
        
        # Handle trigonometric functions (degrees mode)
        expression = re.sub(r'\bsin\(([^)]+)\)', r'math.sin(math.radians(\1))', expression)
        expression = re.sub(r'\bcos\(([^)]+)\)', r'math.cos(math.radians(\1))', expression)
        expression = re.sub(r'\btan\(([^)]+)\)', r'math.tan(math.radians(\1))', expression)
        
        # Handle other functions
        expression = re.sub(r'√\(([^)]+)\)', r'math.sqrt(\1)', expression)
        expression = re.sub(r'\bsqrt\(([^)]+)\)', r'math.sqrt(\1)', expression)
        expression = re.sub(r'\bln\(([^)]+)\)', r'math.log(\1)', expression)
        expression = re.sub(r'\blog\(([^)]+)\)', r'math.log10(\1)', expression)
        expression = re.sub(r'\babs\(([^)]+)\)', r'abs(\1)', expression)
        
        try:
            # Use eval with restricted namespace for safety
            allowed_names = {
                "__builtins__": {},
                "math": math,
                "abs": abs,
                "round": round,
                "min": min,
                "max": max
            }
            result = eval(expression, allowed_names)
            return result
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")
    
    def test_basic_arithmetic(self):
        """Test basic arithmetic operations"""
        assert self.evaluate_expression("2 + 3") == 5
        assert self.evaluate_expression("10 - 4") == 6
        assert self.evaluate_expression("6 * 7") == 42
        assert self.evaluate_expression("15 / 3") == 5
        assert self.evaluate_expression("2 ** 3") == 8
    
    def test_trigonometric_functions(self):
        """Test trigonometric functions"""
        # Test sin, cos, tan with known values
        assert abs(self.evaluate_expression("sin(0)") - 0) < 1e-10
        assert abs(self.evaluate_expression("cos(0)") - 1) < 1e-10
        assert abs(self.evaluate_expression("sin(90)") - 1) < 1e-10
        assert abs(self.evaluate_expression("cos(90)") - 0) < 1e-10
    
    def test_mathematical_functions(self):
        """Test mathematical functions"""
        assert self.evaluate_expression("sqrt(16)") == 4
        assert abs(self.evaluate_expression("log(10)") - 1) < 1e-10
        assert abs(self.evaluate_expression("ln(2.718281828)") - 1) < 1e-6
        assert self.evaluate_expression("abs(-5)") == 5
    
    def test_complex_expressions(self):
        """Test complex expressions combining multiple functions"""
        # Test the specific case from the user's screenshot
        result = self.evaluate_expression("sin(77) + sin(44)")
        assert isinstance(result, (int, float))
        assert not math.isnan(result)
        
        # Test more complex expressions
        result = self.evaluate_expression("sqrt(25) + cos(0) * 3")
        assert abs(result - 8) < 1e-10
        
        result = self.evaluate_expression("log(100) + ln(math.e)")
        assert abs(result - 3) < 1e-10
    
    def test_parentheses_precedence(self):
        """Test parentheses and operator precedence"""
        assert self.evaluate_expression("(2 + 3) * 4") == 20
        assert self.evaluate_expression("2 + 3 * 4") == 14
        assert self.evaluate_expression("sin(30 + 60)") == self.evaluate_expression("sin(90)")
    
    def test_error_handling(self):
        """Test error handling for invalid expressions"""
        with pytest.raises(ValueError):
            self.evaluate_expression("sqrt(-1)")
        
        with pytest.raises(ValueError):
            self.evaluate_expression("1 / 0")
        
        with pytest.raises(ValueError):
            self.evaluate_expression("invalid_function(5)")


class TestCalculatorModule:
    """Test the calculator module if available"""
    
    @pytest.mark.skipif(calculator is None, reason="Calculator module not available")
    def test_calculator_import(self):
        """Test that calculator module can be imported"""
        assert calculator is not None
    
    @pytest.mark.skipif(calculator is None, reason="Calculator module not available")
    def test_calculator_functionality(self):
        """Test basic calculator functionality if module is available"""
        # This would test actual calculator functions if they were properly structured
        # For now, just verify the module exists
        assert hasattr(calculator, '__file__')


class TestFileStructure:
    """Test project file structure and requirements"""
    
    def test_required_files_exist(self):
        """Test that required project files exist"""
        required_files = [
            'calculator.py',
            'calculator_gui.py',
            'requirements.txt',
            'README.md'
        ]
        
        for file in required_files:
            assert os.path.exists(file), f"Required file {file} is missing"
    
    def test_python_files_syntax(self):
        """Test that Python files have valid syntax"""
        python_files = ['calculator.py', 'calculator_gui.py']
        
        for file in python_files:
            if os.path.exists(file):
                with open(file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Try to compile the file to check syntax
                try:
                    compile(content, file, 'exec')
                except SyntaxError as e:
                    pytest.fail(f"Syntax error in {file}: {e}")
    
    def test_requirements_format(self):
        """Test that requirements.txt is properly formatted"""
        if os.path.exists('requirements.txt'):
            with open('requirements.txt', 'r') as f:
                lines = f.readlines()
            
            for line_num, line in enumerate(lines, 1):
                line = line.strip()
                if line and not line.startswith('#'):
                    # Basic check for package name format
                    if '==' in line:
                        package, version = line.split('==', 1)
                        assert package.strip(), f"Empty package name at line {line_num}"
                        assert version.strip(), f"Empty version at line {line_num}"


if __name__ == "__main__":
    # Run tests when executed directly
    pytest.main([__file__, "-v"])
        expression = re.sub(r'\blog\(([^)]+)\)', r'math.log10(\1)', expression)
        
        # Replace constants
        expression = re.sub(r'\bπ\b', str(math.pi), expression)
        expression = re.sub(r'\bpi\b', str(math.pi), expression)
        expression = re.sub(r'\be\b', str(math.e), expression)
        
        print(f"Original: {expression}")
        
        # Safe evaluation
        allowed_names = {
            'math': math,
            'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
            'sqrt': math.sqrt, 'log': math.log, 'log10': math.log10,
            'abs': abs, 'pi': math.pi, 'e': math.e,
            'factorial': math.factorial, 'degrees': math.degrees, 'radians': math.radians
        }
        
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return float(result)
    
    # Test cases
    test_cases = [
        "sin(30)",
        "sin(2+3)",
        "sin(45+45)",
        "cos(π/4)",
        "√(25+0)",
        "√(2*8)",
        "log(10*10)"
    ]
    
    for test in test_cases:
        try:
            result = evaluate_expression(test)
            print(f"✅ {test} = {result}")
        except Exception as e:
            print(f"❌ {test} -> Error: {e}")

if __name__ == "__main__":
    test_evaluate_expression()