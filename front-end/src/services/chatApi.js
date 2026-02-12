const BASE_URL = "http://127.0.0.1:8000";


// -------------------------
// Session (auto once)
// -------------------------
function getSessionId() {
  let id = localStorage.getItem("session_id");

  if (!id) {
    id = crypto.randomUUID();
    localStorage.setItem("session_id", id);
  }

  return id;
}


// -------------------------
// Chat instance (auto once)
// -------------------------
async function getChatId() {
  let chatId = localStorage.getItem("chat_id");

  if (chatId) return chatId;

  const res = await fetch(`${BASE_URL}/chat/create`, {
    method: "POST",
    headers: {
      "session-id": getSessionId()
    }
  });

  const data = await res.json();

  chatId = data.chat_id;
  localStorage.setItem("chat_id", chatId);

  return chatId;
}


// -------------------------
// YOUR MAIN FUNCTION (modified)
// -------------------------
export async function sendChatMessage(text) {
  const chatId = await getChatId();

  const response = await fetch(`${BASE_URL}/chat/${chatId}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "session-id": getSessionId()
    },
    body: JSON.stringify({
      message: text
    })
  });

  if (!response.ok) {
    throw new Error("API failed");
  }

  const data = await response.json();

  return data.response;   // matches FastAPI
}
