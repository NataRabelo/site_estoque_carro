"""Traduzindo colunas

Revision ID: 895d3e8835bc
Revises: 6371b4e80aed
Create Date: 2025-01-23 23:26:15.849464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '895d3e8835bc'
down_revision = '6371b4e80aed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modelo', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('marca', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('preco', sa.Float(), nullable=True))
        batch_op.drop_column('price')
        batch_op.drop_column('name')
        batch_op.drop_column('model')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.add_column(sa.Column('model', sa.VARCHAR(length=100), nullable=True))
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=100), nullable=True))
        batch_op.add_column(sa.Column('price', sa.FLOAT(), nullable=True))
        batch_op.drop_column('preco')
        batch_op.drop_column('marca')
        batch_op.drop_column('modelo')

    # ### end Alembic commands ###
