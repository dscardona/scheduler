"""add employee table

Revision ID: 1819696925c5
Revises: e6d01d9be8c8
Create Date: 2022-11-22 09:45:58.290682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1819696925c5'
down_revision = 'e6d01d9be8c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=128), nullable=False),
    sa.Column('last_name', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('extension', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees')
    # ### end Alembic commands ###
