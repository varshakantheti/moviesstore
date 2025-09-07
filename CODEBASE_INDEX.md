# Movies Store Codebase Index

## Project Overview
A Django-based e-commerce application for selling movies online. The application includes user authentication, movie catalog, shopping cart functionality, and review system.

## Project Structure
```
moviesstore/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database
├── media/                   # Media files (movie images)
│   └── movie_images/        # Movie poster images
├── moviesstore/             # Main project directory
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   ├── asgi.py              # ASGI configuration
│   ├── static/              # Static files
│   │   ├── css/
│   │   │   └── style.css    # Custom CSS styles
│   │   └── img/             # Static images
│   └── templates/
│       └── base.html        # Base template
├── home/                    # Home app
├── movies/                  # Movies app
├── accounts/                # User authentication app
└── cart/                    # Shopping cart app
```

## Applications

### 1. Home App (`home/`)
**Purpose**: Landing page and about page
- **Models**: None (uses Django's built-in models)
- **Views**:
  - `index()`: Homepage view
  - `about()`: About page view
- **URLs**:
  - `/` → `home.index` (homepage)
  - `/about` → `home.about` (about page)
- **Templates**:
  - `home/index.html`: Homepage template
  - `home/about.html`: About page template

### 2. Movies App (`movies/`)
**Purpose**: Movie catalog and review system
- **Models**:
  - `Movie`: Movie information (id, name, price, description, image)
  - `Review`: User reviews for movies (id, comment, date, movie FK, user FK)
- **Views**:
  - `index()`: Movie listing with search functionality
  - `show()`: Individual movie details and reviews
  - `create_review()`: Create new review (login required)
  - `edit_review()`: Edit existing review (login required, owner only)
  - `delete_review()`: Delete review (login required, owner only)
- **URLs**:
  - `/movies/` → `movies.index` (movie list)
  - `/movies/<id>/` → `movies.show` (movie details)
  - `/movies/<id>/review/create/` → `movies.create_review`
  - `/movies/<id>/review/<review_id>/edit/` → `movies.edit_review`
  - `/movies/<id>/review/<review_id>/delete/` → `movies.delete_review`
- **Templates**:
  - `movies/index.html`: Movie listing page
  - `movies/show.html`: Movie details page
  - `movies/edit_review.html`: Edit review form

### 3. Accounts App (`accounts/`)
**Purpose**: User authentication and registration
- **Models**: None (uses Django's built-in User model)
- **Views**:
  - `login()`: User login
  - `signup()`: User registration
  - `logout()`: User logout (login required)
- **URLs**:
  - `/accounts/signup` → `accounts.signup`
  - `/accounts/login/` → `accounts.login`
  - `/accounts/logout/` → `accounts.logout`
- **Templates**:
  - `accounts/login.html`: Login form
  - `accounts/signup.html`: Registration form
- **Forms**:
  - `CustomUserCreationForm`: Custom user registration form
  - `CustomErrorList`: Custom error display for forms

### 4. Cart App (`cart/`)
**Purpose**: Shopping cart functionality
- **Models**: None (uses session-based cart)
- **Views**:
  - `index()`: Display cart contents and total
  - `add()`: Add movie to cart
- **URLs**:
  - `/cart/` → `cart.index` (cart page)
  - `/cart/<id>/add/` → `cart.add` (add to cart)
- **Templates**:
  - `cart/index.html`: Cart display page
- **Utils**:
  - `calculate_cart_total()`: Calculate total price for cart items

## Key Features

### Authentication System
- User registration with custom form validation
- User login/logout functionality
- Login-required decorators for protected views
- Custom error handling for forms

### Movie Management
- Movie catalog with search functionality
- Movie details with image display
- Price and description information
- Image upload support for movie posters

### Review System
- Users can create reviews for movies
- Users can edit/delete their own reviews
- Reviews display with user information and timestamps
- Review management requires authentication

### Shopping Cart
- Session-based cart storage
- Add movies to cart with quantity selection
- Cart total calculation
- Cart persistence across sessions

### UI/UX Features
- Bootstrap 5 for responsive design
- Font Awesome icons
- Custom CSS styling
- Mobile-responsive navigation
- Professional footer with contact information

## Database Schema

### Movie Table
- `id` (AutoField, Primary Key)
- `name` (CharField, max_length=255)
- `price` (IntegerField)
- `description` (TextField)
- `image` (ImageField, upload_to='movie_images/')

### Review Table
- `id` (AutoField, Primary Key)
- `comment` (CharField, max_length=255)
- `date` (DateTimeField, auto_now_add=True)
- `movie` (ForeignKey to Movie)
- `user` (ForeignKey to User)

## Configuration

### Settings (`moviesstore/settings.py`)
- Django 5.0 framework
- SQLite database
- Debug mode enabled
- Static files configuration
- Media files configuration
- Custom template directory
- Installed apps: home, movies, accounts, cart

### URL Configuration
- Main URLs include all app URLs
- Static media URL configuration
- Admin interface at `/admin/`

## Static Files
- Custom CSS in `moviesstore/static/css/style.css`
- Logo and background images in `moviesstore/static/img/`
- Movie images stored in `media/movie_images/`

## Dependencies
- Django 5.0
- Python 3.x
- Bootstrap 5.3.3
- Font Awesome 6.1.1
- Google Fonts (Poppins)

## Security Features
- CSRF protection enabled
- User authentication required for sensitive operations
- User ownership validation for review editing/deletion
- Secure password validation

## Development Notes
- Uses Django's built-in development server
- SQLite database for development
- Media files served through Django's development server
- Debug mode enabled for development
