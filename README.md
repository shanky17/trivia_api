# Trivia API

This is a Django-based API for managing trivia questions and answers.

## Project Structure

```
trivia_api/
├── db.sqlite3
├── manage.py
├── trivia/
│   ├── **init**.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   ├── **init**.py
│   │   └── 0001_initial.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── trivia_api/
    ├── **init**.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/shanky17/trivia_api.git
   cd trivia_api
   ```

2. **Create a virtual environment and activate it:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Apply the migrations:**

   ```sh
   python manage.py migrate
   ```

5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

## API Endpoints

- **Questions:**
  - `GET /api/v1/questions/` - List all questions
  - `GET /api/v1/questions/{id}/` - Retrieve a specific question
