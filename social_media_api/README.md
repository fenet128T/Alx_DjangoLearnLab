This module adds core social media functionality, allowing users to create posts and engage with them via comments. It includes full CRUD (Create, Read, Update, Delete) capabilities with author-level permissions.

🚀 Features
Posts: Users can create, edit, and delete their own posts.

Comments: Users can comment on any post and manage their own comments.

Permissions: Only the author of a post or comment can modify or delete it.

Search: Built-in filtering to search posts by title or content.

Pagination: Results are paginated (10 per page) to ensure high performance.




Social Media API - Follows & Feed:::

This update introduces user-to-user relationships and a personalized content feed.

New Features:::::
Follow System: Users can follow/unfollow others to curate their network.

Dynamic Feed: A personalized list of posts from followed users, sorted by the most recent.

Self-Follow Protection: Logic prevents users from following their own accounts.





Deployment Guide:::
This document outlines the steps taken to deploy the Social Media API to a production environment.

🚀 Production Configuration
Hosting Provider: Render / Heroku

Web Server: Gunicorn (WSGI)

Database: PostgreSQL (Managed Service)

Static Files: Managed via WhiteNoise and collectstatic.

🛠️ Security Checklist
[x] DEBUG set to False.

[x] SECRET_KEY pulled from environment variables.

[x] Security headers (HSTS, XSS Filter) enabled.

[x] HTTPS redirection enforced.