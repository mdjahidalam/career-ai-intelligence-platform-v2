from sqlalchemy.orm import Session

from app.models.job import Job

from app.repositories.base_repository import BaseRepository


class JobRepository(

    BaseRepository[Job]

):

    def __init__(self):

        super().__init__(Job)

    # ----------------------------------

    def search(

        self,

        db: Session,

        keyword: str

    ):

        return (

            db.query(Job)

            .filter(

                Job.job_title.contains(

                    keyword

                )

            )

            .all()

        )