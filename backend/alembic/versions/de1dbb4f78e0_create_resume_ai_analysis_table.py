"""create resume ai analysis table

Revision ID: de1dbb4f78e0
Revises: 20e33f499720
Create Date: 2026-07-28 22:49:55.733087

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de1dbb4f78e0'
down_revision: Union[str, Sequence[str], None] = "530d8cd5e881"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():

    op.create_table(
        "resume_ai_analysis",

        sa.Column("id", sa.Integer(), primary_key=True),

        sa.Column(
            "resume_id",
            sa.Integer(),
            sa.ForeignKey("resumes.id"),
            nullable=False
        ),

        sa.Column(
            "parsed_json",
            sa.JSON(),
            nullable=False
        ),

        sa.Column(
            "placement_probability",
            sa.Float(),
            nullable=True
        ),

        sa.Column(
            "predicted_salary",
            sa.Float(),
            nullable=True
        ),

        sa.Column(
            "career_level",
            sa.Integer(),
            nullable=True
        ),

        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now()
        )
    )

    op.create_index(
        "ix_resume_ai_analysis_id",
        "resume_ai_analysis",
        ["id"]
    )

def downgrade():

    op.drop_index(
        "ix_resume_ai_analysis_id",
        table_name="resume_ai_analysis"
    )

    op.drop_table(
        "resume_ai_analysis"
    )