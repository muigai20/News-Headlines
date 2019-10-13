from app import create_app
from flask_script import Manager, Server

# Creating app instance
app = create_app("development")

manage = Manager(app)

manage.add_command("server", Server)

if __name__ == "__main__":
    manage.run()