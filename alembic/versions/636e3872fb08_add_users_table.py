"""add users table

Revision ID: 636e3872fb08
Revises: 727278441592
Create Date: 2021-11-20 17:57:35.317936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '636e3872fb08'
down_revision = '727278441592'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False), sa.Column('email', sa.String(), nullable=False), sa.Column('password', sa.String(), nullable=False), sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False), sa.PrimaryKeyConstraint('id'), sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
