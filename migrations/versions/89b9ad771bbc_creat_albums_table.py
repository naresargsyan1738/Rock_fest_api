"""creat albums table

Revision ID: 89b9ad771bbc
Revises: 2b176da1ad40
Create Date: 2025-12-31 05:59:00.898862

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '89b9ad771bbc'
down_revision: Union[str, Sequence[str], None] = '2b176da1ad40'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        'albums',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('group_id', sa.Integer(), sa.ForeignKey('rock_groups.id'))
    )


def downgrade() -> None:
    op.drop_table('albums')
