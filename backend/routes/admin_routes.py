from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from models.admin_model import AdminUser, AdminLog
from models.user_model import User
from models.trip_model import Trip
from models.analytics_model import Analytics, DestinationAnalytics
from extensions import db
from datetime import datetime, timedelta

admin_bp = Blueprint('admin', __name__)

def is_admin():
    return 'admin_id' in session

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        admin = AdminUser.query.filter_by(email=email).first()
        if admin and admin.check_password(password):
            session['admin_id'] = admin.id
            session['admin_username'] = admin.username
            admin.last_login = datetime.utcnow()
            db.session.commit()
            return redirect(url_for('admin.dashboard'))
        return render_template('admin/login.html', error="Invalid admin credentials")
    return render_template('admin/login.html')

@admin_bp.route('/dashboard')
def dashboard():
    if not is_admin():
        return redirect(url_for('admin.login'))
    
    # Fetch stats
    stats = {
        'total_users': User.query.count(),
        'total_trips': Trip.query.count(),
        'active_users': User.query.filter(User.created_at >= datetime.utcnow() - timedelta(days=30)).count(),
        'popular_destinations': DestinationAnalytics.query.order_by(DestinationAnalytics.trip_count.desc()).limit(5).all()
    }
    
    return render_template('admin/dashboard.html', stats=stats)

@admin_bp.route('/users')
def users():
    if not is_admin():
        return redirect(url_for('admin.login'))
    users_list = User.query.all()
    return render_template('admin/users.html', users=users_list)

@admin_bp.route('/users/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    if not is_admin():
        return jsonify({'error': 'Unauthorized'}), 401
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'success': True})

@admin_bp.route('/trips')
def trips():
    if not is_admin():
        return redirect(url_for('admin.login'))
    all_trips = Trip.query.all()
    return render_template('admin/trips.html', trips=all_trips)

@admin_bp.route('/analytics')
def analytics():
    if not is_admin():
        return redirect(url_for('admin.login'))
    return render_template('admin/analytics.html')

@admin_bp.route('/reports')
def reports():
    if not is_admin():
        return redirect(url_for('admin.login'))
    return render_template('admin/reports.html')

@admin_bp.route('/settings')
def settings():
    if not is_admin():
        return redirect(url_for('admin.login'))
    return render_template('admin/settings.html')

@admin_bp.route('/logout')
def logout():
    session.pop('admin_id', None)
    session.pop('admin_username', None)
    return redirect(url_for('admin.login'))
