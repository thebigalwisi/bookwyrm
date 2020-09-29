# Generated by Django 3.0.3 on 2020-03-21 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookwyrm', '0018_favorite_remote_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('status_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bookwyrm.Status')),
                ('name', models.CharField(max_length=255)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookwyrm.Book')),
            ],
            options={
                'abstract': False,
            },
            bases=('bookwyrm.status',),
        ),
    ]