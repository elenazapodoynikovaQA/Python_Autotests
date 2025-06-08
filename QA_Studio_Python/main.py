import requests

BASE_URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "75b33d90cc58c03484ad6452cb2995ad"
HEADER = {
    "Content-Type": "application/json",
    "trainer_token": TOKEN
}

# 1. Создание покемона (POST /pokemons)
create_pokemon_body = {
    "name": "PikachuQA",
    "photo_id": 1   # Например, 1 — это стандартная картинка (можно 2, 3 и т.д.)
}


response_create = requests.post(
    url=f"{BASE_URL}/pokemons",
    headers=HEADER,
    json=create_pokemon_body
)
print("Создание покемона:", response_create.text)

# Получаем id созданного покемона для следующего шага
pokemon_id = response_create.json().get('id')

# 2. Смена имени покемона (PUT /pokemons)
if pokemon_id:
    update_pokemon_body = {
        "pokemon_id": pokemon_id,
        "name": "RaichuQA",
        "photo_id": 2     # Обязательное поле (выберите любой id, напр. 2)
    }
    response_update = requests.put(
        url=f"{BASE_URL}/pokemons",
        headers=HEADER,
        json=update_pokemon_body
    )
    print("Смена имени покемона:", response_update.text)
else:
    print("Ошибка: не удалось получить id покемона.")


# 3. Поймать покемона в покебол (POST /trainers/add_pokeball)
if pokemon_id:
    add_pokeball_body = {
        "pokemon_id": pokemon_id
    }
    response_pokeball = requests.post(
        url=f"{BASE_URL}/trainers/add_pokeball",
        headers=HEADER,
        json=add_pokeball_body
    )
    print("Поймать покемона в покебол:", response_pokeball.text)
else:
    print("Ошибка: не удалось поймать покемона в покебол (нет id).")
