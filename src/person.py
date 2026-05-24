class Person:
    def __init__(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str):
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        self._name = name

    def __str__(self):
        return f"Person: {self._name}"
