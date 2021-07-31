from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    api = Api(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('SCHEDULE_DB_URI')  # set env variable with mysql url
    db.init_app(app)

    from app.api.schedule import Schedule
    from app.api.check_avail import ParticipantAvail
    from app.api.add_participant import AddParticipant
    from .models import RoomSchedule, Participants

    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
        return 'HomePage'

    api.add_resource(Schedule, '/schedule_meet')
    api.add_resource(ParticipantAvail, '/check_avail')
    api.add_resource(AddParticipant, '/add_participant')

    return app
