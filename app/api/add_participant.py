from flask import request, jsonify
from flask_restful import Resource
from app import db
from app.models import RoomSchedule, Participants


class AddParticipant(Resource):

    def get(self):
        return jsonify({'msg': 'Use a post request and pass json data'})

    def post(self):
        data = request.get_json()
        name = data['Name']
        meet_id = data['MeetID']
        meet = RoomSchedule.query.filter_by(id=meet_id).first()
        try:
            participant = Participants(name=name)
            meet.participants.append(participant)
            db.session.add(participant)
            db.session.commit()
            msg = 'Participant added to the meeting'
        except Exception as e:
            msg = {'msg': 'Failed', 'err': str(e)}
        return jsonify({'msg': msg})
