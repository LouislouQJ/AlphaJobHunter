from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///jobs.db')
Session = sessionmaker(engine)
session = Session()


class Jobs(Base):
    __tablename__ = 'jobs'

    id = Column(Integer(), primary_key=True)
    date = Column(DateTime())
    firms = Column(String(64))
    url = Column(String(128))

    def __repr__(self):
        return '{self.id},{self.date},{self.firms},{self.url}'.format(self=self)


if __name__ == '__main__':
    Jobs.metadata.create_all(engine)
