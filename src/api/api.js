// const API_URL = "http://localhost:5000";

// export const sendMessage = async (message) => {
//   try {
//     const response = await fetch(`${API_URL}/chat`, {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify({ message }),
//     });
//     return await response.json();
//   } catch (error) {
//     console.error("Error sending message:", error);
//     throw error;
//   }
// };
// api.js
const API_URL = "http://localhost:5000";

export const sendMessage = async (message) => {
  try {
    const response = await fetch(`${API_URL}/chat`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message }),
    });
    return await response.json();
  } catch (error) {
    console.error("Error sending message:", error);
    throw error;
  }
};
