class Task:
    def __init__(self, id, title, description, status=False):
        self.id = id
        self.title = title
        self.description = description
        self.status = status

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status
        }
    
    def __repr__(self):
        return f"<Task {self.title} - Concluída: {self.status}>"