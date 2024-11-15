import openai
from sentence_transformers import SentenceTransformer, util
import time
from openai.error import OpenAIError, RateLimitError

model = SentenceTransformer('all-MiniLM-L6-v2')
openai.api_key = "9bcZIi7ZRlZF9qvCb00ETujiDr8kpGq3fACo36yEm5xc5Envydj3JQQJ99AJACHrzpqXJ3w3AAABACOGCKto"
openai.api_base = "https://kwarraic-openai-resource.openai.azure.com/"
openai.api_type = "azure"
openai.api_version = "2024-08-01-preview"
deployment_name = "khadija-gpt4-deployment"

def get_language(post: str) -> str:
    context = "Identify if the following text's language is in 'English','nonenglish', or 'unintelligible'" # TODO: Insert context
    # ---------------- YOUR CODE HERE ---------------- #
    response = openai.ChatCompletion.create(
        engine=deployment_name,
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": post}
        ]
    )

    classification = response.choices[0].message.content
    return classification

def get_translation(post: str) -> str:
    context = "Translate the following text into English." # TODO: Insert context
    # ---------------- YOUR CODE HERE ---------------- #https://oli.cmu.edu/jcourse/workbook/activity/page?context=857b38290a0001dc2ae475a176bb17ba
    response = openai.ChatCompletion.create(
        engine=deployment_name,
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": post}
        ]
    )

    translated_text = response.choices[0].message.content
    return translated_text


def translate_content(content: str) -> tuple[bool, str]:
    try:  
        time.sleep(60)
        language = get_language(post)

        if isinstance(language, str) and language.isalpha():
            if language.lower().strip() == "english":
              return (True, "Already English")

            if language.lower().strip() == "nonenglish":
              time.sleep(60)
              translation = get_translation(post)
              time.sleep(60)
              return (False, translation)

            if language.lower().strip() == "unintelligible":
              return (False, "Unintelligible")

        return (False, "Unavailable")

  except Exception as e:
      return (False, "Error")

