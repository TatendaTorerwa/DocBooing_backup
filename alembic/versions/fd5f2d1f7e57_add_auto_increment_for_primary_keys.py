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

    # Modify the existing primary key column for each table
    for table in ['Doctor', 'Patient', 'Location', 'Reviews', 'Appointments', 'Specialty', 'PatientAppointment', 'Availability']:
        # Check if the primary key column already exists
        if op.get_context().dialect.has_table(op.get_bind(), table):
            columns = op.get_context().dialect.get_columns(op.get_bind(), table)
            for column in columns:
                # Ensure 'primary_key' and 'autoincrement' attributes exist before accessing them
                if hasattr(column, 'primary_key') and hasattr(column, 'autoincrement'):
                    if column.primary_key and not column.autoincrement:
                        op.alter_column(table, column.name, autoincrement=True)

    # Re-enable foreign key checks
    op.execute("SET FOREIGN_KEY_CHECKS = 1;")


def downgrade() -> None:
    pass
