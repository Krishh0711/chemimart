# Chemimart Project

This is a Chemimart Platform That Enables Businesses to set up and Run an Online Store

## Setup

Follow the instructions below to set up the project locally on your machine.

### Prerequisites

- Python (version 3.11.4) 
- pip (package manager for Python)
- Virtual environment tool (optional, but recommended)

### Installation

1. Clone the repository to your local machine:

   ```shell
   https://github.com/Krishh0711/chemimart.git

2. Navigate to the project directory:
   
   ```shell
   cd chemimart

3. Create and activate a virtual environment (optional, but recommended):

   ```shell
   python -m venv env         # Create a virtual environment
   source env/bin/activate   # Activate the virtual environment

4. Install project dependencies from the requirements.txt file:

   ```shell
   pip install -r requirements.txt

### Running Project

1. Apply database migrations:

   ```shell
   python manage.py migrate

2. Start the development server:

   ```shell
   python manage.py runserver

3. Access the application in your web browser at http://localhost:8000/


### API Details

   For API details refer [this](https://docs.google.com/spreadsheets/d/1bNBefw0jzZ7WwusXcUxZKMVZIi4uT-dXK_IpuYUmIP4/edit?usp=sharing) document.
