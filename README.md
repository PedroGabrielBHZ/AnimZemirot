# Zemirot Database Backup

This project is a backup database of Jewish Zemirot, inspired and populated with content from the Zemirot Database. The aim of this project is to safeguard its content in case of the downfall of the mentioned service.

## Project Structure

The project is structured as follows:

- `app.py`: This is the main application file. It sets up the Flask application and defines the routes.
- `songs_model.py`: This file defines the `Song` model and includes methods for loading the database and searching for songs.
- `songs.json`: This file contains the database of songs in JSON format.
- `static/`: This directory contains static files such as CSS and JavaScript files.
- `templates/`: This directory contains the HTML templates for the application.
- `env/`: This directory contains the Python virtual environment for the project.

## Running the Project

To run the project, first activate the virtual environment:

```sh
source env/bin/activate
```

Then run the Flask application:

```sh
python app.py
```

The application will be accessible at `http://localhost:5000`.

## Searching for Songs

You can search for songs by visiting `<http://localhost:5000/songs?q=><search term>`. The search term can be any string, and the application will return all songs that contain the search term in their `lyricsEnglish` or `lyricsTransliterated` fields.
