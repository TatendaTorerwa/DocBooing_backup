"""Update Patient table

Revision ID: 6dc254045d45
Revises: 
Create Date: 2024-03-28 11:24:50.198905

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '6dc254045d45'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_SpecialtyID', table_name='Specialty')
    op.drop_table('Specialty')
    op.drop_table('Availability')
    op.drop_index('idx_LocationID', table_name='Location')
    op.drop_table('Location')
    op.drop_table('PatientAppointment')
    op.drop_table('Patient')
    op.drop_table('Doctor')
    op.drop_table('Reviews')
    op.drop_table('Appointments')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Appointments',
    sa.Column('AppointmentID', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('PatientID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('DoctorID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('AppointmentTime', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['DoctorID'], ['Doctor.DoctorID'], name='Appointments_ibfk_2'),
    sa.ForeignKeyConstraint(['PatientID'], ['Patient.PatientID'], name='Appointments_ibfk_1'),
    sa.PrimaryKeyConstraint('AppointmentID'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('Reviews',
    sa.Column('ReviewID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('DoctorID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('PatientID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Rating', mysql.DECIMAL(precision=10, scale=0), nullable=True),
    sa.Column('Comment', mysql.TEXT(), nullable=True),
    sa.Column('DatePosted', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['DoctorID'], ['Doctor.DoctorID'], name='FK_Reviews_DoctorID'),
    sa.ForeignKeyConstraint(['DoctorID'], ['Doctor.DoctorID'], name='Reviews_ibfk_1'),
    sa.ForeignKeyConstraint(['PatientID'], ['Patient.PatientID'], name='Reviews_ibfk_2'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('Doctor',
    sa.Column('DoctorID', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('FullName', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('SpecialtyID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LocationID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('AppointmentDateTime', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['LocationID'], ['Location.LocationID'], name='Doctor_ibfk_2'),
    sa.ForeignKeyConstraint(['SpecialtyID'], ['Specialty.SpecialtyID'], name='Doctor_ibfk_1'),
    sa.PrimaryKeyConstraint('DoctorID'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('Patient',
    sa.Column('PatientID', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Username', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('Email', mysql.VARCHAR(length=75), nullable=False),
    sa.Column('Password', mysql.VARCHAR(length=30), nullable=False),
    sa.PrimaryKeyConstraint('PatientID'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('PatientAppointment',
    sa.Column('PatientAppointmentID', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('PatientID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('AppointmentID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ReminderDateTime', mysql.DATETIME(), nullable=True),
    sa.Column('NotificationSent', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('PatientAppointmentID'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('Location',
    sa.Column('LocationID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('LocationName', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('Address', mysql.VARCHAR(length=150), nullable=True),
    sa.Column('City', mysql.VARCHAR(length=120), nullable=True),
    sa.Column('State', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('Zipcode', mysql.VARCHAR(length=12), nullable=True),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('idx_LocationID', 'Location', ['LocationID'], unique=False)
    op.create_table('Availability',
    sa.Column('AvailabilityID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('DoctorID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('DayOfWeek', mysql.ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'), nullable=True),
    sa.Column('StartTime', mysql.TIME(), nullable=True),
    sa.Column('EndTime', mysql.TIME(), nullable=True),
    sa.ForeignKeyConstraint(['DoctorID'], ['Doctor.DoctorID'], name='FK_DoctorID'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('Specialty',
    sa.Column('SpecialtyID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('SpecialtyName', mysql.VARCHAR(length=80), nullable=True),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('idx_SpecialtyID', 'Specialty', ['SpecialtyID'], unique=False)
    # ### end Alembic commands ###
