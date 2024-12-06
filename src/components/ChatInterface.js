// // ChatInterface.js
// import React, { useState, useRef, useEffect } from "react";
// import { useChat } from "../context/ChatContext";
// import { sendMessage } from "../api/api";
// import MessageList from "./MessageList";
// import ChatInput from "./ChatInput";

// const ChatInterface = () => {
//   const { state, dispatch } = useChat();
//   const messagesEndRef = useRef(null);

//   const scrollToBottom = () => {
//     messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
//   };

//   useEffect(() => {
//     scrollToBottom();
//   }, [state.messages]);

//   const handleSendMessage = async (text) => {
//     if (!text.trim()) return;

//     // Add user message
//     dispatch({
//       type: "ADD_MESSAGE",
//       payload: { type: "user", content: text },
//     });

//     // Set loading state
//     dispatch({ type: "SET_LOADING", payload: true });

//     try {
//       const response = await sendMessage(text);
//       dispatch({
//         type: "ADD_MESSAGE",
//         payload: {
//           type: "bot",
//           content: response.response,
//           emotion: response.emotion,
//           emotionResponse: response.emotion_response,
//         },
//       });
//     } catch (error) {
//       dispatch({
//         type: "ADD_MESSAGE",
//         payload: {
//           type: "error",
//           content: "Sorry, something went wrong. Please try again.",
//         },
//       });
//     }
//   };

//   return (
//     <div className="max-w-2xl mx-auto bg-white rounded-lg shadow-xl overflow-hidden">
//       <div className="h-[600px] flex flex-col">
//         <MessageList
//           messages={state.messages}
//           loading={state.loading}
//           messagesEndRef={messagesEndRef}
//         />
//         {/* Pass handleSendMessage as a prop */}
//         <ChatInput onSendMessage={handleSendMessage} disabled={state.loading} />
//       </div>
//     </div>
//   );
// };

// export default ChatInterface;
// ChatInterface.js
import React, { useState, useEffect, useRef } from "react";
import { useChat } from "../context/ChatContext";
import { sendMessage } from "../api/api"; // This function calls your backend
import MessageList from "./MessageList";
import ChatInput from "./ChatInput";

const ChatInterface = () => {
  const { state, dispatch } = useChat();
  const [userMessage, setUserMessage] = useState("");
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [state.messages]);

  const handleSendMessage = async (text) => {
    if (!text.trim()) return;

    // Add the user's message to state
    dispatch({
      type: "ADD_MESSAGE",
      payload: { type: "user", content: text },
    });

    // Set loading state for bot response
    dispatch({ type: "SET_LOADING", payload: true });

    try {
      const response = await sendMessage(text);

      // Check the response for emotion
      const { response: botMessage, emotion, emotion_response } = response;

      // Add bot message to state
      dispatch({
        type: "ADD_MESSAGE",
        payload: {
          type: "bot",
          content: botMessage,
          emotion,
          emotionResponse: emotion_response,
        },
      });

      // Add supportive message based on detected emotion
      if (emotion === "sadness") {
        dispatch({
          type: "ADD_MESSAGE",
          payload: {
            type: "bot",
            content: "I'm here to help. Things will get better. 🌈",
          },
        });
      }
    } catch (error) {
      dispatch({
        type: "ADD_MESSAGE",
        payload: {
          type: "error",
          content: "Sorry, something went wrong. Please try again.",
        },
      });
    }
  };

  return (
    <div className="max-w-2xl mx-auto bg-white rounded-lg shadow-md">
      <div className="h-[600px] flex flex-col">
        <MessageList
          messages={state.messages}
          loading={state.loading}
          messagesEndRef={messagesEndRef}
        />
        <ChatInput
          message={userMessage}
          setMessage={setUserMessage}
          onSendMessage={handleSendMessage}
          disabled={state.loading}
        />
      </div>
    </div>
  );
};

export default ChatInterface;
