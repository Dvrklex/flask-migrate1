"""migrando itec db

Revision ID: 38baa31af459
Revises: 
Create Date: 2022-09-03 14:39:30.841035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38baa31af459'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pais',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sexo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tipo_usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('descripcion', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tipodni',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('provincia',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('idPais', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['idPais'], ['pais.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('localidad',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('idProvincia', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idProvincia'], ['provincia.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('persona',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('idTipodni', sa.Integer(), nullable=False),
    sa.Column('dni', sa.String(length=8), nullable=False),
    sa.Column('direccion', sa.String(length=50), nullable=False),
    sa.Column('idLocalidad', sa.Integer(), nullable=False),
    sa.Column('idPais', sa.Integer(), nullable=False),
    sa.Column('f_nacimiento', sa.Date(), nullable=False),
    sa.Column('idSexo', sa.Integer(), nullable=False),
    sa.Column('telefono', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('f_carga', sa.Date(), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['idLocalidad'], ['localidad.id'], ),
    sa.ForeignKeyConstraint(['idPais'], ['pais.id'], ),
    sa.ForeignKeyConstraint(['idSexo'], ['sexo.id'], ),
    sa.ForeignKeyConstraint(['idTipodni'], ['tipodni.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('contrasenia', sa.String(length=50), nullable=False),
    sa.Column('idTipoUsuario', sa.Integer(), nullable=False),
    sa.Column('idPersona', sa.Integer(), nullable=False),
    sa.Column('f_carga', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['idPersona'], ['persona.id'], ),
    sa.ForeignKeyConstraint(['idTipoUsuario'], ['tipo_usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuario')
    op.drop_table('persona')
    op.drop_table('localidad')
    op.drop_table('provincia')
    op.drop_table('tipodni')
    op.drop_table('tipo_usuario')
    op.drop_table('sexo')
    op.drop_table('pais')
    # ### end Alembic commands ###
