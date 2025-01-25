"""Correção de nome da coluna Ano -> ano

Revision ID: ae56f185571f
Revises: e90ecbd84b9a
Create Date: 2025-01-25 00:31:27.398854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae56f185571f'
down_revision = 'e90ecbd84b9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ano', sa.Integer(), nullable=True))
        batch_op.drop_column('Ano')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Ano', sa.INTEGER(), nullable=True))
        batch_op.drop_column('ano')

    # ### end Alembic commands ###
