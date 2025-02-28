import subprocess

def run_terraform():
    try:
        # Initialize Terraform
        subprocess.run(["terraform", "init"], check=True)

        # Apply Terraform (Auto-approve)
        subprocess.run(["terraform", "apply", "-auto-approve"], check=True)

        print("EC2 Instance created successfully!")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_terraform()
