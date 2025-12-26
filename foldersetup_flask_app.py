import os

def create_file(path, content=""):
    with open(path, "w") as f:
        f.write(content)

def create_ai_ml_project(project_path):
    folders = [
        "config",
        "models",
        "data/raw",
        "data/processed",
        "notebooks",
        "src",
        "static/css",
        "templates",
        "tests"
    ]

    files = {
        "app.py": """from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    return render_template('result.html', prediction="Sample Prediction")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
""",

        "requirements.txt": "flask\nnumpy\npandas\nscikit-learn\n",

        "Procfile": "web: python app.py",

        "runtime.txt": "python-3.10.12",

        "README.md": "# AI/ML Deployment Project\n\nDeployable on AWS, Heroku, or Azure.",

        ".gitignore": """__pycache__/
env/
venv/
*.pkl
*.pyc
.DS_Store
""",

        "config/config.py": "DEBUG = True\nMODEL_PATH = 'models/model.pkl'\n",

        "src/__init__.py": "",

        "src/preprocessing.py": "# Data preprocessing logic\n",

        "src/train.py": "# Model training logic\n",

        "src/predict.py": "# Prediction logic\n",

        "models/model.pkl": "",

        "static/css/style.css": "body { font-family: Arial; }",

        "templates/layout.html": """<!DOCTYPE html>
<html>
<head>
    <title>AI App</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
""",

        "templates/home.html": """{% extends 'layout.html' %}
{% block content %}
<h1>AI/ML Project</h1>
<form action="/predict" method="post">
    <button type="submit">Predict</button>
</form>
{% endblock %}
""",

        "templates/result.html": """{% extends 'layout.html' %}
{% block content %}
<h2>Prediction Result</h2>
<p>{{ prediction }}</p>
{% endblock %}
""",

        "tests/test_app.py": "# Unit tests\n"
    }

    # Create project root
    os.makedirs(project_path, exist_ok=True)

    # Create folders
    for folder in folders:
        os.makedirs(os.path.join(project_path, folder), exist_ok=True)

    # Create files
    for file, content in files.items():
        file_path = os.path.join(project_path, file)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        create_file(file_path, content)

    print("✅ AI/ML project structure created successfully!")

if __name__ == "__main__":
    project_location = input("Enter full project folder path: ").strip()
    create_ai_ml_project(project_location)
