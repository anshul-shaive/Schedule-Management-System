from flask import request, jsonify
from flask_restful import Resource
from app import db
from app.models import RoomSchedule, Participants
from datetime import datetime as dt
import ast


def room_avail(room_id, date, start_time, end_time):
    room_schedule = RoomSchedule.query.filter_by(room_id=room_id, date=date).all()
    dtconv = lambda x: dt.strptime(x, '%H:%M')
    for rs in room_schedule:
        if (dtconv(rs.start_time) < dtconv(end_time)) and (dtconv(rs.end_time) > dtconv(start_time)):
            return False
    return True


class Schedule(Resource):

    def get(self):
        return jsonify({'msg': 'Use a post request and pass json data'})

    def post(self):
        data = request.get_json()
        room_id = data['RoomID']
        date = data['Date']
        start_time = data['StartTime']
        end_time = data['EndTime']
        participants = []
        if data.get('Participants'):
            participants = ast.literal_eval(data['Participants'])
        rooms = ['R1', 'R2', 'R3', 'R4', 'R5']
        msg = ''
        if room_id not in rooms and room_id not in map(lambda x: x.lower(), rooms):
            msg = "Incorrect Room Id"
        else:
            if not room_avail(room_id, date, start_time, end_time):
                msg = "Room not available"

            else:
                schedule = RoomSchedule(room_id=room_id, date=date, start_time=start_time, end_time=end_time)
                participant_list = []
                for participant in participants:
                    part_cp = Participants(name=participant)
                    schedule.participants.append(part_cp)
                    participant_list.append(part_cp)
                try:
                    db.session.add(schedule)
                    db.session.add_all(participant_list)
                    db.session.commit()
                    msg = 'Meeting successfully scheduled'
                except Exception as e:
                    msg = {'msg': 'Failed', 'err': str(e)}
        return jsonify({'msg': msg})
