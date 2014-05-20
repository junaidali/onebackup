__author__ = 'junaid'

from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class BackupJob(Base):
    """
    This object describes each backup job in the system
    """
    __tablename__ = 'backupjob'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def __repr__(self):
        """
        String representation
        """
        return "<BackupJob(id=%s, name=%s, description=%s>" %(self.id, self.name,self.description)