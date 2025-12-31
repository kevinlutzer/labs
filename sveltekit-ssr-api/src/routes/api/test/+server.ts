import { OPENAPI_KEY } from "$env/static/private";
import { json } from '@sveltejs/kit';
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: OPENAPI_KEY
});

export async function GET() {
  try {
    const response = await client.responses.create({
        model: "gpt-5-nano",
        input: "Write a one-sentence bedtime story about a unicorn."
    });
    return json({
      message: response.output_text
    });
  } catch (error) { 
    console.error("Error creating response:", error);
    return json({
      message: "An error occurred while generating the story."
    });
  }

  
} 