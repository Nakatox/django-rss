
# Django-rss

This project is a remake of the site news.ycombinator.
On the main page we have a list of the articles coming from multiples rss that we use, and are stored in the database.
The articles can be upvoted by the users, and there is a ranking based on the most recent ones.







## Features

- The user can register himself with an email and a password.
- The user can connect and have an account.
- The user can see the different articles on the webpage.
- The user can upvote only one time an article that he likes or founds interesting.

  
## Run Locally

Clone the project

```bash
  git clone https://github.com/Nakatox/django-rss.git
```

Go to the project directory

```bash
  cd django-rss
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```

  
## Screenshots

Register Page
![App Screenshot](https://user-images.githubusercontent.com/73486687/137913054-f16c576f-30bf-4d4f-ac5c-0edf86d8628a.png)


Home Page
![App Screenshot](https://user-images.githubusercontent.com/73486687/137913138-0dad4d5d-0f3d-4e97-913f-a7e470a3f43f.png)


  
## API Reference

#### Get all articles

```http
  GET /api/articles
```

#### Register User

```http
  POST /api/user/register
```

#### Login User

```http
  POST /api/user/login
```

#### Get User Infos

```http
  GET /api/user/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

  
## Authors

- [@Ulysseassoo](https://github.com/Ulysseassoo)
- [@Nakatox](https://github.com/Nakatox)
- [@Feuka](https://github.com/fabian222222)
- [@AntoineSimonot ](https://github.com/AntoineSimonot)

  