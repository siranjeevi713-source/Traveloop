from flask import Blueprint, request, render_template, redirect, url_for, session
from flask_login import login_user, logout_user
from services.auth_service import AuthService
from models.user_model import User
from utils.response_handler import success_response, error_response

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json() if request.is_json else request.form
        result, message = AuthService.authenticate_user(data.get('email'), data.get('password'))
        if result:
            user = User.query.get(result['user']['id'])
            login_user(user, remember=True)
            if request.is_json:
                return success_response(result, message)
            return redirect(url_for('dashboard.index'))
        if request.is_json:
            return error_response(message, 401)
        return render_template('auth/login.html', error=message)
    return render_template('auth/login.html')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.get_json() if request.is_json else request.form
        user, message = AuthService.register_user(data)
        if user:
            if request.is_json:
                return success_response(None, message)
            return redirect(url_for('auth.login'))
        if request.is_json:
            return error_response(message)
        return render_template('auth/signup.html', error=message)
    return render_template('auth/signup.html')

@auth_bp.route('/logout')
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('auth.login'))
