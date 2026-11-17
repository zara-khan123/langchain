
#CodeBloomAPP LangChain Basics (Different Approach)

#This is NOT an AI Agent.
#It is a simple LangChain pipeline (LCEL) that:
#1. Explains any concept in simple words
#2. Gives 4-5 key points
#3. Creates 3 practice quiz questions with answers

#Perfect for students who want to revise topics.

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StroutputParser
from langchain_core.runnables import RunnablePassthrough

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

#Step 1: Explain the concept simply

explain_prompt = ChatPromptTemplate.from_template(
	"""You are a friendly teacher for coding students.

Explain the following concept in very simple language
(as if teaching a 1st-year student):

Concept: {topic}

Keep the explanation under 120 words and use everyday examples."""
)


#Step 2: Extract key points

keypoints_prompt = Chat PromptTemplate.from template( 
	"""From this explanation, extract 4-5 clear key points. 
Write them as a bullet list.

Explanation:
{explanation}
"""
)

#Step 3: Generate quiz questions

quiz_prompt = ChatPromptTemplate.from_template(
	"""Based on this explanation, create 3 short practice questions for a student. 
	Also give the correct answer for each.

Format exactly like this:

Q1:
Answer: ...

Q2: ...
Answer: ...

Q3: ...
Answer: ...

Explanation:
{explanation}
"""

#Build the pipeline (Lcel - langchain expression language)

explain_chain = explain_prompt | llm | StroutputParser()
keypoints_chain = keypoints_prompt | llm | StrOutputParser()
quiz_chain = quiz_prompt llm | StrOutputParser()

#Full pipeline: topic explanation key points quiz
full chain = (
	{"topic": RunnablePassthrough()}
	| RunnablePassthrough.assign(explanation=explain_chain)
	| RunnablePassthrough.assign(
		keypoints=Lambda x: keypoints_chain.invoke({"explanation": x["explanation"]}),
		quiz=lambda x: quiz_chain.invoke({"explanation": x["explanation"]})


)
)

#run it

def study_buddy(topic: str):
	print("\n" + "="*65) 
	print(f" Studying: {topic}")
	print("="*65)

	result = full_chain.invoke(topic)

	print("\n SIMPLE EXPLANATION:")
	print(result["explanation"])

	print("\n KEY POINTS:") 
	print(result["keypoints"])

	print("\n PRACTICE QUIZ:")
	print(result["quiz"])
	print("\n" + "-"*65)




if __name__ == "__main__":

	print("codebloom")

	examples = [
	"What is an AI Agent?",
	"ReAct pattern",
	"Difference between LLM and AI Agent",
	"LangChain tools",
	"Short-term vs Long-term memory in agents",

	]

	print("Try these topics (or type your own):\n")
	for i, ex in enumerate(examples, 1):
		print(f" {1}. {ex}")

	print("\nType 'quit' to exit\n")

	while True:
		topic = input("Topic you want to study").strip()
		if topic.lower() in ["quit", "exit", "q"]:
			print("Happy studying!")
			break
		if topic:
			study_buddy(topic)
			