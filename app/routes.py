from __main__ import web
from models.candidate import Candidate
from flask import render_template, request
import requests
import utils


@web.route('/')
def app_page():
    vacancies = requests.get_vacancies()
    return render_template("index.html", option=vacancies)


@web.route('/send', methods=['POST'])
def response():
    candidate = Candidate()
    candidate.position_id = request.form.get("position")
    candidate.surname = request.form.get("surname")
    candidate.name = request.form.get("name")
    candidate.patronymic = request.form.get("patronymic")
    candidate.date_of_birthday = request.form.get("birthday")
    candidate.experience = int(request.form.get("experience"))
    candidate.mail = request.form.get("mail")
    candidate.phone = request.form.get("phone")

    exists = requests.check_existance(candidate.phone)
    if exists:
        candidate.id = exists[0][0]
        invited = requests.check_interview(candidate)
        if invited:
            print("Кандидат уже приглашен")
        else:
            utils.send_to_app(candidate)
    else:
        video = request.files["video"]
        utils.upload_video(video, candidate.phone)
        utils.send_to_app(candidate)
    return app_page()