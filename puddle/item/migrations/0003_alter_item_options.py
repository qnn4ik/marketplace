# Generated by Django 4.2.3 on 2023-10-07 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('name',)},
        ),
    ]
