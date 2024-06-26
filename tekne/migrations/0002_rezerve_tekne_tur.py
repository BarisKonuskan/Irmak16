# Generated by Django 4.1 on 2024-06-03 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tekne", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="rezerve",
            fields=[
                ("rezerveid", models.AutoField(primary_key=True, serialize=False)),
                ("tarih", models.DateTimeField(blank=True, null=True)),
                ("tur", models.CharField(blank=True, max_length=50, null=True)),
                ("tekne", models.CharField(blank=True, max_length=50, null=True)),
                ("adet", models.IntegerField(blank=True, null=True)),
                ("ucret", models.IntegerField(blank=True, null=True)),
                ("toplamucret", models.IntegerField(blank=True, null=True)),
                ("kapora", models.IntegerField(blank=True, null=True)),
                ("telno", models.IntegerField(blank=True, null=True)),
                ("aciklama", models.CharField(blank=True, max_length=250, null=True)),
                ("tamucret", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="tekne",
            fields=[
                ("tekneid", models.AutoField(primary_key=True, serialize=False)),
                ("teknename", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="tur",
            fields=[
                ("turid", models.AutoField(primary_key=True, serialize=False)),
                ("turname", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
