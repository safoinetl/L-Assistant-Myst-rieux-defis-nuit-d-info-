// // components/ChatInput.js
// import React, { useState } from 'react';

// const ChatInput = ({ onSendMessage, disabled }) => {
//   const [message, setMessage] = useState('');

//   const handleSubmit = (e) => {
//     e.preventDefault();
//     if (message.trim() && !disabled) {
//       // Call onSendMessage when the user submits the form
//       onSendMessage(message);
//       setMessage(''); // Clear the input field after sending the message
//     }
//   };

//   return (
//     <form onSubmit={handleSubmit} className="p-4 border-t border-t-gray-200">
//       <div className="flex space-x-2">
//         <input
//           type="text"
//           value={message}
//           onChange={(e) => setMessage(e.target.value)}
//           placeholder="Type your message..."
//           className="flex-1 p-3 border rounded-lg border-input-border focus:outline-none focus:ring-2 focus:ring-primary"
//           disabled={disabled}
//         />
//         <button
//           type="submit"
//           disabled={disabled || !message.trim()}
//           className={`px-6 py-3 rounded-lg bg-primary text-white font-medium transition duration-300 ease-in-out transform ${
//             disabled || !message.trim()
//               ? 'opacity-50 cursor-not-allowed'
//               : 'hover:bg-blue-600 hover:scale-105'
//           }`}
//         >
//           Send
//         </button>
//       </div>
//     </form>
//   );
// };

// export default ChatInput;
// components/ChatInput.js
import React from "react";

const ChatInput = ({ message, setMessage, onSendMessage, disabled }) => {
  const handleSubmit = (e) => {
    e.preventDefault();
    if (message.trim() && !disabled) {
      onSendMessage(message);
      setMessage("");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="p-4 border-t">
      <div className="flex space-x-2">
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type your message..."
          className="flex-1 p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          disabled={disabled}
        />
        <button
          type="submit"
          disabled={disabled || !message.trim()}
          className={`px-4 py-2 rounded-lg bg-blue-500 text-white font-medium
            ${
              disabled || !message.trim()
                ? "opacity-50 cursor-not-allowed"
                : "hover:bg-blue-600"
            }`}
        >
          Send
        </button>
      </div>
    </form>
  );
};

export default ChatInput;
