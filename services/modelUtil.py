from models.MCQModel import MCQModel
from models.Story import Story
from services.jsonUtil import JsonUtil
class ModelUtil:
    @staticmethod
    def makeAPICallQuestion(model, questionNumber):
        completion = model.client.beta.chat.completions.parse(
            messages = model.context,
            model="gpt-4o-mini",
            response_format = MCQModel
        )
        print("*"*80,type(completion.choices[0].message.parsed))
        jsonModel = completion.choices[0].message.parsed
        jsonModel.questionNumber = questionNumber
        model.context.append({"role" : "system", "content": f"You have {(questionNumber+1)-10} left to do. Do not to use this question again: {jsonModel.question}"})
        JsonUtil.saveModelToJsonQuestion(jsonModel,model.questionsIndex)
        return model
    
    @staticmethod
    def makeAPICallStory(model):
        completion = model.client.chat.completions.create(
            model="gpt-4o-mini",
            messages = model.context
        )
        return completion.choices[0].message.content
    
    @staticmethod
    def makeAPICallStoryValidation(model,story):
        completion = model.client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages = model.context,
            response_format = Story
        )
        print("*"*80,type(completion.choices[0].message.parsed))
        jsonModel = completion.choices[0].message.parsed
        jsonModel.story_number = model.storyNumber
        jsonModel.story_content = story
        JsonUtil.saveModelToJsonStory(jsonModel)
        return model
    
