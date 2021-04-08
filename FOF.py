import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# theFile = open("FOF.txt")
# print(str(theFile))
with open('process.json','r',encoding='utf-8') as f:
    data = json.load(f)
theDiv = data['div']
theOL = theDiv['ol']
theWriteWrongFile = open("process.txt", "a")

theListOfQuestions = theOL['li'];
questionJSONObjectList = []
counter = 0
for QuestionObject in theListOfQuestions:
    DIVobjectList = QuestionObject['div']
    questionJSONObject = {}
    for listItem in DIVobjectList:
        if 'class' in listItem.keys():
            if listItem['class'] == 'wpProQuiz_question':
                counter = counter +1
                theDiv = listItem['div']
                theP = theDiv['p']
                if type(theP) == list:
                    theP = theP[0]
                theSpan = theP['span']
                theText = theSpan['#text']
                questionJSONObject[str(counter)+':'] = theText[0]
                theUL = listItem['ul']
                theULList = theUL['li']
                answerObject = {}
                for AnswerItem in theULList:
    
                    theLabel = AnswerItem['label']
                    theSpan = theLabel['span']
                    theIndexLetter = theSpan['#text']
                    if 'wpProQuiz_answerCorrect' in AnswerItem['class']:
                        answerObject[theIndexLetter] = theLabel['#text']
                    if 'wpProQuiz_answerIncorrect' in AnswerItem['class']:
                        answerObject['X-->'+theIndexLetter] = theLabel['#text']
                questionJSONObject['Answers'] = answerObject
            if listItem['class'] == 'wpProQuiz_response':
                counter = 0
                theDiv = listItem['div']
                print(len(theDiv))
                

            
    questionJSONObjectList.append(questionJSONObject)                
            

# print(questionJSONObjectList)     
theWriteWrongFile.write(json.dumps(questionJSONObjectList, indent=0))
theWriteWrongFile.close()      



# print(data['div'])
# print(data['div'])
# tupleLength = len(data)
# for outer in data:
#     for counter in range(len(data)):
#         print(type(outer))
#         print(outer[counter])
# dictionary = json.loads(str(theFile))

# # parse x:
# data = json.dumps(str(theFile))
# print(type(data))

# for i in data['div']:
#     print(i)
  
# # Closing file
# theFile.close()