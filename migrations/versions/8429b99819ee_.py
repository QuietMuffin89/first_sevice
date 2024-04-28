"""empty message

Revision ID: 8429b99819ee
Revises: cf86b996b147
Create Date: 2024-04-28 15:45:44.140645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8429b99819ee'
down_revision = 'cf86b996b147'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('webtoons', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(), nullable=True))
        batch_op.create_index(batch_op.f('ix_webtoons_title'), ['title'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('webtoons', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_webtoons_title'))
        batch_op.drop_column('title')

    # ### end Alembic commands ###
