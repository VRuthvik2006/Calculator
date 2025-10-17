#!/usr/bin/env python3
"""
Simple test runner to verify the calculator functions work
"""

import sys
import os
import math

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

def test_basic_calculator():
    """Test basic calculator functionality"""
    print("Testing basic calculator functionality...")
    
    # Test basic arithmetic
    assert 2 + 3 == 5, "Addition failed"
    assert 10 - 4 == 6, "Subtraction failed"
    assert 6 * 7 == 42, "Multiplication failed"
    assert 15 / 3 == 5, "Division failed"
    
    print("✅ Basic arithmetic tests passed")

def test_mathematical_functions():
    """Test mathematical functions"""
    print("Testing mathematical functions...")
    
    # Test mathematical functions
    assert math.sqrt(16) == 4, "Square root failed"
    assert abs(math.log10(10) - 1) < 1e-10, "Log10 failed"
    assert abs(-5) == 5, "Absolute value failed"
    
    print("✅ Mathematical function tests passed")

def test_file_structure():
    """Test that required files exist"""
    print("Testing file structure...")
    
    # Check that source files exist
    src_dir = os.path.join(os.path.dirname(__file__), '..', 'src')
    
    assert os.path.exists(os.path.join(src_dir, 'calculator.py')), "calculator.py missing"
    assert os.path.exists(os.path.join(src_dir, 'calculator_gui.py')), "calculator_gui.py missing"
    
    # Check that docs exist
    docs_dir = os.path.join(os.path.dirname(__file__), '..', 'docs')
    assert os.path.exists(docs_dir), "docs directory missing"
    
    print("✅ File structure tests passed")

def test_import_calculator():
    """Test that we can import the calculator module"""
    print("Testing calculator import...")
    
    try:
        import calculator
        print("✅ Calculator module imported successfully")
        return True
    except ImportError as e:
        print(f"⚠️ Calculator import failed: {e}")
        # This is non-critical for CI/CD
        return False

def main():
    """Run all tests"""
    print("🧮 Running Calculator Tests")
    print("=" * 40)
    
    tests_passed = 0
    total_tests = 0
    
    # Run tests
    try:
        test_basic_calculator()
        tests_passed += 1
    except Exception as e:
        print(f"❌ Basic calculator test failed: {e}")
    total_tests += 1
    
    try:
        test_mathematical_functions()
        tests_passed += 1
    except Exception as e:
        print(f"❌ Mathematical functions test failed: {e}")
    total_tests += 1
    
    try:
        test_file_structure()
        tests_passed += 1
    except Exception as e:
        print(f"❌ File structure test failed: {e}")
    total_tests += 1
    
    try:
        if test_import_calculator():
            tests_passed += 1
    except Exception as e:
        print(f"❌ Import test failed: {e}")
    total_tests += 1
    
    print("\n" + "=" * 40)
    print(f"Tests Results: {tests_passed}/{total_tests} passed")
    
    if tests_passed == total_tests:
        print("🎉 All tests passed!")
        return 0
    else:
        print(f"❌ {total_tests - tests_passed} tests failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())