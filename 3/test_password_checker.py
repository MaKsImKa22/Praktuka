import unittest
import tempfile
import os
from main import load_common_passwords, find_weak_passwords

class TestPasswordChecker(unittest.TestCase):

    def setUp(self):
        """Set up test data before each test"""
        self.test_users = {
            "user1": "123456",
            "user2": "password", 
            "user3": "qwerty",
            "user4": "securepassword123",
            "user5": "letmein"
        }
        
        # Create a temporary wordlist file for testing
        self.common_passwords = {"123456", "password", "qwerty", "letmein", "admin"}

    def test_load_common_passwords_success(self):
        """Test loading common passwords from existing file"""
        # Create temporary file
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("123456\npassword\nqwerty\nletmein\nadmin\n")
            temp_path = f.name
        
        try:
            result = load_common_passwords(temp_path)
            self.assertEqual(result, self.common_passwords)
        finally:
            os.unlink(temp_path)

    def test_load_common_passwords_file_not_found(self):
        """Test loading from non-existent file"""
        result = load_common_passwords("non_existent_file.txt")
        self.assertEqual(result, set())
        
    def test_load_common_passwords_empty_file(self):
        """Test loading from empty file"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            temp_path = f.name
        
        try:
            result = load_common_passwords(temp_path)
            self.assertEqual(result, set())
        finally:
            os.unlink(temp_path)

    def test_find_weak_passwords_found(self):
        """Test finding weak passwords when they exist"""
        result = find_weak_passwords(self.test_users, self.common_passwords)
        
        expected = {
            "user1": "123456",
            "user2": "password",
            "user3": "qwerty", 
            "user5": "letmein"
        }
        self.assertEqual(result, expected)
        
    def test_find_weak_passwords_none_found(self):
        """Test when no weak passwords are found"""
        strong_users = {
            "user1": "StrongPass123!",
            "user2": "AnotherSecurePass456"
        }
        
        result = find_weak_passwords(strong_users, self.common_passwords)
        self.assertEqual(result, {})
        
    def test_find_weak_passwords_empty_input(self):
        """Test with empty users dictionary"""
        result = find_weak_passwords({}, self.common_passwords)
        self.assertEqual(result, {})
        
    def test_find_weak_passwords_case_sensitivity(self):
        """Test case sensitivity in password matching"""
        users = {"user1": "PASSWORD"}  # uppercase
        result = find_weak_passwords(users, self.common_passwords)
        # Should not match because "password" is lowercase in wordlist
        self.assertEqual(result, {})

if __name__ == "__main__":
    unittest.main()