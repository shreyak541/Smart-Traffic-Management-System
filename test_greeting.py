"""
Test script for the greeting functionality
"""
import sys
import os

# Add src to path for imports  
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from utils.greeting import hello, get_greeting_message


def test_greeting():
    """Test the greeting functions"""
    print("Testing greeting functionality...")
    
    try:
        # Test the message function
        message = get_greeting_message()
        assert isinstance(message, str), "get_greeting_message should return a string"
        assert "Hello" in message, "Greeting message should contain 'Hello'"
        print("✅ get_greeting_message(): PASSED")
        
        # Test the hello function (this will print output)
        result = hello()
        assert isinstance(result, str), "hello() should return a string"
        print("✅ hello() function: PASSED")
        
        return True
        
    except Exception as e:
        print(f"❌ Greeting test failed: {e}")
        return False


if __name__ == "__main__":
    print("🚦 TESTING GREETING FUNCTIONALITY")
    print("=" * 50)
    
    if test_greeting():
        print("=" * 50)
        print("✅ All greeting tests passed!")
    else:
        print("=" * 50)
        print("❌ Some greeting tests failed!")
        exit(1)