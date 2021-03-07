"""add logined in user model.

Revision ID: f17131854336
Revises: 7c2a8da59af1
Create Date: 2021-03-05 11:48:07.108957

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f17131854336'
down_revision = '7c2a8da59af1'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('users')
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('created_at', sa.DateTime, default=datetime.now),
        sa.Column('updated_at', sa.DateTime, default=datetime.now, onupdate=datetime.now),
        sa.Column('name', sa.String),
        sa.Column('email', sa.String),
        sa.Column('password', sa.String),
        sa.Column('logined', sa.Boolean, default=False)
    )


def downgrade():
    pass
