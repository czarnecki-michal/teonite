# Generated by Django 2.2 on 2019-07-31 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='article',
            options={},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_content',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='article',
            name='article_author',
        ),
        migrations.AddField(
            model_name='article',
            name='author_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='articles.Author'),
        ),
    ]