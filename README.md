[![Typing SVG](https://readme-typing-svg.demolab.com?font=Platypi&weight=900&size=24&pause=1000&color=D2691E&background=2FB94200&center=true&vCenter=true&random=false&width=838&height=80&lines=Welcome+to+My+Portfolio+Repository!+%F0%9F%91%8B)](https://git.io/typing-svg)<img src="https://avatars.mds.yandex.net/i?id=0f99f6aad0e457967e4ba476316863a6_l-5145180-images-thumbs&ref=rim&n=13&w=1920&h=1080" alt="Photo">

# 🖥️ My Portfolio 

Welcome to the repository of my **Portfolio Web Application**. This project is built using Django for the backend, 
MongoDB Atlas for the database, and HTML/CSS/JavaScript for the frontend. The application showcases about me, skills, 
and projects while allowing visitors to get in touch with me using a contact form.

---

## 📚 Table of Contents

- 🌟 [Features](#features)
- 🔧 [Technologies Used](#technologies-used)
- 🚀 [Getting Started](#Getting Started)
- 📂 [Folder Structure](#folder-structure)
- 📬 [Contact](#contact)
- 🛠️ [License](#license)

---

## 🌟 Features

- Responsive design for both desktop and mobile.
- Sections for **About Me**, **Skills**, **Resume**, **Projects**, and **Contact**.
- Dynamic navigation menu.
- Contact form to receive user messages, stored in MongoDB Atlas.
- Animations using AOS (Animate On Scroll).
- Easy scalability for adding new sections and projects.

---

## 🔧 Technologies Used

### Backend:
- **Django**: Python web framework for server-side logic.
- **djongo**: Connector to integrate MongoDB with Django.
- **MongoDB Atlas**: Cloud-based NoSQL database.

### Frontend:
- **HTML5**, **CSS3**, **JavaScript**: Core frontend technologies.
- **Bootstrap 5**: Responsive design framework.
- **AOS Library**: Animation on scroll.
- **Typed.js**: Typing effect on the Hero section.

### Middleware & Tools:
- **WhiteNoise**: Serve static files efficiently in production.
- **dotenv**: Manage environment variables securely.

---

## 🚀 Getting Started

### Prerequisites:
- Python (==3.11.8)
- Node.js (Optional for additional frontend development)
- MongoDB Atlas account
- Git

### Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/AmirSarrafzadeh/Portfolio.git
   cd Portfolio
   ```
2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```
4. Create a .env file in the project root:
###### Generate a new key using `python -c 'from django.core.management.utils import get_random_secret_key'`
```env
db_username=YOUR_MONGODB_USERNAME
db_password=YOUR_MONGODB_PASSWORD
db_host=YOUR_MONGODB_HOST
db_app=YOUR_MONGODB_APP_NAME
SECRET_KEY=YOUR_DJANGO_SECRET_KEY 
```
5. Collect static files:

```bash
python manage.py collectstatic
```
6. Run the development server:

```bash
python manage.py runserver
```

7. Access the app at:
```
http://127.0.0.1:8000
```

8. Usage<br>
Contact Form:
Users can fill out the contact form to send their details (name, email, subject, message). Submissions are stored in the contacts collection in MongoDB Atlas.

9. Adding New Projects:
Update the home.html file under the #portfolio section with the new project details.
Include any required static assets (images, icons) in the static/ folder.


10. Customizing the Design:
Edit the style.css file in the static/css folder to modify the design and layout.

## 📂 Folder Structure
```
Portfolio/
├── home/                  # App folder
│   ├── migrations/        # Database migrations
│   ├── admin.py           # Application admin
│   ├── apps.py            # Application apps
│   ├── forms.py           # Django forms
│   ├── models.py          # Database models
│   ├── tests.py           # Application tests
│   ├── urls.py            # URL routing for the app
│   └── views.py           # Application views
├── Portfolio/             # Project folder
│   ├── staticfiles/       # Collected static files (development)
│   ├── asgi.py            # ASGI configuration
│   ├── settings.py        # Main project settings
│   ├── urls.py            # Project-wide URL routing
│   └── wsgi.py            # WSGI configuration
├── static/                # Collected static files (production)
├── templates/             # Global HTML templates
├── .env                   # Environment variables
├── .gitignore             # Git ignore rules
├── .Makefile              # Makefile for common commands
├── .manage.py             # Django management script
├── .Procfile              # Heroku deployment file
├── .README.md             # Project documentation
├── .requirements.txt      # Python dependencies
└── .runtime.txt           # Python runtime version 
```


## 📬 Contact
Feel free to reach out for any inquiries or collaborations:

- [Email](mailto:amirsarrafzadeh88@gmail.com)
- <a href="https://www.linkedin.com/in/amir-sarrafzadeh/">linkedin</a> 
- <a href="https://github.com/AmirSarrafzadeh/">Github</a>


## 🛠️ License
This project is licensed under the MIT License. See the LICENSE file for details.


### Key Fixes:
- Added line breaks where necessary.
- Used proper Markdown syntax for lists, tables, and code blocks.
- Ensured the folder structure is enclosed in a code block for clarity.

Let me know if you need additional information!

# Developed with ❤️ by Amir