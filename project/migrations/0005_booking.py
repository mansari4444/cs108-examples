# Generated by Django 2.2.7 on 2021-04-15 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_guide'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_booking', models.DateField(blank=True)),
                ('total_price', models.IntegerField()),
                ('boat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Boat')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Customer')),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Guide')),
            ],
        ),
    ]
