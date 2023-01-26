from flask import Blueprint, render_template

from .models import Post

post = Blueprint("post", __name__, url_prefix='/')

posts = Post.query.all()[:4]

@post.route("/")
def home_page():
    

    return render_template(
        "index.html",
        posts_all=posts[:4],
        page_title="Accueil",
        subheading="bienvenu(e) sur clean blog"
    )
    
@post.route("/blog/")    
def blog_page():
    return render_template("page/blog/list.html",
        posts_all=posts,
        page_title="blog",
        subheading="liste des articles"
    )

@post.route("blog/<int:post_id>")
def blog_detail_page(post_id):
    article = Post.query.get_or_404(post_id)
    
    return render_template(
        "page/blog/detail.html",
        post=article,
        page_title=article.post_title,
        subheading=article.post_subtitle
        )
    

@post.route("/contact/")
def contact_page():

	return render_template(
        "page/contact.html",
        page_title="Contact",
        subheading="Laissez un message"
    )


@post.route("/support/")
def support_page():
    return render_template(
        "page/support.html",
        page_title="Support",
        subheading="Besoin d' aides ?",
    )
