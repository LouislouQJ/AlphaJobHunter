from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from db_init import Jobs, session
from sqlalchemy import desc, or_
from manage.config import config


def quick_query(keywords):
    rules = or_(*[Jobs.firms.like(w) for w in keywords])
    return session.query(Jobs).filter(rules).filter(
        Jobs.date >= config["KEY_TIMESTAMP"]).distinct().order_by(desc(Jobs.date)).all()


keywords = dict()
keywords['securities'] = ['%证券%', '%国泰君安%', '%申万宏源%']
keywords['banks'] = ['%银行%']
keywords['funds'] = ['%基金%', '%资产%', '%资管%', '%资产管理%']
app = Flask(__name__)
Bootstrap(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', securities=quick_query(keywords['securities'])[:4],
                           funds=quick_query(keywords['funds'])[:4],
                           banks=quick_query(keywords['banks'])[:4])


@app.route('/securities')
def security():
    return render_template('securities.html', entities=quick_query(keywords['securities']))


@app.route('/funds')
def funds():
    return render_template('securities.html', entities=quick_query(keywords['funds']))


@app.route('/banks')
def banks():
    return render_template('securities.html', entities=quick_query(keywords['banks']))


if __name__ == '__main__':
    app.run()
