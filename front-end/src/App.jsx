import { useState } from "react";
import ChatWindow from "./components/ChatWindow/ChatWindow";
import ChatInput from "./components/ChatInput/ChatInput";
import { sendChatMessage } from "./services/chatApi";
import "./App.css";

function App() {
  const [messages, setMessages] = useState([]);

  const handleSend = async (text) => {
    setMessages(prev => [...prev, { sender: "user", text }]);

    try {
      const reply = await sendChatMessage(text);

      setMessages(prev => [
        ...prev,
        { sender: "bot", text: reply }
      ]);

    } catch {
      setMessages(prev => [
        ...prev,
        { sender: "bot", text: "❌ Backend error" }
      ]);
    }
  };

  return (
    <div className="app">
      <h2>🤖 FastAPI Chatbot</h2>
      <ChatWindow messages={messages} />
      <ChatInput onSend={handleSend} />
    </div>
  );
}

export default App;
