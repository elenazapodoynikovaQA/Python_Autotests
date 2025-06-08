import requests

BASE_URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "75b33d90cc58c03484ad6452cb2995ad"  
TRAINER_ID = "36182"  
HEADER = {
    "Content-Type": "application/json",
    "trainer_token": TOKEN
}

def test_get_trainers_status():
    """Проверить, что GET /trainers возвращает 200"""
    response = requests.get(f"{BASE_URL}/trainers")
    assert response.status_code == 200

def test_trainer_name_in_response():
    """Проверить, что имя вашего тренера есть в ответе /trainers"""
    params = {"trainer_id": TRAINER_ID}
    response = requests.get(f"{BASE_URL}/trainers", params=params)
    assert response.status_code == 200
    data = response.json()["data"]
    assert isinstance(data, list), "Ожидался список тренеров"
    assert len(data) > 0, "Список тренеров пуст"

    trainer_info = data[0]["trainer_name"]
    print("Имя из ответа сервера:", trainer_info)   # <-- Вот сюда!
    assert trainer_info == "Aya"  # или любое ваше актуальное имя



