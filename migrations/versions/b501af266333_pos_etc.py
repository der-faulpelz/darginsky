"""pos etc

Revision ID: b501af266333
Revises: 6b41f1adeefc
Create Date: 2018-11-04 23:06:42.448455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b501af266333'
down_revision = '6b41f1adeefc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('govern_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_govern_model_name'), 'govern_model', ['name'], unique=False)
    op.create_table('tanty',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tanty_word'), 'tanty', ['word'], unique=False)
    op.create_table('pos_links',
    sa.Column('pos_id', sa.Integer(), nullable=True),
    sa.Column('tanty_pos_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pos_id'], ['tanty.id'], ),
    sa.ForeignKeyConstraint(['tanty_pos_id'], ['tanty.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pos_links')
    op.drop_index(op.f('ix_tanty_word'), table_name='tanty')
    op.drop_table('tanty')
    op.drop_index(op.f('ix_govern_model_name'), table_name='govern_model')
    op.drop_table('govern_model')
    # ### end Alembic commands ###