# Chemimart Project

This is a ChemiMart Platform that enables businesses to set up and run an online Store

## Setup

Follow the instructions below to set up the project locally on your machine.

### Prerequisites

- Python (version 3.11.4) 
- pip (package manager for Python)
- Virtual environment tool (optional, but recommended)

### Installation

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/Krishh0711/chemimart.git

2. Navigate to the project directory:
   
   ```shell
   cd chemimart

3. Create and activate a virtual environment (optional, but recommended):

   ```shell
   python3 -m venv env         # Create a virtual environment
   source env/bin/activate   # Activate the virtual environment

4. Install project dependencies from the requirements.txt file:

   ```shell
   pip install -r requirements.txt

### Running Project

1. Create media/product_images folder to upload product images. 

   ```shell
   mkdir media # Create a media directory
   cd media    # Navigate to the media directory
   mkdir product_images # Create a product_images directory
   cd ..   # Navigate back to the project root directory

2. Apply database migrations:

   ```shell
   python manage.py migrate

3. Start the development server:

   ```shell
   python manage.py runserver

4. Access the application in your web browser at http://localhost:8000/


### API Details

   For API details refer [this](https://docs.google.com/spreadsheets/d/1bNBefw0jzZ7WwusXcUxZKMVZIi4uT-dXK_IpuYUmIP4/edit?usp=sharing) document.

### High-Level Design 

   Have discussed high-level design of critical features [here](https://docs.google.com/document/d/1E2u4KNTDXW6OIkyRKCUqQqZ3_6Ic9gQJOQavNCJROso/edit?usp=sharing)
