from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField('Название на русском', max_length=200)
    title_en = models.CharField('Название на английском', max_length=200, blank=True)
    title_jp = models.CharField('Название на японском', max_length=200, blank=True)
    image = models.ImageField('Картинка', blank=True)
    description = models.TextField('Описание', blank=True)
    previous_evolution = models.ForeignKey('Pokemon', related_name='next', on_delete=models.PROTECT, blank=True,
                                           null=True,
                                           verbose_name='Предыдущая эволюция')

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, related_name='pokemonsentities', on_delete=models.CASCADE)
    lat = models.FloatField('Долгота')
    lon = models.FloatField('Широта')
    appeared_at = models.DateTimeField('Время появления', null=True, blank=True)
    disappeared_at = models.DateTimeField('Время пропажи', null=True, blank=True)
    level = models.IntegerField('Уровень', null=True, blank=True)
    health = models.IntegerField('Здоровье', null=True, blank=True)
    strength = models.IntegerField('Атака', null=True, blank=True)
    defence = models.IntegerField('Защита', null=True, blank=True)
    stamina = models.IntegerField('Выносливость', null=True, blank=True)
