# appt_reminder
This app generates appointment reminders

## installation

1. Create a Python virtual environment:

    python3 -m venv venv

2. Switch to the virtual environment and install dependencies from `requirements.txt`:

    source venv/bin/activate
    python -m pip install -r requirements.txt

3. Set up the required configuration file, with the connection info to your MySQL or MariaDB instance.  Its location should be `~/Documents/projects/proj_configs/conf/appt_reminder.config` or change that location in `/app/db/engine.py`.

4. Now you can run the application:

    python run.py

