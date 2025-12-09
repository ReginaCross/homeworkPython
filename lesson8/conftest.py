import pytest
import os
from typing import Dict, Any


def pytest_configure(config):
    """Конфигурация pytest."""
    # Проверяем наличие необходимых переменных окружения
    required_vars = ['API_BASE_URL', 'API_TOKEN']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        raise pytest.UsageError(
            f"Не установлены переменные окружения: {', '.join(missing_vars)}. "
            f"Пожалуйста, установите их перед запуском тестов."
        )


@pytest.fixture(scope="session")
def api_config() -> Dict[str, str]:
    """Конфигурация API."""
    return {
        'base_url': os.getenv('API_BASE_URL'),
        'token': os.getenv('API_TOKEN'),
        'headers': {
            'Authorization': f'Bearer {os.getenv("API_TOKEN")}',
            'Content-Type': 'application/json'
        }
    }


@pytest.fixture
def test_project_data() -> Dict[str, Any]:
    """Данные для создания тестового проекта."""
    return {
        "name": f"Test Project {os.urandom(4).hex()}",
        "description": "Тестовый проект для автоматизированного тестирования",
        "is_active": True
    }


@pytest.fixture
def cleanup_project(api_config):
    """Фикстура для очистки созданных проектов после тестов."""
    created_projects = []
    
    yield created_projects
    
    # После выполнения тестов удаляем созданные проекты
    from api.projects_api import ProjectsAPI
    api = ProjectsAPI(api_config['base_url'], api_config['headers'])
    
    for project_id in created_projects:
        try:
            api.delete_project(project_id)
        except Exception:
            pass  # Игнорируем ошибки при удалении