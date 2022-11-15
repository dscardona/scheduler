"""create schedulers

Revision ID: 63c2cb30f2d3
Revises: 
Create Date: 2022-11-15 16:02:16.411405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63c2cb30f2d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE schedulers(
            id SERIAL PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE schedulers;
        """
    )
