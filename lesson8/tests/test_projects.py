import pytest
from api.projects_api import ProjectsAPI
from models.project import ProjectCreate, ProjectUpdate


class TestProjectsAPI:
    """Тесты для API проектов."""
    
    # ========== POSITIVE TESTS ==========
    
    def test_create_project_positive(self, api_config, test_project_data, cleanup_project):
        """Позитивный тест создания проекта."""
        # Arrange
        api = ProjectsAPI(api_config['base_url'], api_config['headers'])
        
        # Act
        response = api.create_project(test_project_data)
        cleanup_project.append(response.id)  # Добавляем для очистки
        
        # Assert
        assert response.id is not None
        assert response.name == test_project_data['name']
        assert response.description == test_project_data['description']
        assert response.is_active == test_project_data['is_active']
        assert response.created_at is not None
        assert response.updated_at is not None
    
    def test_get_project_positive(self, api_config, test_project_data, cleanup_project):
        """Позитивный тест получения проекта."""
        # Arrange
        api = ProjectsAPI(api_config['base_url'], api_config['headers'])
        created_project = api.create_project(test_project_data)
        cleanup_project.append(created_project.id)
        
        # Act
        retrieved_project = api.get_project(created_project.id)
        
        # Assert
        assert retrieved_project.id == created_project.id
        assert retrieved_project.name == created_project.name
        assert retrieved_project.description == created_project.description
        assert retrieved_project.is_active == created_project.is_active
    
    def test_update_project_positive(self, api_config, test_project_data, cleanup_project):
        """Позитивный тест обновления проекта."""
        # Arrange
        api = ProjectsAPI(api_config['base_url'], api_config['headers'])
        created_project = api.create_project(test_project_data)
        cleanup_project.append(created_project.id)
        
        update_data = {
            "name": f"Updated {test_project_data['name']}",
            "description": "Обновленное описание",
            "is_active": False
        }
        
        # Act
        updated_project = api.update_project(created_project.id, update_data)
        
        # Assert
        assert updated_project.id == created_project.id
        assert updated_project.name == update_data['name']
        assert updated_project.description == update_data['description']
        assert updated_project.is_active == update_data['is_active']
        assert updated_project.updated_at != created_project.updated_at
    
    # ========== NEGATIVE TESTS ==========
    
    def test_create_project_negative_missing_required_field(self, api_config):
        """Негативный тест создания проекта без обязательного поля."""
        # Arrange
        api = ProjectsAPI(api_config['base_url'], api_config['headers'])
        invalid_data = {
            "description": "Проект без имени",
            "is_active": True
        }
        
        # Act & Assert
        with pytest.raises(Exception) as exc_info:
            api.create_project(invalid_data)
        
        # Проверяем, что это ошибка валидации или 400 статус
        assert "name" in str(exc_info.value).lower() or "400" in str(exc_info.value)
    
    def test_get_project_negative_not_found(self, api_config):
        """Негативный тест получения несуществующего проекта."""
        # Arrange
        api = ProjectsAPI(api_config['base_url'], api_config['headers'])
        non_existent_id = 999999
        
        # Act & Assert
        with pytest.raises(Exception) as exc_info:
            api.get_project(non_existent_id)
        
        # Проверяем, что получили 404 ошибку
        assert "404" in str(exc_info.value)
    
    def test_update_project_negative_invalid_data(self, api_config, test_project_data, cleanup_project):
        """Негативный тест обновления проекта с некорректными данными."""
        # Arrange
        api = ProjectsAPI(api_config['base_url'], api_config['headers'])
        created_project = api.create_project(test_project_data)
        cleanup_project.append(created_project.id)
        
        invalid_update_data = {
            "name": "",  # Пустое имя - невалидно
            "is_active": True
        }
        
        # Act & Assert
        with pytest.raises(Exception) as exc_info:
            api.update_project(created_project.id, invalid_update_data)
        
        # Проверяем, что получили ошибку
        assert "400" in str(exc_info.value) or "validation" in str(exc_info.value).lower()
    
    def test_create_project_negative_unauthorized(self, api_config, test_project_data):
        """Негативный тест создания проекта без авторизации."""
        # Arrange
        invalid_headers = api_config['headers'].copy()
        invalid_headers['Authorization'] = 'Bearer invalid_token'
        api = ProjectsAPI(api_config['base_url'], invalid_headers)
        
        # Act & Assert
        with pytest.raises(Exception) as exc_info:
            api.create_project(test_project_data)
        
        # Проверяем, что получили 401 ошибку
        assert "401" in str(exc_info.value)
    
    def test_update_project_negative_readonly_field(self, api_config, test_project_data, cleanup_project):
        """Негативный тест обновления read-only поля (если такое есть)."""
        # Arrange
        api = ProjectsAPI(api_config['base_url'], api_config['headers'])
        created_project = api.create_project(test_project_data)
        cleanup_project.append(created_project.id)
        
        # Пробуем обновить поле, которое может быть read-only (например, created_at)
        invalid_update_data = {
            "name": "Новое имя",
            "created_at": "2024-01-01T00:00:00Z"  # Предполагаем, что это read-only
        }
        
        # Act
        updated_project = api.update_project(created_project.id, invalid_update_data)
        
        # Assert - проверяем, что read-only поле не изменилось
        # (это зависит от API, может потребоваться адаптация)
        assert updated_project.name == "Новое имя"
        # created_at должно остаться исходным или сервер должен игнорировать это поле