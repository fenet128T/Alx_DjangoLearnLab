Registration
User fills form → RegisterForm validates → user saved → logged in automatically.

Login:
Uses Django’s built-in LoginView.

Logout:
Uses Django’s built-in LogoutView.

Profile:
Protected using @login_required.
Users can update their email.


Tagging:

..Tags are comma-separated during post creation/editing.
..Clicking a tag filters posts by that tag.

Search:

..Use search bar.
..Search matches title, content, and tags.
..Uses Django Q objects for filtering.

Features
Dynamic Content: Authenticated users can create new posts through the /post/new/ endpoint.

Security Mixins: Implemented LoginRequiredMixin and UserPassesTestMixin to protect data. Only the original author of a post has permission to edit or delete it.

CBV Architecture: Utilizes Django's class-based views (ListView, DetailView, etc.) for clean, maintainable logic.