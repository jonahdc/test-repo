import subprocess
import shlex
from typing import List, Optional

# Whitelist of allowed commands
ALLOWED_COMMANDS = {
    'ls': ['-l', '-a', '-h'],
    'echo': None,  # None means all arguments are allowed
    'pwd': [],     # Empty list means no arguments allowed
}

def validate_command(command: str, args: List[str]) -> bool:
    """Validate if a command and its arguments are allowed."""
    # Check for shell metacharacters in command and args
    shell_metacharacters = ['|', '&', ';', '(', ')', '<', '>', '$', '`', '\\']
    if any(char in command for char in shell_metacharacters):
        return False
    if any(any(char in arg for char in shell_metacharacters) for arg in args):
        return False
        
    if command not in ALLOWED_COMMANDS:
        return False
        
    allowed_args = ALLOWED_COMMANDS[command]
    if allowed_args is None:
        return True
    
    return all(arg in allowed_args for arg in args if arg.startswith('-'))

def secure_execute_command(user_input: str) -> Optional[str]:
    """
    Securely execute a command with validation.
    Returns command output if successful, None if command is not allowed.
    """
    try:
        # Split the input into command and arguments safely
        parts = shlex.split(user_input)
        if not parts:
            return None
            
        command = parts[0]
        args = parts[1:] if len(parts) > 1 else []
        
        # Validate the command and arguments
        if not validate_command(command, args):
            return None
            
        # Execute the command safely without shell=True
        result = subprocess.run(
            parts,
            capture_output=True,
            text=True,
            shell=False,
            check=True
        )
        return result.stdout
        
    except (subprocess.SubprocessError, ValueError):
        return None

def hello_world():
    """Original function preserved for compatibility"""
    print("hello world");
