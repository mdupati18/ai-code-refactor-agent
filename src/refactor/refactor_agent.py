import openai
from utils.file_utils import read_file, write_file

class RefactorAgent:
    def __init__(self, model="gpt-4o-mini"):
        self.model = model

    def refactor(self, file_path):
        code = read_file(file_path)

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a code refactoring agent."},
                {"role": "user", "content": f"Refactor this code:\n\n{code}"}
            ]
        )

        improved_code = response["choices"][0]["message"]["content"]
        return improved_code
