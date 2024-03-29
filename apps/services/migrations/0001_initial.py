# Generated by Django 5.0.1 on 2024-01-24 02:55

import django.db.models.deletion
import tinymce.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Budgets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('status', models.CharField(choices=[('OS', 'Orçamento solicitado'), ('EA', 'Em análise'), ('R', 'Realizado'), ('C', 'Cancelado'), ('F', 'Fechado')], default='OS', max_length=2)),
                ('service_tag', models.CharField(choices=[('M', 'Motion design'), ('EI', 'Edição de imagem'), ('EV', 'Edição de video')], max_length=2)),
                ('descricao', tinymce.models.HTMLField()),
                ('file_path', models.CharField(max_length=300)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
