# Generated by Django 4.1.3 on 2022-12-20 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_api', '0004_remove_responsavel_celular_responsavel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=200)),
                ('cep', models.CharField(blank=True, max_length=8, null=True)),
                ('endereco', models.CharField(blank=True, max_length=200, null=True)),
                ('numero_endereco', models.CharField(blank=True, max_length=20, null=True)),
                ('complemento', models.CharField(blank=True, max_length=200, null=True)),
                ('bairro', models.CharField(blank=True, max_length=200, null=True)),
                ('cidade', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='atendido',
            name='escola',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_api.escola'),
        ),
    ]
