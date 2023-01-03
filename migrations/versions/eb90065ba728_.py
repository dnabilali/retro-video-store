"""empty message

Revision ID: eb90065ba728
Revises: 6b8c126afa38
Create Date: 2023-01-03 14:41:13.471516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb90065ba728'
down_revision = '6b8c126afa38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('name', sa.String(), nullable=False))
    op.add_column('customer', sa.Column('phone_number', sa.String(), nullable=False))
    op.add_column('customer', sa.Column('postal_code', sa.String(), nullable=False))
    op.add_column('customer', sa.Column('register_at', sa.DateTime(), nullable=False))
    op.add_column('customer', sa.Column('videos_checked_out_count', sa.Integer(), nullable=False))
    op.add_column('video', sa.Column('release_date', sa.DateTime(), nullable=True))
    op.add_column('video', sa.Column('title', sa.String(), nullable=False))
    op.add_column('video', sa.Column('total_inventory', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('video', 'total_inventory')
    op.drop_column('video', 'title')
    op.drop_column('video', 'release_date')
    op.drop_column('customer', 'videos_checked_out_count')
    op.drop_column('customer', 'register_at')
    op.drop_column('customer', 'postal_code')
    op.drop_column('customer', 'phone_number')
    op.drop_column('customer', 'name')
    # ### end Alembic commands ###