# Generated by Django 2.2.1 on 2019-06-17 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricscore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveries',
            name='batsman',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='deliveries',
            name='batting_team',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='deliveries',
            name='bowler',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='deliveries',
            name='bowling_team',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='deliveries',
            name='dismissal_kind',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='deliveries',
            name='fielder',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='deliveries',
            name='non_striker',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='deliveries',
            name='player_dismissed',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='matches',
            name='city',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='matches',
            name='dl_winners',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='matches',
            name='player_of_match',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='matches',
            name='result',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='matches',
            name='team1',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='matches',
            name='team2',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='matches',
            name='toss_desicion',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='matches',
            name='toss_won',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='matches',
            name='umpire1',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='matches',
            name='umpire2',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='matches',
            name='umpire3',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='matches',
            name='venue',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='matches',
            name='winners',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
