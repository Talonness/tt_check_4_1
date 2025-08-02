from flask import Blueprint, render_template, request, redirect, url_for, current_app

ui_bp = Blueprint("ui", __name__)

@ui_bp.route("/tasks/new", methods=["GET"])
def task_form():
    return render_template("add_task.html")

@ui_bp.route("/tasks/new", methods=["POST"])
def task_submit():
    title = request.form.get("title")
    description = request.form.get("description")
    current_app.task_service.add_task(title, description)
    return redirect(url_for("ui.task_form"))