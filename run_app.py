from artjam import app, db
import artjam.config as config

from flask.ext.script import Manager


def create_app(cfg=None):
    if cfgi == 'debug':
        app.config.from_object(config.debugConfig)
    elif cfg == 'production':
        app.config.from_object(config.productionConfig)
    else:
        raise NameError("This configuration name is not allowed!")
    return app

manager = Manager(create_app)


@manager.command
def init_db():
    db.create_all()


@manager.command
def run():
    app.run()

if __name__ == '__main__':
    manager.add_option('-c', '--config', dest='cfg', required=False)
    manager.run()
