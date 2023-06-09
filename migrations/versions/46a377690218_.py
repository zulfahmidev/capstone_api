"""empty message

Revision ID: 46a377690218
Revises: dc378b6eda0a
Create Date: 2023-06-07 16:33:46.728232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46a377690218'
down_revision = 'dc378b6eda0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('options', schema=None) as batch_op:
        batch_op.add_column(sa.Column('weight', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('options', schema=None) as batch_op:
        batch_op.drop_column('weight')

    # ### end Alembic commands ###
