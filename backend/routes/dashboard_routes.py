from flask import Blueprint, render_template, session, redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from models.user_model import User
from models.settings_model import UserSetting
from models.notification_model import Notification
from extensions import db
import os
from services.trip_service import TripService
from werkzeug.utils import secure_filename

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/api/trips/create', methods=['POST'])
@login_required
def api_create_trip():
    data = request.get_json()
    trip, message = TripService.create_full_trip(current_user.id, data)
    if trip:
        return jsonify({'success': True, 'trip_id': trip.id})
    return jsonify({'success': False, 'error': message}), 400

@dashboard_bp.route('/api/notifications')
@login_required
def get_notifications():
    notifs = Notification.query.filter_by(user_id=current_user.id).order_by(Notification.created_at.desc()).limit(10).all()
    return jsonify([n.to_dict() for n in notifs])

@dashboard_bp.route('/api/profile/upload', methods=['POST'])
@login_required
def upload_profile_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = secure_filename(f"user_{current_user.id}_{file.filename}")
        upload_path = os.path.join('frontend', 'static', 'uploads', 'avatars', filename)
        file.save(upload_path)
        current_user.profile_image = f"uploads/avatars/{filename}"
        db.session.commit()
        return jsonify({'success': True, 'image_url': url_for('static', filename=current_user.profile_image)})

@dashboard_bp.route('/')
@login_required
def index():
    return render_template('dashboard/dashboard.html')

@dashboard_bp.route('/my-trips')
@login_required
def my_trips():
    return render_template('dashboard/my-trips.html')

@dashboard_bp.route('/create-trip')
@login_required
def create_trip():
    return render_template('dashboard/create-trip.html')

@dashboard_bp.route('/itinerary')
@login_required
def itinerary():
    return render_template('dashboard/itinerary.html')

@dashboard_bp.route('/budget')
@login_required
def budget():
    return render_template('dashboard/budget.html')

@dashboard_bp.route('/activities')
@login_required
def activities():
    return render_template('dashboard/activities.html')

@dashboard_bp.route('/packing-list')
@login_required
def packing_list():
    return render_template('dashboard/packing-list.html')

@dashboard_bp.route('/notes')
@login_required
def notes():
    return render_template('dashboard/notes.html')

@dashboard_bp.route('/shared-trips')
@login_required
def shared_trips():
    return render_template('dashboard/shared-trips.html')

@dashboard_bp.route('/profile')
@login_required
def profile():
    return render_template('dashboard/profile.html')

@dashboard_bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    user = current_user
    user_settings = UserSetting.query.filter_by(user_id=user.id).first()
    
    if not user_settings:
        user_settings = UserSetting(user_id=user.id)
        db.session.add(user_settings)
        db.session.commit()

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'profile':
            user.full_name = request.form.get('full_name')
            db.session.commit()
        elif action == 'preferences':
            user_settings.theme = 'dark' if request.form.get('dark_mode') else 'light'
            user_settings.notifications_enabled = True if request.form.get('notifications') else False
            user_settings.privacy_public = True if request.form.get('privacy') else False
            user_settings.language = request.form.get('language')
            db.session.commit()
        
        return redirect(url_for('dashboard.settings'))

    return render_template('dashboard/settings.html', settings=user_settings)
