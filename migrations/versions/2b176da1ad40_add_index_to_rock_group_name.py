from alembic import op
import sqlalchemy as sa

revision = '2b176da1ad40'
down_revision = '51745a54403b'   
branch_labels = None
depends_on = None

def upgrade():
    op.create_index('idx_rockgroup_name', 'rock_groups', ['name'])

def downgrade():
    op.drop_index('idx_rockgroup_name', table_name='rock_groups')
