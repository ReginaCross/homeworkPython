from typing import Dict, Any, Optional
from .base_api import BaseAPI
from models.project import ProjectCreate, ProjectUpdate, ProjectResponse


class ProjectsAPI(BaseAPI):
    """Класс для работы с API проектов."""
    
    def create_project(self, project_data: Dict[str, Any]) -> ProjectResponse:
        """
        Создает новый проект.
        
        Args:
            project_data: Данные проекта
            
        Returns:
            ProjectResponse: Созданный проект
        """
        
        project_create = ProjectCreate(**project_data)
        
        response = self.post('/api-v2/projects', json=project_create.dict(exclude_none=True))
        return ProjectResponse(**response.json())
    
    def get_project(self, project_id: int) -> ProjectResponse:
        """
        Получает проект по ID.
        
        Args:
            project_id: ID проекта
            
        Returns:
            ProjectResponse: Найденный проект
        """
        response = self.get(f'/api-v2/projects/{project_id}')
        return ProjectResponse(**response.json())
    
    def update_project(self, project_id: int, update_data: Dict[str, Any]) -> ProjectResponse:
        """
        Обновляет проект.
        
        Args:
            project_id: ID проекта
            update_data: Данные для обновления
            
        Returns:
            ProjectResponse: Обновленный проект
        """
        
        project_update = ProjectUpdate(**update_data)
        
        response = self.put(f'/api-v2/projects/{project_id}', 
                           json=project_update.dict(exclude_none=True))
        return ProjectResponse(**response.json())
    
    def delete_project(self, project_id: int) -> bool:
        """
        Удаляет проект.
        
        Args:
            project_id: ID проекта
            
        Returns:
            bool: True если успешно удален
        """
        response = self.delete(f'/api-v2/projects/{project_id}')
        return response.status_code == 204