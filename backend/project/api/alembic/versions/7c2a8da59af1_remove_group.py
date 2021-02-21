"""Remove group

Revision ID: 7c2a8da59af1
Revises: 8e0976fba17a
Create Date: 2021-02-21 02:55:46.232995

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c2a8da59af1'
down_revision = '8e0976fba17a'
branch_labels = None
depends_on = None


def upgrade():
    # op.drop_table('groups')
    # op.drop_table('todo')
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
        'todo',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('created_at', sa.DateTime, default=datetime.now),
        sa.Column('updated_at', sa.DateTime, default=datetime.now, onupdate=datetime.now),
        sa.Column('title', sa.String),
        sa.Column('description', sa.String),
        sa.Column('status', sa.String),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
    )


def downgrade():
    op.create_table(
        'groups',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('created_at', sa.DateTime, default=datetime.now),
        sa.Column('updated_at', sa.DateTime, default=datetime.now, onupdate=datetime.now),
        sa.Column('groupname', sa.String),
        sa.Column('user_name', sa.String, sa.ForeignKey('users.name'))
        
    )
    op.create_table(
        'todo',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('created_at', sa.DateTime, default=datetime.now),
        sa.Column('updated_at', sa.DateTime, default=datetime.now, onupdate=datetime.now),
        sa.Column('title', sa.String),
        sa.Column('description', sa.String),
        sa.Column('status', sa.String),
        sa.Column('user_name', sa.String, sa.ForeignKey('users.name')),
        # sa.Column('group_name', sa.String, sa.ForeignKey('groups.name')),
    )
