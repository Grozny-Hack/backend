"""empty message

Revision ID: 34a1663e3832
Revises: eda166fd66a9
Create Date: 2023-05-10 19:47:55.307256

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "34a1663e3832"
down_revision = "eda166fd66a9"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("users", "first_name", existing_type=sa.VARCHAR(length=50), nullable=True)
    op.alter_column("users", "last_name", existing_type=sa.VARCHAR(length=50), nullable=True)
    op.alter_column("users", "picture_url", existing_type=sa.TEXT(), nullable=True)
    op.alter_column("users", "hashed_password", existing_type=sa.TEXT(), nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("users", "picture_url", existing_type=sa.TEXT(), nullable=False)
    op.alter_column("users", "last_name", existing_type=sa.VARCHAR(length=40), nullable=False)
    op.alter_column("users", "first_name", existing_type=sa.VARCHAR(length=15), nullable=False)
    op.alter_column("users", "hashed_password", existing_type=sa.TEXT(), nullable=False)
    # ### end Alembic commands ###
