from pathlib import Path
import json
from models import MCQModel,Story
class JsonUtil:
    @staticmethod
    def saveModelToJsonQuestion(model: MCQModel, questionIndex:int):
        model_json = model.model_dump_json()
        
        folder_path = Path('../data/json/questions')
        file_path = folder_path/f"questions{questionIndex}.json"
        if not file_path.exists() or file_path.stat().st_size == 0:
            data = []
        else:
            with open(file_path, 'r') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
        data.append(json.loads(model_json))
        
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            print(f'updated {file_path}')
            
    @staticmethod
    def saveModelToJsonStory(model: Story):
        model_json = model.model_dump_json()
        folder_path = Path('../data/json/stories')
        file_path = folder_path/f"story{model.story_number}.json"
        if not file_path.exists() or file_path.stat().st_size == 0:
            data = []
        else:
            with open(file_path, 'r') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
        data.append(json.loads(model_json))
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            print(f'updated {file_path}')