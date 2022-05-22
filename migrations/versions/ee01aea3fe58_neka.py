"""Neka

Revision ID: ee01aea3fe58
Revises: 
Create Date: 2022-05-21 02:36:52.034022

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee01aea3fe58'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('jar', 'date_added')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jar', sa.Column('date_added', sa.DATETIME(), nullable=False))
    # ### end Alembic commands ###