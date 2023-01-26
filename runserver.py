import os 
import logging

from core import create_app, db 
from core.models import Post, Author

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    
app = create_app(os.getenv('FLASK_CONFIG') or 'dev')

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, post=Post, author=Author)
    
@app.cli.command("init_db")
def init_db():
    db.create_all()
    db.session.commit()
    logging.warning("Database initialized !")
    
if __name__ == "__main__":
    app.run(threaded=True, port=8080)
