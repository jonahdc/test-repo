import unittest
import sys
import os
import importlib.util

# Load the module with the dash in the name
spec = importlib.util.spec_from_file_location("valid_file", 
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "valid-file.py"))
valid_file = importlib.util.module_from_spec(spec)
spec.loader.exec_module(valid_file)

secure_execute_command = valid_file.secure_execute_command

class TestSecureCommand(unittest.TestCase):
    def test_allowed_command(self):
        # Test allowed command
        result = secure_execute_command("echo hello")
        self.assertIsNotNone(result)
        self.assertIn("hello", result)

    def test_disallowed_command(self):
        # Test disallowed command
        result = secure_execute_command("rm -rf /")
        self.assertIsNone(result)

    def test_command_injection(self):
        # Test command injection attempts
        result = secure_execute_command("echo hello; rm -rf /")
        self.assertIsNone(result)
        
        result = secure_execute_command("echo hello && ls")
        self.assertIsNone(result)
        
        result = secure_execute_command("echo `rm -rf /`")
        self.assertIsNone(result)  # Backticks are properly blocked
        
        # Test that regular safe commands still work
        result = secure_execute_command("echo 'hello world'")
        self.assertIsNotNone(result)
        self.assertIn("hello world", result)
        
    def test_allowed_ls(self):
        # Test allowed ls command with valid flags
        result = secure_execute_command("ls -l")
        self.assertIsNotNone(result)
        
    def test_ls_invalid_flags(self):
        # Test ls command with invalid flags
        result = secure_execute_command("ls --delete")
        self.assertIsNone(result)

if __name__ == '__main__':
    print("Starting tests...")
    try:
        # Run a single test first to debug
        suite = unittest.TestLoader().loadTestsFromTestCase(TestSecureCommand)
        test = unittest.TextTestRunner(verbosity=2).run(suite)
        print(f"Tests run: {test.testsRun}")
        print(f"Failures: {len(test.failures)}")
        print(f"Errors: {len(test.errors)}")
        if test.failures:
            print("\nFailures:")
            for failure in test.failures:
                print(failure[1])
        if test.errors:
            print("\nErrors:")
            for error in test.errors:
                print(error[1])
    except Exception as e:
        print(f"Test execution error: {str(e)}")