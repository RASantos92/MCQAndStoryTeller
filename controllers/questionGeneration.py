from openai import OpenAI
from dotenv import load_dotenv
import os
from services.modelUtil import ModelUtil
load_dotenv()

class QuestionGeneration:
    MAX_TOKENS = 4000
    
    def __init__ (self,difficulty):
        self.difficutly = difficulty
        instructions = f"You are to generate and provide 10 multiple choice questions based around 'Programming Fundamentals using Python`. These 10 questions should be {difficulty} level questions. Each question should follow this strict formating: - **Question number** for each question header. - Display the **complexity level**. - **Scenario** that explain the real-time situation. - **Question** should be question based on the senario. - **Options** should always be labeled with a number from 1-4. - **Explanation** for the answer - **Answer** Should always start with the correct number option following the answer. Another important note is never repeat the same question. Always double check to make sure you have not generated the same question."
        self.context = [{"role": "system", "content":instructions}]
        self.client = OpenAI(api_key=os.getenv("myGptkey"))
        self.questionsIndex = QuestionGeneration.calculateNextQuestionIndex()
        
        
    def generate10Questions(self):
        for i in range(11):
            print(ModelUtil.makeAPICall(self,i))

    @staticmethod
    def calculateNextQuestionIndex():
        folder_path = './questions'
        os.makedirs(folder_path, exist_ok=True)
        files = os.listdir(folder_path)
        return len(files)