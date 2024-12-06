
import React from 'react';

const Message = ({ message }) => {
  const isUser = message.type === 'user';
  const isError = message.type === 'error';

  return (
    <div
      className={`flex ${isUser ? 'justify-end' : 'justify-start'} items-start`}
    >
      <div
        className={`max-w-[75%] p-3 rounded-lg shadow-md ${
          isUser
            ? 'bg-primary text-white'
            : isError
            ? 'bg-red-100 text-red-700'
            : 'bg-gray-100 text-gray-800'
        }`}
      >
        <p className="text-sm">{message.content}</p>
        {message.emotionResponse && (
          <p className="mt-2 text-xs opacity-75">{message.emotionResponse}</p>
        )}
      </div>
    </div>
  );
};

export default Message;
