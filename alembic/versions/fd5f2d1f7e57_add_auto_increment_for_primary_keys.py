"""Add_auto_increment_for_primary_keys

Revision ID: fd5f2d1f7e57
Revises: 82d4c52a8a4a
Create Date: 2024-03-28 13:44:28.351036

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fd5f2d1f7e57'
down_revision: Union[str, None] = '82d4c52a8a4a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Disable foreign key checks temporarily
    op.execute("SET FOREIGN_KEY_CHECKS = 0;")

    # Iterate over each table
    for table in ['Doctor', 'Patient', 'Location', 'Reviews', 'Appointments', 'Specialty', 'PatientAppointment', 'Availability']:
        # Create a new primary key column
        op.add_column(table, sa.Column('id', sa.Integer(), nullable=False, autoincrement=True, primary_key=True))

        # Drop the old primary key column
        with op.batch_alter_table(table, reflect_args=[sa.Column('id')]) as batch_op:
            batch_op.drop_column(f'{table}ID')

    # Re-enable foreign key checks
    op.execute("SET FOREIGN_KEY_CHECKS = 1;")

def downgrade() -> None:
    pass
