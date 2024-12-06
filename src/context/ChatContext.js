// import React, { createContext, useContext, useReducer } from "react";

// const ChatContext = createContext();

// const chatReducer = (state, action) => {
//   switch (action.type) {
//     case "ADD_MESSAGE":
//       return {
//         ...state,
//         messages: [...state.messages, action.payload],
//         loading: false,
//       };
//     case "SET_LOADING":
//       return {
//         ...state,
//         loading: action.payload,
//       };
//     default:
//       return state;
//   }
// };

// export const ChatProvider = ({ children }) => {
//   const [state, dispatch] = useReducer(chatReducer, {
//     messages: [],
//     loading: false,
//   });

//   return (
//     <ChatContext.Provider value={{ state, dispatch }}>
//       {children}
//     </ChatContext.Provider>
//   );
// };

// export const useChat = () => useContext(ChatContext);
// ChatContext.js
import React, { createContext, useContext, useReducer } from 'react';

const ChatContext = createContext();

const chatReducer = (state, action) => {
  switch (action.type) {
    case 'ADD_MESSAGE':
      return {
        ...state,
        messages: [...state.messages, action.payload],
        loading: false,
      };
    case 'SET_LOADING':
      return {
        ...state,
        loading: action.payload,
      };
    default:
      return state;
  }
};

export const ChatProvider = ({ children }) => {
  const [state, dispatch] = useReducer(chatReducer, {
    messages: [],
    loading: false,
  });

  return (
    <ChatContext.Provider value={{ state, dispatch }}>
      {children}
    </ChatContext.Provider>
  );
};

export const useChat = () => useContext(ChatContext);
