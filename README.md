# ScrapBridge
I developed *Scrap Bridge*, an advanced waste management platform that connects users with scrap collectors, I built the **login/signup system**, allowing users and collectors to authenticate securely.  

To enhance efficiency, I integrated a **deep learning-based CNN model** to classify different types of scrap automatically. I also implemented the **scrap pickup request system**, where users can submit requests, and collectors can accept or reject them. Additionally, I developed a **real-time notification system** to keep users informed about request status updates.  

The platform was structured using **Django for the backend**, a **responsive frontend**, and a **database** for storing user and request data. Through continuous testing and optimization, I ensured high accuracy in scrap classification and smooth request handling, making *Scrap Bridge* a reliable and scalable solution for waste management.

## Installation
To install and use this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/username/myproject.git

2. Navigate to the project directory:
   ```bash
      cd myproject
   
3. Create a virtual environment:
   ```bash
      python -m venv venv  # For Linux/macOS
      python -m venv venv.bat  # For Windows
   
4. For Linux/macOS:
    ```bash
      source venv/bin/activate

5. For Windows:
    ```bash
      .\venv\Scripts\activate

6. Install the dependencies:
    ```bash
      pip install -r requirements.txt

7. Apply database migrations:
    ```bash
      python manage.py migrate
    
8. Run the development server:
    ```bash
      python manage.py runserver
    
# Visit http://localhost:8000 in your web browser.

# A Short Look To ScrapBridge

