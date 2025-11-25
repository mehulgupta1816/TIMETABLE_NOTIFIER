
PROBLEM STATEMENT:

Students or professionals often miss important classes, meetings, or scheduled events because they rely solely on static, easy-to-forget paper timetables or require manual checking of digital calendars. This leads to missed learning opportunities, professional commitments and events, and wasted time due to being unprepared or late.

SCOPE OF THE PROJECT:

This project offers:
•	The program will offer command-line or basic script-level methods to start, stop, or reload the timetable file.

•	The program will contain a scheduling thread that continuously checks the current system time against the events listed in the loaded timetable.

•	The program will read timetable data from a simple structured file which the user must create and maintain. The data must include Event Name and Time.

TARGET USERS:

This program targets user bases including:

1.	Students : For Timetable
2.	Working : For Event and Meeting Schedule
3.	Teachers and Professors: For lecture reminders.

HIGH LEVEL FEATURES:

1.	Data Input: 

File Reading: The ability to read and process a static, structured timetable file in a  JSON format.

Data Structure Mapping: Converting the raw file data into a usable, internal Python data structure that can be easily queried by the scheduler.

2.	Time Monitoring and Scheduling Engine (TMSE):

Daily Filter: The engine first checks the current day of the week and filters the entire timetable to only the events scheduled for that specific day.

Time Comparison: For the filtered events, it constantly calculates the difference between the current system time and the event's time.

Notification Trigger: It triggers the notification feature when the calculated time difference exactly matches the user's pre-set lead time.

AUTHOR:

MEHUL GUPTA
25BCE10244








