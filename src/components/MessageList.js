// import React from 'react';
// import Message from './Message';
// import LoadingIndicator from './LoadingIndicator';

// const MessageList = ({ messages, loading, messagesEndRef }) => {
//   return (
//     <div className="flex-1 overflow-y-auto p-4 space-y-4">
//       {messages.map((message, index) => (
//         <Message key={index} message={message} />
//       ))}
//       {loading && <LoadingIndicator />}
//       <div ref={messagesEndRef} />
//     </div>
//   );
// };

// export default MessageList;
// components/MessageList.js
// components/MessageList.js
import React from 'react';
import Message from './Message';
import LoadingIndicator from './LoadingIndicator';

const MessageList = ({ messages, loading, messagesEndRef }) => {
  return (
    <div className="flex-1 overflow-y-auto p-4 space-y-4">
      {messages.map((message, index) => (
        <Message key={index} message={message} />
      ))}
      {loading && <LoadingIndicator />}
      <div ref={messagesEndRef} />
    </div>
  );
};

export default MessageList;
