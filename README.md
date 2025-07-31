# LinkShortner

This is a simple URL shortener web application built with Flask and SQLite. It allows users to submit long URLs and generates short URLs that redirect to the original links. The app stores the URL mappings in a local SQLite database.

## Features

- Submit a long URL via a web form.
- Generate a unique short ID for each URL.
- Store the short ID and full URL in an SQLite database.
- Redirect short URLs to the original full URLs.
- Simple and clean user interface with HTML templates.

## How It Works

1. The user visits the home page (`/`) and submits a long URL through the form.
2. The app generates a random 6-character short ID consisting of letters and digits.
3. The short ID and full URL are saved in the `urls` table of the SQLite database (`urls.db`).
4. The app displays the shortened URL to the user.
5. When the shortened URL is accessed (`/<short_id>`), the app looks up the full URL in the database and redirects the user to it.
6. If the short ID is not found, the app returns a 404 error.

## Project Structure

- `app.py`: Main Flask application code.
- `urls.db`: SQLite database file storing URL mappings.
- `templates/`: HTML templates for the home page (`index.html`) and result page (`result.html`).

## Requirements

- Python 3.x
- Flask
- SQLite3 (usually included with Python)

## Setup and Running

1. Install Flask if not already installed:

   ```
   pip install flask
   ```

2. Run the application:

   ```
   python app.py
   ```

3. Open your browser and go to `http://localhost:5000` to use the app.

## Notes

- The app generates short URLs based on the host URL where it is running. If running locally, the short URLs will only work on your machine.
- To make the app accessible worldwide, deploy it on a public server or use services like Heroku or ngrok.
- The database is a simple SQLite file and may not be suitable for high-traffic production use.

## License

This project is open source and free to use.
