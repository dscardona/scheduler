"""make certain columns not nullable

Revision ID: ece532607554
Revises: 6e4be2d8c295
Create Date: 2022-11-22 09:53:02.506495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ece532607554'
down_revision = '6e4be2d8c295'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('schedule', 'employee_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('schedule', 'assignment_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('schedule', 'assignment_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('schedule', 'employee_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###