"""add foundation_year column

Revision ID: 51745a54403b
Revises: 
Create Date: 2025-12-31 05:03:44.326712

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '51745a54403b'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('rock_groups', sa.Column('foundation_year', sa.Integer(), nullable=True)) 


def downgrade():
    op.drop_column('rock_groups', 'foundation_year')
