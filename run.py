# run.py
from flask import Flask
from app.services.students.routes import students_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(students_bp, url_prefix="/students")
    return app    

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
