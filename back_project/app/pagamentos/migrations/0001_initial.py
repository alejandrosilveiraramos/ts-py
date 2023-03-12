# Generated by Django 4.1.7 on 2023-03-12 01:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('forma_pagamento', models.CharField(max_length=50)),
                ('data_pagamento', models.DateField()),
                ('status_pagamento', models.CharField(max_length=20)),
                ('solicitacao_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.solicitacao')),
            ],
            options={
                'db_table': 'pagamento',
            },
        ),
    ]
