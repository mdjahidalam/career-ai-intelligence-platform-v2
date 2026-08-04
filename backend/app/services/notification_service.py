from app.models.notification import Notification

from app.repositories.notification_repository import (
    NotificationRepository
)


class NotificationService:

    @staticmethod
    def create(
        db,
        user,
        title,
        message,
        notification_type="INFO"
    ):

        notification = Notification(

            user_id=user.id,

            title=title,

            message=message,

            notification_type=notification_type

        )

        return NotificationRepository.create(
            db,
            notification
        )

    # ----------------------------------------

    @staticmethod
    def get_notifications(
        db,
        user
    ):

        return NotificationRepository.get_by_user(
            db,
            user.id
        )

    # ----------------------------------------

    @staticmethod
    def mark_read(
        db,
        notification
    ):

        return NotificationRepository.mark_as_read(
            db,
            notification
        )