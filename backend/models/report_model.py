from extensions import db
from datetime import datetime

class Report(db.Model):
    __tablename__ = 'reports'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    report_type = db.Column(db.String(50), nullable=False) # 'user_stats', 'trip_analytics', etc.
    file_path = db.Column(db.String(255))
    created_by = db.Column(db.Integer, db.ForeignKey('admin_users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'report_type': self.report_type,
            'file_path': self.file_path,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat()
        }
