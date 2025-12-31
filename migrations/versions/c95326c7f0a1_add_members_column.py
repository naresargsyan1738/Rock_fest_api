"""add members column

Revision ID: c95326c7f0a1
Revises: 74d9632ef0e6
Create Date: 2025-12-31 12:11:17.370388
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = 'c95326c7f0a1'
down_revision: Union[str, Sequence[str], None] = '89b9ad771bbc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.add_column('rock_groups', sa.Column('members', sa.JSON(), nullable=True))

def downgrade() -> None:
    op.drop_column('rock_groups', 'members')
