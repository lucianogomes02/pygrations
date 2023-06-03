"""primeira-migration

Revision ID: 3148ad2196c8
Revises: 
Create Date: 2023-06-03 02:40:25.374079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3148ad2196c8"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "pessoa",
        sa.Column("id", sa.UUID, primary_key=True),
        sa.Column("nome", sa.String(length=50), nullable=False),
        sa.Column("email", sa.String(length=50), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("pessoa")
