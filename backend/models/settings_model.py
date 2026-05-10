from extensions import db

class UserSetting(db.Model):
    __tablename__ = 'user_settings'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    theme = db.Column(db.String(20), default='light')
    notifications_enabled = db.Column(db.Boolean, default=True)
    privacy_public = db.Column(db.Boolean, default=False)
    language = db.Column(db.String(10), default='en')
    
    # Relationship back to user
    user = db.relationship('User', backref=db.backref('settings', uselist=False))

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'theme': self.theme,
            'notifications_enabled': self.notifications_enabled,
            'privacy_public': self.privacy_public,
            'language': self.language
        }
