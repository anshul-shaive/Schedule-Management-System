from app import db


class RoomSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    room_id = db.Column(db.String(5), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    start_time = db.Column(db.String(20), nullable=False)
    end_time = db.Column(db.String(20), nullable=False)
    participants = db.relationship("Participants", backref="room_s", lazy='dynamic')

    def __repr__(self):
        return '<RoomSchedule %r>' % self.room_id


class Participants(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    room_schedule_id = db.Column(db.Integer, db.ForeignKey('room_schedule.id'))
    room_ss = db.relationship('RoomSchedule')

    def __repr__(self):
        return '<Participants %r>' % self.name