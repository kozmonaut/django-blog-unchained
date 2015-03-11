# django-blog-unchained
Easy blogging with Django 1.6. 

Try it live: [dropsql.herokuapp.com](http://dropsql.herokuapp.com)

## Getting started 
### Installation
- Pull it from Github repository: 
```
$ git clone https://github.com/kozmonaut/django-blog-unchained
```

- Install all requirements: 
```
$ pip install -r requirements.txt
```

- Create database model:
```
$ python manage.py syncdb
$ python manage.py schemamigration --initial blog
$ python manage.py migrate blog
```

- Run Django server: 
```
$ python manage.py runserver
```

If you using it local you can access it on http://localhost:8000 and http://localhost:8000/admin

### Things you should check

- Add your Disqus API key and website shortname - settings.py
- If you need, you can change URL path for storing media uploads(default: /media/uploads/) - settings.py
- For using PostgreSQL or MySQL change database engine - settings.py

### Features
- Flatpages - You can use it for static content, like About us, Contact, Help etc.
- Commenting engine(django.comments and Disqus addon) - Leave a comment on each article
- CKEditor - Edit your article content as you wish
- Media upload
- Code highlight - You can highlight your code with different syntaxes
- Tags - Browse through articles by their tags
- Categories - Browse articles by their category
- Recent posts - There is list of recently added posts
- Recent comments - List of recent comments on articles
- Simple search engine - Search articles by title or description
- Social media share buttons
- RSS - Use RSS feeds

### Customization
- Blog uses Bootstrap framework, you can modify it anytime.
- Change social media profile links inside - /blog/templates/include/base.html (for now!)
- If you need more features about seach engine, check [Haystack](http://haystacksearch.org/)
- Generate different highlight theme(monokai, tango, etc.): 
```
$ pygmentize -S tango -f html > blog/static/css/code.css
```
___
### Deploy it to heroku
Follow the official Heroku documentation to deploy your app: [devcenter.heroku.com](http://devcenter.heroku.com)
