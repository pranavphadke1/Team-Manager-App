# Team-Manager-App

This is a team-member-management application implemented with Django.

# Run server

To run this application, first cd into the teamMembersManagement directory:
Open the terminal and type:

- cd teamMembersManagement/

  Then, run the server by typing:

- python manage.py runserver

This should start the server at 'http://127.0.0.1:8000/'

Note, to access the admin page, go to 'http://127.0.0.1:8000/admin/'

- username: pranav
- password: pw

# Documentation:

- The 'team' directory is the app as a whole while the 'teamMembersManagement' directory contains the settings information.
- The model for a team member is the object 'Member' found in 'team/models.py'
- The views are found in 'team/views.py'. I used generic class based views to create four different views (List/Read, Create, Update, Delete).
- Note that I added a forth page, a delete confirmation page, due to the nature of the DeleteView generic class.
- The specific urls for all the pages are found in 'team/urls.py'

## Page Summary

# List Page

The database "teamMembersManagement/db.sqlite3" should already come with two members (Pranav Phadke and Adam Smith).

- To add a new member, click the plus icon in the top right. This will redirect to the Add page at 'http://127.0.0.1:8000/member-create/'
- To edit a current member, click on their profile. This will redirect to the Edit page at 'http://127.0.0.1:8000/member-update/<pk>/', where <pk> is the primary key (id) of the member in the database.

# Add Page

When adding a new member, you must provide the member's first name, last name, email, phone number, and role (defaulted to Regular). If one of these are not provided, a member cannot be added. If you do not want to add a new member, press the "Go back" button in the top right to be redirected to the List Page. To add a new member, press the "Save" button in the bottom right. This will add the new member to the database and redirect to the List Page.

# Edit Page

The Edit Page shows a member's current information and role. They can be changed, but not left blank. To save your edits, press the "Save" button in the bottom right. If you do not want to edit the member, press the "Go back" button in the top right. If you wish to delete a member, press the "Delete" button in the bottom left. This will redirect to a confirmation page at 'http://127.0.0.1:8000/member-delete/<pk>/'.

# Delete Page

This page acts as a confirmation page when you wish to delete a member. If you are certain you want to delete the member, press the "Delete" button. If you do not want to delete the member, press the "Cancel" button.
