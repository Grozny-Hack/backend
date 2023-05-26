"""empty message

Revision ID: b69063b2574f
Revises:
Create Date: 2023-05-05 22:00:03.300001

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "b69063b2574f"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "profiles",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("first_name", sa.VARCHAR(length=15), nullable=False),
        sa.Column("last_name", sa.VARCHAR(length=40), nullable=False),
        sa.Column("email", sa.VARCHAR(length=90), nullable=False),
        sa.Column("picture_url", sa.TEXT(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("profiles")
    # ### end Alembic commands ###