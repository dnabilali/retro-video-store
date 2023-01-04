"""empty message

Revision ID: 753d3e3b217f
Revises: 5c293d031382
Create Date: 2023-01-03 18:46:50.542942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '753d3e3b217f'
down_revision = '5c293d031382'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customer', 'register_at')
    op.drop_column('customer', 'phone')
    op.drop_column('customer', 'videos_checked_out_count')
    op.drop_column('customer', 'name')
    op.drop_column('customer', 'postal_code')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('postal_code', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('customer', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('customer', sa.Column('videos_checked_out_count', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('customer', sa.Column('phone', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('customer', sa.Column('register_at', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
