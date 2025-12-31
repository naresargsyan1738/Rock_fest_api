"""convert members to jsonb

Revision ID: df6b72c36f1c
Revises: 74d9632ef0e6
Create Date: 2025-12-31 12:28:37.395915

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'df6b72c36f1c'
down_revision: Union[str, Sequence[str], None] = 'c95326c7f0a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("ALTER TABLE rock_groups ALTER COLUMN members TYPE jsonb USING members::jsonb;")

def downgrade():
    op.execute("ALTER TABLE rock_groups ALTER COLUMN members TYPE json USING members::text;")
