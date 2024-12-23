# Pollogram-API

Pollogram-API is a backend API for an Instagram clone project, designed using Django and Django REST Framework (DRF). It provides endpoints to manage users, profiles, posts, and comments.

---

## Features

- User Management: Register, authenticate, and manage user accounts.
- Profile Management: Create, view, and update user profiles.
- Post Management: Upload, edit, and view posts.
- Comment System: Add, edit, and manage comments on posts.

## Endpoints

| Endpoint       | Description                     |
| -------------- | ------------------------------- |
| /api/user/     | Manage user-related operations. |
| /api/profile/  | View and edit user profiles.    |
| /api/posts/    | CRUD operations for posts.      |
| /api/comments/ | Manage comments on posts.       |

### /api/user/

| Endpoint          | Description          |
| ----------------- | -------------------- |
| /                 | Get user info        |
| /signup/          | Signup new user      |
| /login/           | Login user           |
| /refresh/         | Refresh auth token   |
| /verify/          | Verify auth token    |
| /change-password/ | Change user password |

### /api/profile/

| Endpoint                     | Description                                        |
| ---------------------------- | -------------------------------------------------- |
| /                            | Get Profiles list                                  |
| /current-user/               | Get current user profile detailed view             |
| /current-user/profile-image/ | Update current user's profile image                |
| /:pk/                        | Get user profile detailed view based on profile id |
| /:pk/follow/                 | Follow user profile with profile id                |
| /:pk/unfollow/               | Unfollow user profile with profile id              |

### /api/posts/

| Endpoint     | Description                                             |
| ------------ | ------------------------------------------------------- |
| /            | GET: retrieve posts list, POST: Create new post         |
| /:pk/        | GET: get detailed post by id, DELETE: delete post by id |
| /:pk/like/   | Like post by id                                         |
| /:pk/unlike/ | Unlike post by id                                       |

### /api/comments/

| Endpoint     | Description                                                                 |
| ------------ | --------------------------------------------------------------------------- |
| /:post_id/   | GET: retrieve comments list by post id, POST: create new comment by post id |
| /:pk/delete/ | Delete comment by id                                                        |
| /:pk/like/   | Like comment by id                                                          |
| /:pk/unlike/ | Unlike comment by id                                                        |

## Installation

1. Clone the Repository

```bash
git clone https://github.com/bobbykim89/pollogram-api.git
cd pollogram-api
```

2. Set Up Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Set Up Environment Variables<br>
   Create a `.env` file in the root directory and add the necessary configuration variables (e.g., database URL, secret key, etc.).

5. Run Migrations

```bash
python manage.py migrate
```

6. Start the Server

```bash
python manage.py runserver
```

## Dependencies

Here’s the list of main dependencies used in the project:

```makefile
asgiref==3.8.1
certifi==2024.8.30
cloudinary==1.41.0
Django==5.1.3
django-filter==24.3
djangorestframework==3.15.2
djangorestframework-simplejwt==5.3.1
Markdown==3.7
psycopg==3.2.3
psycopg-binary==3.2.3
PyJWT==2.10.0
python-dotenv==1.0.1
six==1.16.0
sqlparse==0.5.2
typing_extensions==4.12.2
urllib3==2.2.3
whitenoise==6.8.2
```

## Usage

After starting the server, you can access the API endpoints at http://localhost:8000/. Use a tool like Postman or curl to test the API.

## Future Enhancements

Implement user stories for following/unfollowing.
Add notifications for likes and comments.

## License

This project is licensed under the MIT License.

Feel free to customize further based on your specific implementation!
