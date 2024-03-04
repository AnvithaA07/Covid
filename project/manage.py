from flask.cli import FlaskGroup
from main import app, db  # Assuming your Flask app is defined in a file named main.py

cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()
