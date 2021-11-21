"""add content column to post table

Revision ID: 727278441592
Revises: c7018221f7db
Create Date: 2021-11-20 17:44:08.766519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '727278441592'
down_revision = 'c7018221f7db'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
