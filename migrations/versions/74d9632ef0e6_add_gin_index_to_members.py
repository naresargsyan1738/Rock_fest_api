"""add gin index to members

Revision ID: 74d9632ef0e6
Revises: 89b9ad771bbc
Create Date: 2025-12-31 12:04:54.373932

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74d9632ef0e6'
down_revision: Union[str, Sequence[str], None] = 'c95326c7f0a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm;")
    op.execute("CREATE INDEX idx_members_gin ON rock_groups USING gin ((members));")

def downgrade():
    op.execute("DROP INDEX IF EXISTS idx_members_gin;")
