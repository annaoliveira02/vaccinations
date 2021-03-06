"""Criando tabela de vacinas

Revision ID: 0526692ab24c
Revises: 
Create Date: 2021-11-22 18:46:31.513111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0526692ab24c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vaccine_cards',
    sa.Column('cpf', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('cpf')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vaccine_cards')
    # ### end Alembic commands ###
