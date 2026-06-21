# Healthcare Technology Watch CMS

## Project Description

Healthcare Technology Watch CMS is a simple content management system created for the CIS 112 final project.

The project allows employees to submit, review, save, and publish healthcare technology updates. The system stores the submitted updates in a JSON file and automatically generates a static HTML webpage from the saved data.

Healthcare is used as an example industry for this project. The same CMS structure could be adapted for other industries such as education, business, finance, technology, or public services.

## Requirements

- Python 3
- Tkinter (included with most standard Python installations)
- No external packages are required

## Main Features

- Tkinter GUI for adding, updating, deleting, and publishing content
- JSON file used as static data storage
- HTML generator that creates an index.html webpage
- Local web server using server.py
- Separate Python modules and classes for better project organization
- User-friendly web dashboard for reviewing submitted updates

## How to Run the Project

### 1. Run the Content Editor GUI

Open the project in PyCharm.

Run this file:

```bash
python main.py
```

This opens the Tkinter content editor. From the GUI, the user can:

- Add a new healthcare technology update
- Select and update an existing update
- Delete an update
- Clear the form fields
- Generate / publish the HTML webpage

### 2. Run the Local Web Server

Run this file:

```bash
python server.py
```

The server will start on port 8001.

Open this link in a browser:

http://localhost:8001/index.html

The website may also open automatically when server.py is run.

## Project Files

### main.py

Contains the Tkinter GUI. This is the content editor where users can create, update, delete, and publish healthcare technology updates.

### content_item.py

Contains the `TechnologyUpdate` class. This class represents one submitted healthcare technology update.

### cms_manager.py

Handles the CMS data operations, including loading, saving, adding, updating, and deleting records from the JSON file.

### data.json

Stores the submitted healthcare technology updates as static data.

### html_generator.py

Generates the static index.html webpage using the records stored in data.json.

### index.html

The generated website page that displays the healthcare technology updates in a user-friendly dashboard format.

### server.py

Starts a local web server and hosts the generated index.html file.

### favicon.svg

Provides the small browser icon for the website.

## Website Notes

The website displays the submitted healthcare technology updates as review cards. Each card includes:

- Category
- Status
- News title
- Employee name
- Department
- Summary
- Why it matters
- Source link

The Submit, Review, Approve, and Share labels on the website are visual workflow indicators. They are not interactive buttons. The actual content editing actions are performed in the Tkinter GUI.

## Final Project Requirements Covered

This project includes the main required parts of the CIS 112 final project:

- Content Editing GUI
- Static Data Storage using JSON
- HTML webpage generation
- Local server hosting
- Classes and modules

## Author

Selma Boz