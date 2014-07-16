# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'QuizTranslation'
        db.create_table('career_quiz_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['career.Quiz'])),
        ))
        db.send_create_signal('career', ['QuizTranslation'])

        # Adding unique constraint on 'QuizTranslation', fields ['language_code', 'master']
        db.create_unique('career_quiz_translation', ['language_code', 'master_id'])

        # Adding model 'Quiz'
        db.create_table('career_quiz', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('career', ['Quiz'])

        # Adding model 'AnswerTranslation'
        db.create_table('career_answer_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['career.Answer'])),
        ))
        db.send_create_signal('career', ['AnswerTranslation'])

        # Adding unique constraint on 'AnswerTranslation', fields ['language_code', 'master']
        db.create_unique('career_answer_translation', ['language_code', 'master_id'])

        # Adding model 'Answer'
        db.create_table('career_answer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('career', ['Answer'])

        # Adding model 'QuestionTranslation'
        db.create_table('career_question_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('help_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['career.Question'])),
        ))
        db.send_create_signal('career', ['QuestionTranslation'])

        # Adding unique constraint on 'QuestionTranslation', fields ['language_code', 'master']
        db.create_unique('career_question_translation', ['language_code', 'master_id'])

        # Adding model 'Question'
        db.create_table('career_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('quiz', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['career.Quiz'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('career', ['Question'])

        # Adding model 'QuizToCareer'
        db.create_table('career_quiztocareer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quiz', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['career.Quiz'])),
            ('career', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['career.Career'])),
            ('passed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('due_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('career', ['QuizToCareer'])

        # Adding model 'Career'
        db.create_table('career_career', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('career', ['Career'])

        # Adding model 'Student'
        db.create_table('career_student', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('career', ['Student'])

        # Adding model 'Teacher'
        db.create_table('career_teacher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('career', ['Teacher'])

        # Adding model 'StudentToTeacher'
        db.create_table('career_studenttoteacher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['career.Student'])),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['career.Teacher'])),
        ))
        db.send_create_signal('career', ['StudentToTeacher'])


    def backwards(self, orm):
        # Removing unique constraint on 'QuestionTranslation', fields ['language_code', 'master']
        db.delete_unique('career_question_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'AnswerTranslation', fields ['language_code', 'master']
        db.delete_unique('career_answer_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'QuizTranslation', fields ['language_code', 'master']
        db.delete_unique('career_quiz_translation', ['language_code', 'master_id'])

        # Deleting model 'QuizTranslation'
        db.delete_table('career_quiz_translation')

        # Deleting model 'Quiz'
        db.delete_table('career_quiz')

        # Deleting model 'AnswerTranslation'
        db.delete_table('career_answer_translation')

        # Deleting model 'Answer'
        db.delete_table('career_answer')

        # Deleting model 'QuestionTranslation'
        db.delete_table('career_question_translation')

        # Deleting model 'Question'
        db.delete_table('career_question')

        # Deleting model 'QuizToCareer'
        db.delete_table('career_quiztocareer')

        # Deleting model 'Career'
        db.delete_table('career_career')

        # Deleting model 'Student'
        db.delete_table('career_student')

        # Deleting model 'Teacher'
        db.delete_table('career_teacher')

        # Deleting model 'StudentToTeacher'
        db.delete_table('career_studenttoteacher')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'career.answer': {
            'Meta': {'object_name': 'Answer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'career.answertranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'AnswerTranslation', 'db_table': "'career_answer_translation'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['career.Answer']"})
        },
        'career.career': {
            'Meta': {'object_name': 'Career'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quizzes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['career.Quiz']", 'null': 'True', 'through': "orm['career.QuizToCareer']", 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'career.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quiz': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['career.Quiz']"}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'career.questiontranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'QuestionTranslation', 'db_table': "'career_question_translation'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'help_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['career.Question']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        'career.quiz': {
            'Meta': {'object_name': 'Quiz'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'career.quiztocareer': {
            'Meta': {'object_name': 'QuizToCareer'},
            'career': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['career.Career']"}),
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'passed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'quiz': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['career.Quiz']"})
        },
        'career.quiztranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'QuizTranslation', 'db_table': "'career_quiz_translation'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['career.Quiz']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        'career.student': {
            'Meta': {'object_name': 'Student'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'career.studenttoteacher': {
            'Meta': {'object_name': 'StudentToTeacher'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['career.Student']"}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['career.Teacher']"})
        },
        'career.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['career.Student']", 'null': 'True', 'through': "orm['career.StudentToTeacher']", 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['career']