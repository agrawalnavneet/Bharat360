# Government News Feedback Platform

A Django-based web application that collects feedback from users on government-related news articles from different regional sources.

## Features

- **News Articles Management**: Display government-related news articles from various regional sources
- **Regional Sources**: Support for multiple news sources organized by region
- **User Feedback Collection**: Users can rate articles (1-5 stars) and provide comments
- **Filtering**: Filter news by region, category, or source
- **Statistics Dashboard**: View platform statistics including article counts, feedback metrics, and top sources
- **Modern UI**: Beautiful, responsive design using Bootstrap 5
- **Admin Interface**: Full Django admin interface for managing articles, sources, and feedback

## Installation

1. **Create a virtual environment** (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Run migrations**:
```bash
python manage.py migrate
```

4. **Create a superuser** (to access admin panel):
```bash
python manage.py createsuperuser
```

5. **Run the development server**:
```bash
python manage.py runserver
```

6. **Access the application**:
- Main site: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## Usage

### Adding News Sources

1. Go to the admin panel at `/admin/`
2. Navigate to "News Sources"
3. Click "Add News Source"
4. Fill in:
   - Name: Name of the news source (e.g., "The Times")
   - Region: Region or location (e.g., "New York", "California")
   - Website: Optional URL to the source's website
   - Description: Optional description
   - Is Active: Check to make it visible

### Adding News Articles

1. Go to the admin panel
2. Navigate to "News Articles"
3. Click "Add News Article"
4. Fill in:
   - Title: Article title
   - Content: Full article content
   - Source: Select a news source
   - Published Date: When the article was published
   - URL: Optional link to original article
   - Category: Select from Policy, Legislation, Election, Budget, Public Service, or Other

### Collecting Feedback

Users can:
- View articles on the main page
- Filter articles by region, category, or source
- Click on an article to read it
- Submit feedback with:
  - Rating (1-5 stars)
  - Optional comment
  - Optional name and email
  - Whether the article was helpful

## Project Structure

```
django/
├── manage.py
├── newsfeedback/          # Main project directory
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── news/                   # News application
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│       └── news/
│           ├── base.html
│           ├── news_list.html
│           ├── news_detail.html
│           └── statistics.html
├── requirements.txt
└── README.md
```

## Models

- **NewsSource**: Represents a news source with region information
- **NewsArticle**: Represents a government-related news article
- **Feedback**: User feedback on articles with ratings and comments

## Future Enhancements

- User authentication and profiles
- Email notifications for new articles
- RSS feed integration
- API endpoints for external integrations
- Advanced analytics and reporting
- Comment threading and replies
- Article search functionality

## License

This project is open source and available for educational purposes.

