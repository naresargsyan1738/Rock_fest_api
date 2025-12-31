"""merge heads

Revision ID: ef9076dd09be
Revises: 74d9632ef0e6, df6b72c36f1c
Create Date: 2025-12-31 12:36:49.446413

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ef9076dd09be'
down_revision: Union[str, Sequence[str], None] = ('74d9632ef0e6', 'df6b72c36f1c')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
