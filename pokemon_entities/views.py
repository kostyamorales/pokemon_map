import folium
from django.shortcuts import render
from pokemon_entities.models import Pokemon, PokemonEntity
import logging

logger = logging.getLogger()
MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # tooltip=name,  # disable tooltip because of folium encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        for pokemon_entity in PokemonEntity.objects.filter(pokemon=pokemon):
            add_pokemon(
                folium_map, pokemon_entity.lat, pokemon_entity.lon, pokemon.image.path)

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemon_on_page = {
            'pokemon_id': pokemon.id,
            'title_ru': pokemon.title_ru,
        }
        try:
            pokemon_on_page['img_url'] = pokemon.image.url
        except ValueError as error:
            logger.info(error)
        pokemons_on_page.append(pokemon_on_page)

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    requested_pokemon = Pokemon.objects.get(id=pokemon_id)
    pokemon = {
        'title_ru': requested_pokemon.title_ru,
        'title_en': requested_pokemon.title_en,
        'title_jp': requested_pokemon.title_jp,
        'description': requested_pokemon.description,
        'previous_evolution': requested_pokemon.previous_evolution,
    }
    try:
        pokemon['img_url'] = requested_pokemon.image.url
    except ValueError as error:
        logger.info(error)
    try:
        pokemon['next_evolution'] = requested_pokemon.pokemon_set.get()
    except Pokemon.DoesNotExist as error:
        logger.info(error)

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in PokemonEntity.objects.filter(pokemon=requested_pokemon):
        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.lon, requested_pokemon.image.path)

    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon})
