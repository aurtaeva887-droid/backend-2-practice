from fastapi import FastAPI, HTTPException

app = FastAPI()

# --- Имитация базы данных ---
categories_db = [
    {"id": 1, "name": "Стрижки и укладки"},
    {"id": 2, "name": "Маникюр и педикюр"},
    {"id": 3, "name": "Брови и ресницы"},
    {"id": 4, "name": "Спа-процедуры"},
]

services_db = [
    # Услуги для категории 1 (5 штук)
    {"id": 1, "category_id": 1},
    {"id": 2, "category_id": 1},
    {"id": 3, "category_id": 1},
    {"id": 4, "category_id": 1},
    {"id": 5, "category_id": 1},
    # Услуги для категории 2 (2 штуки для примера)
    {"id": 6, "category_id": 2},
    {"id": 7, "category_id": 2},
    # Услуги для категории 3 (1 штука)
    {"id": 8, "category_id": 3},
    # Услуги для категории 4 (0 штук, проверим, что вернет 0)
]

# --- Задание 1: Список категорий ---
@app.get("/categories")
def get_categories():
    result = []
    for category in categories_db:
        # Считаем количество услуг для этой категории
        count = len([s for s in services_db if s["category_id"] == category["id"]])
        
        result.append({
            "id": category["id"],
            "name": category["name"],
            "servicesCount": count
        })
    return result

# --- Задание 2: Информация по категории ---
@app.get("/categories/{category_id}")
def get_category(category_id: int):
    # Ищем категорию по ID
    category = next((c for c in categories_db if c["id"] == category_id), None)
    
    if category is None:
        # Если не нашли, возвращаем ошибку 404 с нужным текстом
        raise HTTPException(status_code=404, detail="Сategory not found")
    
    # Считаем количество услуг
    count = len([s for s in services_db if s["category_id"] == category["id"]])
    
    return {
        "id": category["id"],
        "name": category["name"],
        "servicesCount": count
    }