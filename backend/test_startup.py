from app import create_app
app = create_app()
print("App created successfully!")
import app as app_module
print(f"DB URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
