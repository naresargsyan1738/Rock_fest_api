from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_index('idx_rockgroup_name', 'rock_groups', ['name'])


def downgrade():
    op.drop_index('idx_rockgroup_name', table_name='rock_groups')
