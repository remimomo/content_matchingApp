# Content Recommender Application

## Setup

1. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Save the JSON data into `users.json` and `content.json` in the root directory, or use the upload feature on the webpage.

4. Run the application:
    ```bash
    python app.py
    ```

5. Open a web browser and go to `http://127.0.0.1:5000` to view the content recommendations.

6. To upload new JSON files, use the file upload form on the webpage.

## Running Tests

Run the tests with:
```bash
python -m unittest discover -s app/tests
