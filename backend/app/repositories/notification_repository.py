from sqlalchemy.orm import Session

from app.models.notification import Notification


class NotificationRepository:

    @staticmethod
    def create(
        db: Session,
        notification: Notification
    ):

        db.add(notification)
        db.commit()
        db.refresh(notification)

        return notification

    @staticmethod
    def get_by_user(
        db: Session,
        user_id: int
    ):

        return (
            db.query(Notification)
            .filter(
                Notification.user_id == user_id
            )
            .all()
        )

    @staticmethod
    def mark_as_read(
        db: Session,
        notification: Notification
    ):

        notification.is_read = True

        db.commit()

        db.refresh(notification)

        return notification