from sqlalchemy import String, Integer, Column, TIMESTAMP, text, ForeignKey
from .dataBase import Base


class Aluno(Base):
  __tablename__ = 'alunos'

  id = Column(Integer, primary_key=True, autoincrement=True)
  nome = Column(String(50), nullable=False)
  matricula = Column(String(50), nullable=False)
  #idade = Column(Integer, nullable=False)
  #email = Column(String(20), nullable=False)
  curso_id = Column(Integer, ForeignKey('cursos.id'))
  #periodo = Column(Integer, nullable=False, server_default="0")
  #cidade = Column(String(40))
  #estado = Column(String(2))
  #pais = Column(String(40))
  added_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))