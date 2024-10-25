"""empty message

Revision ID: d13455b4a117
Revises: 904ba16c7804
Create Date: 2024-10-25 23:51:39.211162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd13455b4a117'
down_revision = '904ba16c7804'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('genre_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('author_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('editorial_id', sa.Integer(), nullable=False))
        
        # Adding foreign keys with names
        batch_op.create_foreign_key('fk_books_genre', 'genres', ['genre_id'], ['id'])
        batch_op.create_foreign_key('fk_books_editorial', 'editorial', ['editorial_id'], ['id'])
        batch_op.create_foreign_key('fk_books_author', 'authors', ['author_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        # Dropping foreign keys with specified names
        batch_op.drop_constraint('fk_books_genre', type_='foreignkey')
        batch_op.drop_constraint('fk_books_editorial', type_='foreignkey')
        batch_op.drop_constraint('fk_books_author', type_='foreignkey')
        
        batch_op.drop_column('editorial_id')
        batch_op.drop_column('author_id')
        batch_op.drop_column('genre_id')

    # ### end Alembic commands ###