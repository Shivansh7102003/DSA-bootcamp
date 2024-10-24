# Cloud Storage Deduplication System

This project is a cloud storage deduplication system built with Flask, MySQL, and Python. The application allows users to upload files, checks for duplicates based on file hashes (SHA-256), and manages original and duplicate files efficiently.

## Features

- **File Upload**: Users can upload files, and the system checks for duplicates using SHA-256 hashing.
- **Duplicate Handling**: If a file is detected as a duplicate, it's saved with a unique name indicating its duplicate status.
- **File Management**: Users can view files, check for duplicates, and delete files (original or duplicate).
- **Delete Options**: Users can delete the original file, all duplicates, or only the duplicate files.

## Requirements

To run this project, you need to install the following Python libraries:

### Python Libraries
- [Flask](https://pypi.org/project/Flask/) – for building the web application.
- [MySQL Connector](https://pypi.org/project/mysql-connector-python/) – for connecting and interacting with the MySQL database.
- [Werkzeug](https://pypi.org/project/Werkzeug/) – for securely handling file uploads.

### Additional Tools
- MySQL Workbench (or any other MySQL management tool) for creating and managing the database.

To install the required libraries, run:
```bash
pip install -r requirements.txt
