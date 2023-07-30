import openai
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write an email to my boss for resignation?",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)

'''
{
  "id": "cmpl-7g6IVVEmDcc7ABetntBJztUPh1aaZ",
  "object": "text_completion",
  "created": 1690268339,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "\n\nDear [Your Boss Name],\n\nI am writing to inform you that I am formally resigning from my current position at [Company Name]. I am grateful for the time I have spent here and for the opportunity to work with and learn from a great team.\n\nMy last day of work will be [date] as per my contract terms. I am happy to ensure a smooth transition for my replacement by helping to train and follow up with any inquiries they may have.\n\nAgain, I want to thank you for the time I have spent here and wish the company every success in the future.\n\nSincerely,\n[Your Name]",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 134,
    "total_tokens": 143
  }
}
'''