# Generated by Django 3.1.6 on 2021-02-04 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(max_length=200, verbose_name='Название на русском')),
                ('title_en',
                 models.CharField(blank=True, max_length=200, null=True, verbose_name='Название на английском')),
                ('title_jp',
                 models.CharField(blank=True, max_length=200, null=True, verbose_name='Название на японском')),
                ('image', models.ImageField(upload_to='', verbose_name='Картинка')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('previous_evolution',
                 models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                   to='pokemon_entities.pokemon', verbose_name='Предыдущая эволюция')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(verbose_name='Долгота')),
                ('lon', models.FloatField(verbose_name='Широта')),
                ('appeared_at', models.DateTimeField(blank=True, null=True, verbose_name='Время появления')),
                ('disappeared_at', models.DateTimeField(blank=True, null=True, verbose_name='Время пропажи')),
                ('level', models.IntegerField(blank=True, null=True, verbose_name='Уровень')),
                ('health', models.IntegerField(blank=True, null=True, verbose_name='Здоровье')),
                ('strength', models.IntegerField(blank=True, null=True, verbose_name='Атака')),
                ('defence', models.IntegerField(blank=True, null=True, verbose_name='Защита')),
                ('stamina', models.IntegerField(blank=True, null=True, verbose_name='Выносливость')),
                ('pokemon',
                 models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pokemon_entities.pokemon')),
            ],
        ),
    ]
