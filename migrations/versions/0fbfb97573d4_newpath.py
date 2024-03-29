"""newpath

Revision ID: 0fbfb97573d4
Revises: b501af266333
Create Date: 2018-11-04 23:59:44.721470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fbfb97573d4'
down_revision = 'b501af266333'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_tanty_word', table_name='tanty')
    op.drop_table('tanty')
    op.drop_table('pos_links')
    op.drop_index('ix_part_of_speech_name', table_name='part_of_speech')
    op.drop_table('part_of_speech')
    op.drop_index('ix_govern_model_name', table_name='govern_model')
    op.drop_table('govern_model')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('govern_model',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_govern_model_name', 'govern_model', ['name'], unique=False)
    op.create_table('part_of_speech',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.NUMERIC(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index('ix_part_of_speech_name', 'part_of_speech', ['name'], unique=False)
    op.create_table('pos_links',
    sa.Column('pos_id', sa.INTEGER(), nullable=True),
    sa.Column('tanty_pos_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['pos_id'], ['tanty.id'], ),
    sa.ForeignKeyConstraint(['tanty_pos_id'], ['tanty.id'], )
    )
    op.create_table('tanty',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('word', sa.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_tanty_word', 'tanty', ['word'], unique=False)
    # ### end Alembic commands ###
