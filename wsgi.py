import sys
import os

# Add the current directory and backend directory to sys.path
root_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(root_dir)
sys.path.append(os.path.join(root_dir, 'backend'))

from backend.app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
