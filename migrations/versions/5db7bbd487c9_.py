"""empty message

Revision ID: 5db7bbd487c9
Revises: 
Create Date: 2021-02-22 20:07:19.745812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5db7bbd487c9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('drink')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('drink',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=80), nullable=True),
    sa.Column('recipe', sa.VARCHAR(length=180), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###
