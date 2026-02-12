const API_URL = "http://127.0.0.1:8000/chat";

export async function sendChatMessage(text) {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      
      message:text
    })
  });

  if (!response.ok) {
    throw new Error("API failed");
  }
  const data = await response.json();
  return data.reply;

  

 
}
