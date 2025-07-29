# Appointment Reminder App

## Running the app
1. Complete the Developer Setup (See `DEVELOPER_SETUP.md`)
2. Launch the app from the terminal:

       flask --app flaskr run --debug

   *Or* by using Docker:

       docker build --tag 'appt_reminder' .

       docker run -p 5000:5000 appt_reminder:latest

3. In your browser:
    - Go to localhost:5000/hello
    - You should see 'Hello, World!' in your browser window