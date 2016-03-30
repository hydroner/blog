"""empty message

Revision ID: 7f91fea70c40
Revises: f15fff2d268a
Create Date: 2016-03-30 14:53:01.945694

"""

# revision identifiers, used by Alembic.
revision = '7f91fea70c40'
down_revision = 'f15fff2d268a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('member_since', sa.DateTime(), nullable=True))
    op.drop_column('users', 'member_me')
    op.drop_column('users', 'name')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.VARCHAR(length=64), nullable=True))
    op.add_column('users', sa.Column('member_me', sa.DATETIME(), nullable=True))
    op.drop_column('users', 'member_since')
    ### end Alembic commands ###
