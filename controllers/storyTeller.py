from openai import OpenAI
from dotenv import load_dotenv
import os
from services.modelUtil import ModelUtil
load_dotenv()

class StoryTeller:
    MAX_TOKENS = 4000
    def __init__ (self):
        instructions = f"You are a story teller. Your job is to generate a short story. This story need to be coherent from start to finish. The main charater is a time-traveling detective with a distinct personality, skills, and a compelling reason for utilizing time travel in solving mysteries. Develop a complex plot and intriguing mystery, taking advatage of temporal aspects.Create a vivid setting that seamlessly intergrates different time periods, adding depth and richness to the narrative. The story most have a clear beginning middle and end, with a resolution to the mystery that is satisfying and unexpected"
        self.context = [{"role": "system", "content":instructions}]
        self.client = OpenAI(api_key=os.getenv("myGptkey"))
        self.storyNumber = StoryTeller.calculateNextStoryIndex()
        
        
    def generateStory(self):
        story = ModelUtil.makeAPICallStory(self)
        print(story)
        self.validateStory(story)
        
    def validateStory(self,story):
        self.context = [{"role":"system", "content" : f"You are a college English teacher. You need to grade this story on **coherentness**, **plot complexity**, and ensure the story has a **start, middle, and end**. There should be a score from 0 - 100  for the **coherency_score** and **plot_complexity_score. For **has_start_middle_end** this should either be `True` for `False`. The **overall_score** is the average between the three. For the **has_start_middle_end** True should be evaluated to 100 and false evaluated to 0. Here is the story: {story}" }]
        results = ModelUtil.makeAPICallStoryValidation(self,story)
        print("*"*100,"\n", results)
        
    @staticmethod
    def calculateNextStoryIndex():
        folder_path = './stories'
        os.makedirs(folder_path, exist_ok=True)
        files = os.listdir(folder_path)
        return len(files)