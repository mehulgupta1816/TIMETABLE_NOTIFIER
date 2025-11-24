# TIMETABLE_NOTIFIER
Vityarthi Project By Mehul Gupta (25BCE10244).

README.md

PROJECT TITLE:  
CLASS TIMETABLE NOTIFIER FOR  STUDENTS

OVERVIEW OF THE PROJECT:

This python program works as a notifier tool for students which notifies them about their class according to their timings. This project aims to develop a simple yet effective Python-based command-line or desktop application to help students manage their schedules and receive timely notifications for classes and important events. The goal is to create a reliable, easy-to-use tool that replaces manual timetable checking and minimizes the chance of missing lectures or deadlines.

FEATURES:

1. Continuous Monitoring: The application runs in a persistent loop (while True), constantly checking the current time against the scheduled events in the timetable.
2. Time-Based Notifications: It triggers a notification precisely when the current system time matches the scheduled time of an entry.
3. Notification Sound:  When the notification pops up it also plays a beep sound along with the notification to drive attention of the user.
4.Prevent Duplicate Alerts: Each scheduled event is tracked using a unique key and stored in the set. This ensures that the user receives the reminder only once per event, per day, preventing notification spam.
5. Daily State Reset: At the change of the day (midnight), the internal notification tracker automatically clears, ensuring that recurring daily events are correctly scheduled and notified again on the new date.

TECHNOLOGIES/TOOLS USED:

1.	Python 3
2.	Libraries like json, time, datetime and os.
3.	Built-in functions like print.
4.	Basic control flow like loops, if-elif-else statements.

STEPS TO INSTALL AND RUN:

1.	Install Python3.
2.	Save file as TIMETABLE_NOTIFIER.py.
3.	Save json file as timetable.json.
4.	Run the program using :python TIMETABLE_NOTIFIER.py.

INSTRUCTION FOR TESTING:

1.	Feed your timetable in the “timetable.json” file including class timings and subject names.
2.	Start the program by clicking on Run.
3.	Check if it gives output line as “Timetable Notifier started”. If yes, the program has started correctly.
4.	Wait for the time of the class according to the timetable file.
5.	Check the notification and the beep sound at the time.

SCREENSHOTS:

<img width="818" height="374" alt="image" src="https://github.com/user-attachments/assets/c51506fb-5fb7-4f22-9e84-45432e894eea" />

<img width="939" height="1446" alt="image" src="https://github.com/user-attachments/assets/bbd2b0ef-e171-4fb0-b2d9-ae58c1e25c03" />

<img width="941" height="389" alt="image" src="https://github.com/user-attachments/assets/a6bd4a35-c422-4b19-b7a3-173457638eee" />

<img width="940" height="1014" alt="image" src="https://github.com/user-attachments/assets/21a0f79e-8d5f-48f4-a6b4-fe39714bb545" />

<img width="944" height="426" alt="image" src="https://github.com/user-attachments/assets/0fe78487-2a56-4cde-8c4a-79a430eca1fd" />

AUTHOR:

MEHUL GUPTA
25BCE10244








                                                                                                         
 


