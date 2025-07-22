import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_name', models.CharField(max_length=255)),
                ('profession', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Professional',
                'verbose_name_plural': 'Professionals',
                'db_table': 'professionals',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='api.professional')),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointments',
                'db_table': 'appointments',
            },
        ),
    ]
