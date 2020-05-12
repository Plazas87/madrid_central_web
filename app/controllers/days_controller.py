from flask import render_template, request, redirect
from app.models.day import Day
from app import db

#@dates_blueprints.route('/')
def index_days():
    days = Day.query
    return render_template('days/index.html', days=days)

def create_days():
    days = Day.create_range(request.form.get('initialDay'), request.form.get('finalDay'))
    for day in days:
        new_day = Day(id=''.join(day), day=day[2], month=day[1], year=day[0])
        day = Day.query.get(''.join(day))
        if day:
            continue
        db.session.add(new_day)
        db.session.commit()
    return redirect('/days')

def delete_days():
    db.session.query(Day).delete()
    db.session.commit()
    return redirect('/days')
