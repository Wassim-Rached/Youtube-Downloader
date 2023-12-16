# YouTube Downloader with Django
## Overview

This Django app leverages the 'pytube' library to create a simple YouTube downloader.

## Features

- Users can input YouTube video URLs.

- The app fetches and downloads videos securely.

- Diffrent Video download quality specific download.

## Setup

**Clone the repository:**
  ```bash
    git clone https://github.com/Wassim-Rached/youtube-downloader
  ```
**Install the required dependencies:**
  ```bash
    pip install -r requirements.txt
  ```
**Run migrations:**
```bash
  python manage.py migrate
```
**Start the Django development server:**
```bash
  python manage.py runserver
```

## Usage

- Visit the app in your browser at [http://localhost:8000](http://localhost:8000)

- Input YouTube video URLs.

- Submit the form to download videos securely.

## Security

- Validate user input to prevent abuse.

- Implement measures to ensure a secure download process.

#

**Feel free to contribute and enhance this YouTube downloader with Django!**
