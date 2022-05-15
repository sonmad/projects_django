from django.db import models

class Project(models.Model):
    
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
   # auto_increment_id = models.AutoField(primary_key=True)
    projectnumber = models.CharField(db_column='ProjectNumber', verbose_name='Projektnummer', max_length=100, db_collation='Danish_Norwegian_CI_AS', blank=False, null=False)  # Field name made lowercase.
    title = models.CharField(db_column='Title', verbose_name='Titel', max_length=255, db_collation='Danish_Norwegian_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', verbose_name='Beskrivelse', max_length=255, db_collation='Danish_Norwegian_CI_AS', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', verbose_name='Startdato', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', verbose_name='Slutdato', blank=True, null=True)  # Field name made lowercase.
    confidential = models.BooleanField(db_column='Confidential', verbose_name='Klassifikation', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    
 
# Metadata
    class Meta:
        managed = False
        db_table = 'Project'

    def __str__(self):
        return self.projectnumber

class Projectlink(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    projectid = models.ForeignKey(Project, models.DO_NOTHING, db_column='ProjectId', related_name='projectlinks', blank=True, null=True)  # Field name made lowercase. 
    category = models.CharField(db_column='Category', max_length=50, db_collation='Danish_Norwegian_CI_AS', blank=True, null=True)  # Field name made lowercase.
    linkname = models.CharField(db_column='LinkName', max_length=100, db_collation='Danish_Norwegian_CI_AS', blank=True, null=True)  # Field name made lowercase.
    link = models.TextField(db_column='Link', db_collation='Danish_Norwegian_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProjectLink'
        # Methods
    def __str__(self):
        return self.link
   

