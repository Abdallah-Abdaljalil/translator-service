from src.translator import translate_content
# from sentence_transformers import SentenceTransformer, util

# model = SentenceTransformer('all-MiniLM-L6-v2')

# def eval_single_response_complete(expected_answer: tuple[bool, str], llm_response: tuple[bool, str]) -> float:
#     expected_lang, expected_text = expected_answer
#     response_lang, response_text = llm_response
#     lang_score = 1.0 if expected_lang == response_lang else 0.0
#     expected_embedding = model.encode(expected_text, convert_to_tensor=True)
#     response_embedding = model.encode(response_text, convert_to_tensor=True)
#     similarity_score = util.cos_sim(expected_embedding, response_embedding).item()
#     combined_score = 0.5 * lang_score + 0.5 * similarity_score
#     assert combined_score >= 0.6

# def test_chinese():
#     eval_single_response_complete((False, "This is a message in Chinese"), translate_content("这是一条中文消息"))

# def test_llm_normal_response():
#     eval_single_response_complete((False, "Here is your first example."), translate_content("Hier ist dein erstes Beispiel."))

# def test_llm_gibberish_response():
#     eval_single_response_complete((False, "Unintelligible"), translate_content("sdgkl fdkg ldfkgj dflkgj"))
