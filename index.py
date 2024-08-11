from controllers.questionGeneration import QuestionGeneration
from controllers.storyTeller import StoryTeller
print("You want python coding questions?, or a compeling time traveling detective story? \n a)questions \n b)story")

path = input()

if path == "a":
    print("You have picked coding questions type in your desired difficulty.")
    difficulty = input()
    qg = QuestionGeneration(difficulty)
    try:
        qg.generate10Questions()
        print("Your questions have been generated.")
    except:
        print("somthing went wrong")
else:
    st = StoryTeller()
    st.generateStory()

