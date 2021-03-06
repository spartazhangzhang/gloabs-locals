"""empty message

Revision ID: 291a976f334e
Revises: e001416b8f4e
Create Date: 2018-04-24 10:59:31.212000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '291a976f334e'
down_revision = 'e001416b8f4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('movie', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comment', 'in_movies', ['movie'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_column('comment', 'movie')
    # ### end Alembic commands ###
