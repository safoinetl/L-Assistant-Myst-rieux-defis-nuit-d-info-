// App.js
import React from 'react';
import { ChatProvider } from './context/ChatContext';
import ChatInterface from './components/ChatInterface';

function App() {
  return (
    <ChatProvider>
      <div className="min-h-screen bg-background font-sans">
        <div className="container mx-auto p-4">
          <h1 className="text-4xl font-semibold text-primary text-center mb-8">
            Chatbot Assistant
          </h1>
          <ChatInterface />
        </div>
      </div>
    </ChatProvider>
  );
}

export default App;
