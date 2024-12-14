# Dela Paz Pulot Aplaya Health Center Management System

## Project Overview
The Dela Paz Pulot Aplaya Health Center Management System is a desktop application designed to efficiently manage patient health records. It provides healthcare workers with an intuitive interface to add, update, delete, and search for patient information, ensuring that vital health data is easily accessible and well-organized. The system aims to improve healthcare delivery and promote better health outcomes in the community.

## Python Concepts and Libraries Used
This project utilizes several key Python concepts and libraries:
- **Tkinter**: The primary library used for creating the graphical user interface (GUI). It allows for the design of windows, buttons, and input fields, making the application user-friendly.
- **Pymysql**: This library is used to connect to a MySQL database, enabling the application to perform CRUD (Create, Read, Update, Delete) operations on patient records stored in the database.
- **Data Handling**: Python's built-in data structures (like lists and dictionaries) are used to manage and manipulate patient data efficiently.
- **Error Handling**: The application incorporates error handling to manage user input and database operations, ensuring a smooth user experience.

## Chosen Sustainable Development Goal (SDG)
This project aligns with **Sustainable Development Goal 3 (SDG 3)**, which aims to ensure healthy lives and promote well-being for all at all ages. The system supports this goal by:
- **Improving Access to Health Information**: By providing a centralized platform for managing patient records, healthcare workers can easily access and update vital health information, leading to better patient care.
- **Promoting Health Equity**: The application is designed to be user-friendly, making it accessible to healthcare workers in underserved communities, thereby promoting equitable access to health services.
- **Supporting Health Initiatives**: The system can facilitate various health programs, such as vaccination drives and health education campaigns, contributing to overall community health improvement.

## Instructions for Running the Program
**Login to the System**
Login Window: Upon launching, you will see the login window.
**Enter Credentials:**
Username: Type BHW
Password: Type 1234
Click the "Login" Button: If the credentials are correct, you will be directed to the main application interface. If not, an error message will prompt you to enter the correct credentials.
Step 3: Main Application Interface
Once logged in, you will see the main interface where you can manage patient records.

**Features:**
Add Patient Record:

Fill in the required fields:
ID
Name
Phone Number
Date of Birth
Age
Gender
Weight
Height
Health Condition
Medicine
Click the "Add" button to save the new record. If any fields are empty, an error message will prompt you to fill them in.
Update Patient Record:

**Select a record from the displayed table.**
Modify the fields as needed.
Click the "Update" button to save the changes. Ensure the ID remains unique; otherwise, an error message will appear.
Delete Patient Record:

**Select a record from the table**.
Click the "Delete" button and confirm the deletion when prompted.
Search for Patient Record:

**Enter any known details (ID, Name, etc.) in the respective fields.**
Click the "Search" button to find and display the record. If no data is found, an error message will inform you.
Reset Database:

Click the "Reset" button to delete all records in the database. Confirm the action when prompted.
Clear Input Fields:

Click the "Clear" button to reset all input fields to empty
