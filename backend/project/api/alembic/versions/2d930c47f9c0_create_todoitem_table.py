"""create todoitem table

Revision ID: 2d930c47f9c0
Revises: 
Create Date: 2021-02-15 14:33:49.755049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d930c47f9c0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'todoitem',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String),
        sa.Column('description', sa.String),
    )


def downgrade():
    op.drop_table('todoitem')
