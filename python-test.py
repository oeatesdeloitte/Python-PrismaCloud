import subprocess
import pickle
import os

# Command Injection vulnerability (CVE-2014-6271, Shellshock)
def run_command(cmd):
    subprocess.call(cmd, shell=True)

# Unsafe deserialization (CVE-2019-11324)
def unsafe_deserialize(data):
    return pickle.loads(data)

# Hardcoded sensitive information
def connect_to_database():
    username = "admin"
    password = "password123"
    # Database connection code here

# Insecure file permissions (CVE-2019-6446)
def create_temp_file():
    with open("tempfile.txt", "w") as f:
        f.write("This is a temporary file.")

# Insecure use of eval (CVE-2016-1000110)
def evaluate_expression(expr):
    return eval(expr)

if __name__ == "__main__":
    # Example usage of the vulnerabilities

    # Command Injection
    run_command("ls -la")

    # Unsafe deserialization
    data = b"cos\nsystem\n(S'echo vulnerable'\ntR."
    unsafe_deserialize(data)

    # Hardcoded credentials
    connect_to_database()

    # Insecure file permissions
    create_temp_file()

    # Insecure eval
    evaluate_expression("1 + 2")
