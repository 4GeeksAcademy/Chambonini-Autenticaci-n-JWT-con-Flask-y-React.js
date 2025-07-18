"""Agrega columna lastname a User

Revision ID: eb2f6dd0ba12
Revises: 0763d677d453
Create Date: 2025-06-30 23:01:50.611189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb2f6dd0ba12'
down_revision = '0763d677d453'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('lastname', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('avatar', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('salt', sa.String(length=80), nullable=False))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=80),
               existing_nullable=False)
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.alter_column('email',
               existing_type=sa.String(length=80),
               type_=sa.VARCHAR(length=120),
               existing_nullable=False)
        batch_op.drop_column('salt')
        batch_op.drop_column('avatar')
        batch_op.drop_column('lastname')

    # ### end Alembic commands ###
