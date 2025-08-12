import os
import openai

# Create the client using your API key
client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def classify_with_openai(email_address):
    prompt = f"""
You are an AI email security assistant. Given the email address below, determine if it looks like a spam sender or a genuine one. Return only one word: "Spam" or "Genuine".

Email: {email_address}
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an email spam classifier."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()

# Example usage
if __name__ == "__main__":
    email = input("Enter an email address to classify: ")
    result = classify_with_openai(email)
    print(f"\nResult ➜ {result}")
