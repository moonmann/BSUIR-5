from models import session
from models.Student import Student


def get_all():
    # TODO
    n = session.query(Student).filter().first()
    return n
