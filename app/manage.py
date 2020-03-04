from __future__ import absolute_import

import os

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from application import create_app, db


app = create_app(os.getenv("BAUPASS_CONFIG") or "default")
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)

manager.add_command("shell", Shell(make_context=make_shell_context))


if __name__ == "__main__":
    manager.run()
