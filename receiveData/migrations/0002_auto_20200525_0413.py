# Generated by Django 3.0.5 on 2020-05-25 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receiveData', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrickwoodStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('basically_intact_square', models.CharField(max_length=6)),
                ('damaged_square', models.CharField(max_length=6)),
                ('destroyed_square', models.CharField(max_length=6)),
                ('note', models.CharField(max_length=200)),
                ('reporting_unit', models.TextField(max_length=20)),
            ],
            options={
                'db_table': 'BrickwoodStructure',
            },
        ),
        migrations.CreateModel(
            name='CommDisaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='', max_length=20)),
                ('location', models.CharField(default='', max_length=100)),
                ('type', models.CharField(default='', max_length=4)),
                ('grade', models.CharField(default='', max_length=4)),
                ('picture', models.ImageField(default='', upload_to='')),
                ('note', models.TextField(default='', max_length=200)),
                ('reporting_unit', models.TextField(default='202', max_length=50)),
            ],
            options={
                'db_table': 'CommDisaster',
            },
        ),
        migrations.CreateModel(
            name='CrackRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='', max_length=20)),
                ('location', models.CharField(default='', max_length=100)),
                ('type', models.CharField(default='', max_length=10)),
                ('status', models.CharField(default='', max_length=10)),
                ('picture', models.ImageField(default='', upload_to='')),
                ('note', models.TextField(default='', max_length=200)),
                ('reporting_unit', models.TextField(default='202', max_length=50)),
            ],
            options={
                'db_table': 'CrackRecord',
            },
        ),
        migrations.CreateModel(
            name='DebrisRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='', max_length=20)),
                ('location', models.CharField(default='', max_length=100)),
                ('type', models.CharField(default='', max_length=10)),
                ('status', models.CharField(default='', max_length=10)),
                ('picture', models.ImageField(default='', upload_to='')),
                ('note', models.TextField(default='', max_length=200)),
                ('reporting_unit', models.TextField(default='202', max_length=50)),
            ],
            options={
                'db_table': 'DebrisRecord',
            },
        ),
        migrations.CreateModel(
            name='DisasterInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='', max_length=20)),
                ('location', models.CharField(default='', max_length=100)),
                ('longitude', models.FloatField(default='', max_length=100)),
                ('latitude', models.FloatField(default='', max_length=100)),
                ('depth', models.FloatField(default='')),
                ('magnitude', models.FloatField(default='')),
                ('picture', models.ImageField(default='', upload_to='')),
                ('reporting_unit', models.TextField(default='', max_length=50)),
            ],
            options={
                'db_table': 'DisasterInfo',
            },
        ),
        migrations.CreateModel(
            name='FrameworkStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('basically_intact_square', models.CharField(max_length=6)),
                ('slight_damaged_square', models.CharField(max_length=6)),
                ('moderate_damaged_square', models.CharField(max_length=6)),
                ('serious_damaged_square', models.CharField(max_length=6)),
                ('destroyed_square', models.CharField(max_length=6)),
                ('note', models.CharField(max_length=200)),
                ('reporting_unit', models.TextField(max_length=20)),
            ],
            options={
                'db_table': 'FrameworkStructure',
            },
        ),
        migrations.CreateModel(
            name='GasDisaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='', max_length=20)),
                ('location', models.CharField(default='', max_length=100)),
                ('type', models.CharField(default='', max_length=4)),
                ('grade', models.CharField(default='', max_length=4)),
                ('picture', models.ImageField(default='', upload_to='')),
                ('note', models.TextField(default='', max_length=200)),
                ('reporting_unit', models.TextField(default='202', max_length=50)),
            ],
            options={
                'db_table': 'GasDisaster',
            },
        ),
        migrations.CreateModel(
            name='InjuredStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('reporting_unit', models.TextField(max_length=20)),
            ],
            options={
                'db_table': 'InjuredStatistics',
            },
        ),
        migrations.CreateModel(
            name='IrrigationDisaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='', max_length=20)),
                ('location', models.CharField(default='', max_length=100)),
                ('type', models.CharField(default='', max_length=4)),
                ('grade', models.CharField(default='', max_length=4)),
                ('picture', models.ImageField(default='', upload_to='')),
                ('note', models.TextField(default='', max_length=200)),
                ('reporting_unit', models.TextField(default='202', max_length=50)),
            ],
            options={
                'db_table': 'IrrigationDisaster',
            },
        ),
        migrations.CreateModel(
            name='KarstRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='', max_length=20)),
                ('location', models.CharField(default='', max_length=100)),
                ('type', models.CharField(default='', max_length=10)),
                ('status', models.CharField(default='', max_length=10)),
                ('picture', models.ImageField(default='', upload_to='')),
                ('note', models.TextField(default='', max_length=200)),
                ('reporting_unit', models.TextField(default='202', max_length=50)),
            ],
            options={
                'db_table': 'KarstRecord',
            },
        ),
        migrations.CreateModel(
            name='LandslideRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='', max_length=20)),
                ('location', models.CharField(default='', max_length=100)),
                ('type', models.CharField(default='', max_length=10)),
                ('status', models.CharField(default='', max_length=10)),
                ('picture', models.ImageField(default='', upload_to='')),
                ('note', models.TextField(default='', max_length=200)),
                ('reporting_unit', models.TextField(default='202', max_length=50)),
            ],
            options={
                'db_table': 'LandslideRecord',
            },
        ),
        migrations.CreateModel(
            name='MasonryStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('basically_intact_square', models.CharField(max_length=6)),
                ('slight_damaged_square', models.CharField(max_length=6)),
                ('moderate_damaged_square', models.CharField(max_length=6)),
                ('serious_damaged_square', models.CharField(max_length=6)),
                ('destroyed_square', models.CharField(max_length=6)),
                ('note', models.CharField(max_length=200)),
                ('reporting_unit', models.TextField(max_length=20)),
            ],
            options={
                'db_table': 'MasonryStructure',
            },
        ),
        migrations.CreateModel(
            name='MissingStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('reporting_unit', models.TextField(max_length=20)),
            ],
            options={
                'db_table': 'MissingStatistics',
            },
        ),
        migrations.CreateModel(
            name='OilDisaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='', max_length=20)),
                ('location', models.CharField(default='', max_length=100)),
                ('type', models.CharField(default='', max_length=4)),
                ('grade', models.CharField(default='', max_length=4)),
                ('picture', models.ImageField(default='', upload_to='')),
                ('note', models.TextField(default='', max_length=200)),
                ('reporting_unit', models.TextField(default='202', max_length=50)),
            ],
            options={
                'db_table': 'OilDisaster',
            },
        ),
        migrations.CreateModel(
            name='OtherRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='', max_length=20)),
                ('location', models.CharField(default='', max_length=100)),
                ('type', models.CharField(default='', max_length=10)),
                ('picture', models.ImageField(default='', upload_to='')),
                ('note', models.TextField(default='', max_length=200)),
                ('reporting_unit', models.TextField(default='202', max_length=50)),
            ],
            options={
                'db_table': 'OtherRecord',
            },
        ),
        migrations.CreateModel(
            name='OtherStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('basically_intact_square', models.CharField(max_length=6)),
                ('slight_damaged_square', models.CharField(max_length=6)),
                ('moderate_damaged_square', models.CharField(max_length=6)),
                ('serious_damaged_square', models.CharField(max_length=6)),
                ('destroyed_square', models.CharField(max_length=6)),
                ('note', models.CharField(max_length=200)),
                ('reporting_unit', models.TextField(max_length=20)),
            ],
            options={
                'db_table': 'OtherStructure',
            },
        ),
        migrations.CreateModel(
            name='PowerDisaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='', max_length=20)),
                ('location', models.CharField(default='', max_length=100)),
                ('type', models.CharField(default='', max_length=4)),
                ('grade', models.CharField(default='', max_length=4)),
                ('picture', models.ImageField(default='', upload_to='')),
                ('note', models.TextField(default='', max_length=200)),
                ('reporting_unit', models.TextField(default='202', max_length=50)),
            ],
            options={
                'db_table': 'PowerDisaster',
            },
        ),
        migrations.CreateModel(
            name='SettlementRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='', max_length=20)),
                ('location', models.CharField(default='', max_length=100)),
                ('type', models.CharField(default='', max_length=10)),
                ('status', models.CharField(default='', max_length=10)),
                ('picture', models.ImageField(default='', upload_to='')),
                ('note', models.TextField(default='', max_length=200)),
                ('reporting_unit', models.TextField(default='202', max_length=50)),
            ],
            options={
                'db_table': 'SettlementRecord',
            },
        ),
        migrations.CreateModel(
            name='TrafficDisaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='', max_length=20)),
                ('location', models.CharField(default='', max_length=100)),
                ('type', models.CharField(default='', max_length=4)),
                ('grade', models.CharField(default='', max_length=4)),
                ('picture', models.ImageField(default='', upload_to='')),
                ('note', models.TextField(default='', max_length=200)),
                ('reporting_unit', models.TextField(default='202', max_length=50)),
            ],
            options={
                'db_table': 'TrafficDisaster',
            },
        ),
        migrations.CreateModel(
            name='WaterDisaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='', max_length=20)),
                ('location', models.CharField(default='', max_length=100)),
                ('type', models.CharField(default='', max_length=4)),
                ('grade', models.CharField(default='', max_length=4)),
                ('picture', models.ImageField(default='', upload_to='')),
                ('note', models.TextField(default='', max_length=200)),
                ('reporting_unit', models.TextField(default='202', max_length=50)),
            ],
            options={
                'db_table': 'WaterDisaster',
            },
        ),
        migrations.AddField(
            model_name='totaldata',
            name='MSCode',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='civilstructure',
            name='date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='collapserecord',
            name='date',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='deathstatistics',
            name='date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='disasterprediction',
            name='date',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='disasterrequest',
            name='date',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.DeleteModel(
            name='CommDissaster',
        ),
        migrations.AddField(
            model_name='waterdisaster',
            name='ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='receiveData.TotalData'),
        ),
        migrations.AddField(
            model_name='trafficdisaster',
            name='ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='receiveData.TotalData'),
        ),
        migrations.AddField(
            model_name='settlementrecord',
            name='ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='receiveData.TotalData'),
        ),
        migrations.AddField(
            model_name='powerdisaster',
            name='ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='receiveData.TotalData'),
        ),
        migrations.AddField(
            model_name='otherstructure',
            name='ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='receiveData.TotalData'),
        ),
        migrations.AddField(
            model_name='otherrecord',
            name='ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='receiveData.TotalData'),
        ),
        migrations.AddField(
            model_name='oildisaster',
            name='ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='receiveData.TotalData'),
        ),
        migrations.AddField(
            model_name='missingstatistics',
            name='ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='receiveData.TotalData'),
        ),
        migrations.AddField(
            model_name='masonrystructure',
            name='ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='receiveData.TotalData'),
        ),
        migrations.AddField(
            model_name='landsliderecord',
            name='ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='receiveData.TotalData'),
        ),
        migrations.AddField(
            model_name='karstrecord',
            name='ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='receiveData.TotalData'),
        ),
        migrations.AddField(
            model_name='irrigationdisaster',
            name='ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='receiveData.TotalData'),
        ),
        migrations.AddField(
            model_name='injuredstatistics',
            name='ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='receiveData.TotalData'),
        ),
        migrations.AddField(
            model_name='gasdisaster',
            name='ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='receiveData.TotalData'),
        ),
        migrations.AddField(
            model_name='frameworkstructure',
            name='ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='receiveData.TotalData'),
        ),
        migrations.AddField(
            model_name='disasterinfo',
            name='ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='receiveData.TotalData'),
        ),
        migrations.AddField(
            model_name='debrisrecord',
            name='ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='receiveData.TotalData'),
        ),
        migrations.AddField(
            model_name='crackrecord',
            name='ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='receiveData.TotalData'),
        ),
        migrations.AddField(
            model_name='commdisaster',
            name='ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='receiveData.TotalData'),
        ),
        migrations.AddField(
            model_name='brickwoodstructure',
            name='ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='receiveData.TotalData'),
        ),
    ]