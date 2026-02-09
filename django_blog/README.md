Registration

User fills form → RegisterForm validates → user saved → logged in automatically.

Login

Uses Django’s built-in LoginView.

Logout

Uses Django’s built-in LogoutView.

Profile

Protected using @login_required.
Users can update their email.