"""empty message

Revision ID: 84d70e43a20d
Revises: bb58ca8c3a08
Create Date: 2024-10-23 00:08:25.330327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84d70e43a20d'
down_revision = 'bb58ca8c3a08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('authors', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)

    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.drop_column('genre')
        batch_op.drop_column('author')
        batch_op.drop_column('editorial')

    with op.batch_alter_table('editorial', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)

    with op.batch_alter_table('genres', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('genres', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)

    with op.batch_alter_table('editorial', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)

    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('editorial', sa.VARCHAR(length=120), nullable=True))
        batch_op.add_column(sa.Column('author', sa.VARCHAR(length=120), nullable=True))
        batch_op.add_column(sa.Column('genre', sa.VARCHAR(length=120), nullable=True))
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)

    with op.batch_alter_table('authors', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)

    # ### end Alembic commands ###
