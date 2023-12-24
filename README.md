# Ship Tracking System

This project implements a ship tracking system using a sqlite as a relational database and a Django-based REST API. It includes functionalities to load ship positions from a CSV file into a database and expose endpoints to retrieve information about ships and their positions.

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

Install required Python packages:

    ```
    pip install -r requirements.txt
    ```

### Loading CSV Data

1. Place your CSV file containing vessel positions in the project directory.

2. Run the data loading script:

    ```bash
    python manage.py add_positions <csv file path>
    ```

### Running the Django App

1. Run the Django application:

    ```
    python manage.py runserver
    ```

2. Access the API endpoints:

    - Ships: http://127.0.0.1:8000/api/ships/
    - Positions (replace `<imo number>` with the actual IMO number): http://127.0.0.1:8000/api/positions/?imo=<imo number>
