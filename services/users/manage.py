# services/users/manage.py

import sys
import unittest

from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import User  # nuevo

app = create_app()

cli = FlaskGroup(create_app=create_app)

# new
@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def test():
    """Ejecuta las pruebas sin cobertura de código"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)


if __name__ == '__main__':
    cli()

