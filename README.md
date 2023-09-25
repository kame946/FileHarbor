# FileHarbor

FileHarbor is a user-friendly web application that allows authenticated users to securely upload and manage files. It provides a seamless experience for users to store and share their files while maintaining data security.


## Features

- User registration with profile pictures.
- Secure authentication and password hashing.
- Easy file upload with a user-friendly interface.
- File storage in a secure and organized manner.
- Real-time feedback on successful uploads.
- Logout feature for user convenience.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fileharbor.git
   cd fileharbor
    ```
2. Create a virtual environment (optional but recommended):
   ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Access the application at http://localhost:8000/ in your web browser.
