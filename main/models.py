from main import db
from flask_sqlalchemy import SQLAlchemy


class Entry(db.Model):
    """
        ▽ DB操作のやり方
        from main.models import Entry
        from main import db
        entry1 = Entry(title='title1', text='text1')
        db.session.add(entry1)
        db.session.commit()
        
        entry2 = Entry(title='title2', text='text2')
        db.session.add(entry2)
        db.sesion.commit()
        db.session.commit()
        entries = Entry.query.all()
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)

    def __repr__(self):
        return "<Entry id={} title={!r}>".format(self.id, self.title)


def init():
    """
        以下のコマンドでDBを作成する
        python -c "import main.models; main.models.init()"
    """
    db.create_all()