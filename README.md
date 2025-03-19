# ScrapBridge

This project is a Django-based web application.

## Installation

To install and use this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/username/myproject.git
   cd myproject

   python -m venv venv  # For Linux/macOS
   python -m venv venv.bat  # For Windows
   
2. For Linux/macOS:
    ```bash
      source venv/bin/activate

3. For Windows:
    ```bash
      .\venv\Scripts\activate

4. Install the dependencies:
    ```bash
      pip install -r requirements.txt

5. Apply database migrations:
    ```bash
      python manage.py migrate
    
6. Run the development server:
    ```bash
      python manage.py runserver
    
** Visit http://localhost:8000 in your web browser. **
