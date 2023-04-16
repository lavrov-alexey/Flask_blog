from flask import Blueprint, render_template, redirect

from blog.user.views import USERS

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {
    1: {
        'author': 1,
        'title': 'Заголовок статьи-1',
        'text': 'Текст статьи-1. Текст статьи-1.Текст статьи-1.Текст статьи-1.Текст статьи-1'
    },
    2: {
        'author': 1,
        'title': 'Заголовок статьи-2',
        'text': 'Текст статьи-2. Текст статьи-2.Текст статьи-2.Текст статьи-2.Текст статьи-2'
    },
    3: {
        'author': 2,
        'title': 'Заголовок статьи-3',
        'text': 'Текст статьи-3. Текст статьи-3.Текст статьи-3.Текст статьи-3.Текст статьи-3'
    },
    4: {
        'author': 2,
        'title': 'Заголовок статьи-4',
        'text': 'Текст статьи-4. Текст статьи-4.Текст статьи-4.Текст статьи-4.Текст статьи-4'
    },
    5: {
        'author': 3,
        'title': 'Заголовок статьи-5',
        'text': 'Текст статьи-5. Текст статьи-5.Текст статьи-5.Текст статьи-5.Текст статьи-5'
    },
}

@article.route('/')
def article_list():
    return render_template(
        'articles/list.html',
        articles=ARTICLES,
    )

@article.route('/<int:pk>')
def get_article(pk: int):
    # обработака варианта несуществующего id
    try:
        article = ARTICLES[pk]
        author_pk = article['author']
    except KeyError:
        return redirect('/articles/')
    return render_template(
        'articles/details.html',
        article=article,
        article_pk=pk,
        author=USERS[author_pk]
    )