"""empty message

Revision ID: 0a61f21f7831
Revises: 34a1663e3832
Create Date: 2023-05-17 14:17:46.977218

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0a61f21f7831"
down_revision = "34a1663e3832"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "businesscard",
        sa.Column("job_title", sa.VARCHAR(length=50), nullable=False),
        sa.Column("specificity", sa.VARCHAR(length=50), nullable=False),
        sa.Column("phone", sa.VARCHAR(length=12), nullable=True),
        sa.Column("email", sa.VARCHAR(length=254), nullable=False),
        sa.Column("address", sa.TEXT(), nullable=True),
        sa.Column("first_name", sa.VARCHAR(length=50), nullable=False),
        sa.Column("last_name", sa.VARCHAR(length=50), nullable=False),
        sa.Column("tg_url", sa.VARCHAR(length=50), nullable=True),
        sa.Column("vk_url", sa.VARCHAR(length=50), nullable=True),
        sa.Column("fb_url", sa.VARCHAR(length=50), nullable=True),
        sa.Column("own_site_url", sa.TEXT(), nullable=True),
        sa.Column("summary_url", sa.TEXT(), nullable=True),
        sa.Column("company_logo", sa.TEXT(), nullable=True),
        sa.Column("bio", sa.VARCHAR(length=500), nullable=True),
        sa.Column("bc_template_type", sa.TEXT(), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.alter_column(
        "users", "first_name", existing_type=sa.VARCHAR(length=15), type_=sa.VARCHAR(length=50), existing_nullable=True
    )
    op.alter_column(
        "users", "last_name", existing_type=sa.VARCHAR(length=40), type_=sa.VARCHAR(length=50), existing_nullable=True
    )
    op.alter_column(
        "users", "email", existing_type=sa.VARCHAR(length=90), type_=sa.VARCHAR(length=254), existing_nullable=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users", "email", existing_type=sa.VARCHAR(length=254), type_=sa.VARCHAR(length=90), existing_nullable=False
    )
    op.alter_column(
        "users", "last_name", existing_type=sa.VARCHAR(length=50), type_=sa.VARCHAR(length=40), existing_nullable=True
    )
    op.alter_column(
        "users", "first_name", existing_type=sa.VARCHAR(length=50), type_=sa.VARCHAR(length=15), existing_nullable=True
    )
    op.drop_table("businesscard")
    # ### end Alembic commands ###
