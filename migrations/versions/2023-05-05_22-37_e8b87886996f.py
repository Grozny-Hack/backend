"""empty message

Revision ID: e8b87886996f
Revises: b69063b2574f
Create Date: 2023-05-05 22:37:26.831584

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "e8b87886996f"
down_revision = "b69063b2574f"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("profiles", sa.Column("hashed_password", sa.TEXT(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("profiles", "hashed_password")
    # ### end Alembic commands ###
