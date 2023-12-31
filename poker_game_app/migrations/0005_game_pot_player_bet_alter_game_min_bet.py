# Generated by Django 5.0 on 2023-12-24 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poker_game_app', '0004_alter_player_card1_alter_player_card2'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='pot',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='bet',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='min_bet',
            field=models.IntegerField(default=0),
        ),
    ]
