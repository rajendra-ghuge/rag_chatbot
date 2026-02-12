import "./ChatWindow.css";
import ReactMarkdown from "react-markdown";
import { useEffect, useRef } from "react";

function ChatWindow({ messages }) {
  const bottomRef = useRef(null);

  // auto-scroll when new message arrives
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <div className="chat-window">
      {messages.map((msg, i) => (
        <div key={i} className={`message ${msg.sender}`}>
          <ReactMarkdown>{msg.text}</ReactMarkdown>
        </div>
      ))}

      {/* invisible anchor */}
      <div ref={bottomRef} />
    </div>
  );
}

export default ChatWindow;
