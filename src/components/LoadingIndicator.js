// import React from "react";

// const LoadingIndicator = () => {
//   return (
//     <div className="flex items-center space-x-2 p-4">
//       <div className="animate-bounce h-2 w-2 bg-gray-500 rounded-full"></div>
//       <div className="animate-bounce h-2 w-2 bg-gray-500 rounded-full delay-100"></div>
//       <div className="animate-bounce h-2 w-2 bg-gray-500 rounded-full delay-200"></div>
//     </div>
//   );
// };

// export default LoadingIndicator;
// components/LoadingIndicator.js
import React from "react";

const LoadingIndicator = () => {
  return (
    <div className="flex justify-center items-center space-x-2 p-4">
      <div className="animate-bounce h-3 w-3 bg-primary rounded-full"></div>
      <div className="animate-bounce h-3 w-3 bg-primary rounded-full delay-100"></div>
      <div className="animate-bounce h-3 w-3 bg-primary rounded-full delay-200"></div>
    </div>
  );
};

export default LoadingIndicator;
