import os
import subprocess
import sys

def install_requirements():
    """Install required packages from requirements.txt"""
    print("Installing required packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("Packages installed successfully!")

def set_api_key():
    """Set the Cerebras API key as an environment variable"""
    api_key = input("Enter your Cerebras API key (or press Enter to use the fallback key): ").strip()
    if api_key:
        os.environ["CEREBRAS_API_KEY"] = api_key
        print("API key set successfully!")
    else:
        print("Using fallback API key (less secure)...")

def run_application():
    """Run the Flask application"""
    print("Starting the Flask application...")
    print("Access the application at:")
    print("- Local: http://localhost:5000")
    print("- Network: http://your_machine_ip:5000")
    print("\nPress CTRL+C to stop the application.")
    
    # Import and run the app
    from app import app
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    print("LLaMA Chatbot Deployment Script")
    print("=" * 30)
    
    try:
        install_requirements()
        set_api_key()
        run_application()
    except KeyboardInterrupt:
        print("\nApplication stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
