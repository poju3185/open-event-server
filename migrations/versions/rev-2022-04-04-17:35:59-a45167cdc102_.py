"""empty message

Revision ID: a45167cdc102
Revises: 0dba0c2e0ba0
Create Date: 2022-04-04 17:35:59.622520

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'a45167cdc102'
down_revision = '0dba0c2e0ba0'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('stream_loop', sa.Boolean(), nullable=True))
    op.add_column('events', sa.Column('stream_autoplay', sa.Boolean(), nullable=True))
    op.add_column('events_version', sa.Column('stream_loop', sa.Boolean(), autoincrement=False, nullable=True))
    op.add_column('events_version', sa.Column('stream_autoplay', sa.Boolean(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events_version', 'stream_autoplay')
    op.drop_column('events_version', 'stream_loop')
    op.drop_column('events', 'stream_autoplay')
    op.drop_column('events', 'stream_loop')
    # ### end Alembic commands ###