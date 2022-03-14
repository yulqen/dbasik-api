class Project:
    def __init__(self, name: str, project_id: int, project_type: str, budget: str):
        self.budget = budget
        self.type = project_type
        self.id = project_id
        self.name = name
