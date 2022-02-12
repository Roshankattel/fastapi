"""add users

Revision ID: 3280ecb9b68d
Revises: dd493125f427
Create Date: 2022-02-12 21:10:06.871056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3280ecb9b68d'
down_revision = 'dd493125f427'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    # another way to set primary key
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
