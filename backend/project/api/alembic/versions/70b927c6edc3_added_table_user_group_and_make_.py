"""Added table user, group and make relationship.

Revision ID: 70b927c6edc3
Revises: 2d930c47f9c0
Create Date: 2021-02-21 02:11:10.173314

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70b927c6edc3'
down_revision = '2d930c47f9c0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('created_at', sa.DateTime, default=datetime.now),
        sa.Column('updated_at', sa.DateTime, default=datetime.now, onupdate=datetime.now),
        sa.Column('name', sa.String),
        sa.Column('email', sa.String),
        sa.Column('password', sa.String)
    )

    op.create_table(
        'groups',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('created_at', sa.DateTime, default=datetime.now),
        sa.Column('updated_at', sa.DateTime, default=datetime.now, onupdate=datetime.now),
        sa.Column('groupname', sa.String),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'))
        
    )
    op.create_table(
        'todo',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('created_at', sa.DateTime, default=datetime.now),
        sa.Column('updated_at', sa.DateTime, default=datetime.now, onupdate=datetime.now),
        sa.Column('title', sa.String),
        sa.Column('description', sa.String),
        sa.Column('status', sa.String),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('group_id', sa.Integer, sa.ForeignKey('groups.id')),
    )


def downgrade():
    op.droup_table('users')
    op.droup_table('groups')
    op.droup_table('todo')
    op.create_table(
        'todoitem',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String),
        sa.Column('description', sa.String),
    )
