from flask import request, jsonify
from flask_restful import Resource
from app.models import RoomSchedule, Participants
from datetime import datetime as dt


class ParticipantAvail(Resource):

    def get(self):
        return jsonify({'msg': 'Use a post request and pass json data'})

    def post(self):
        data = request.get_json()
        name = data['Name']
        date = data['Date']
        start_time = data['StartTime']
        end_time = data['EndTime']
        msg = 'Participant is available'
        participant_meets = Participants.query.filter_by(name=name).all()
        dtconv = lambda x: dt.strptime(x, '%H:%M')
        for meet in participant_meets:
            participant_meet = RoomSchedule.query.filter_by(id=meet.room_schedule_id).first()
            if not participant_meet.date == date:
                continue
            if (dtconv(participant_meet.start_time) < dtconv(end_time)) and \
                    (dtconv(participant_meet.end_time) > dtconv(start_time)):
                msg = 'Not available'
                return jsonify({'msg': msg})
        return jsonify({'msg': msg})
