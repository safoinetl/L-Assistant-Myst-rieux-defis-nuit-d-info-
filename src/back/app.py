# from flask import Flask, request, jsonify
# from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSequenceClassification, pipeline
# from flask_cors import CORS
# from langdetect import detect
# import sqlite3
# import time

# # Initialize Flask app
# app = Flask(__name__)
# CORS(app)

# # Load pre-trained language model and tokenizer
# MODEL_NAME = "bigscience/bloom-560m"
# tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
# model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# # Load pre-trained emotion detection model
# emotion_model_name = "j-hartmann/emotion-english-distilroberta-base"
# emotion_tokenizer = AutoTokenizer.from_pretrained(emotion_model_name)
# emotion_model = AutoModelForSequenceClassification.from_pretrained(emotion_model_name)
# emotion_classifier = pipeline("text-classification", model=emotion_model, tokenizer=emotion_tokenizer)

# # Initialize text generation pipeline
# generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

# # SQLite database setup
# DATABASE = "user_data.db"

# def init_db():
#     """Initialize the SQLite database with required tables."""
#     conn = sqlite3.connect(DATABASE)
#     cursor = conn.cursor()
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS user_data (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         message TEXT,
#         emotion TEXT,
#         timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
#     )
#     """)
#     conn.commit()
#     conn.close()

# init_db()

# # Emotion response templates
# EMOTION_RESPONSES = {
#     "joy": "I'm glad you're feeling happy! 😊",
#     "sadness": "I'm here to help. Things will get better. 🌈",
#     "anger": "I'm sorry if something upset you. Let's solve it together. 🤝",
#     "fear": "It's okay to feel afraid. We're here for you. 🤗",
#     "love": "It's nice to feel loved! 💖",
#     "surprise": "Wow, that's surprising! 😲",
#     "neutral": "I hear you. Please tell me more about that."
# }

# def detect_emotion(text):
#     """Detect emotion in text using emotion classification pipeline."""
#     try:
#         result = emotion_classifier(text)
#         if result:
#             return result[0]['label'].lower()
#     except Exception as e:
#         print(f"Error detecting emotion: {e}")
#         return "neutral"

# def generate_response(user_input):
#     """Generate a contextual response using the language model."""
#     try:
#         prompt = f"User: {user_input}\nAssistant: Let me help you with that."
        
#         response = generator(
#             prompt,
#             max_length=150,
#             num_return_sequences=1,
#             pad_token_id=tokenizer.eos_token_id,
#             temperature=0.7,
#             top_p=0.9,
#             do_sample=True
#         )[0]['generated_text']
        
#         # Extract only the assistant's response
#         response_parts = response.split("Assistant:")
#         if len(response_parts) > 1:
#             response = response_parts[-1].strip()
#         else:
#             response = "I understand. Let me help you with that."
            
#         return response
#     except Exception as e:
#         print(f"Error generating response: {e}")
#         return "I apologize, but I'm having trouble generating a response right now."

# @app.route('/', methods=['GET'])
# def hello():
#     """Root endpoint to verify the API is running."""
#     return jsonify({
#         "message": "Welcome to Richatt Chatbot!",
#         "status": "online",
#         "version": "2.0"
#     })

# @app.route("/chat", methods=['GET', 'POST'])
# def chat():
#     """Main chat endpoint handling both GET and POST requests."""
#     try:
#         if request.method == 'GET':
#             return jsonify({"message": "Chat endpoint is working. Use POST to send messages."})
        
#         # Get user input from POST request
#         data = request.get_json(force=True)
#         user_input = data.get("message", "")

#         if not user_input:
#             return jsonify({"error": "No message provided"}), 400

#         # Detect input language
#         try:
#             lang = detect(user_input)
#         except:
#             lang = 'en'

#         # Emotion detection
#         start_time = time.time()
#         emotion = detect_emotion(user_input)
#         emotion_detection_time = time.time() - start_time

#         # Generate response
#         start_time = time.time()
#         response = generate_response(user_input)
#         generation_time = time.time() - start_time

#         # Save to database
#         try:
#             conn = sqlite3.connect(DATABASE)
#             cursor = conn.cursor()
#             cursor.execute(
#                 "INSERT INTO user_data (message, emotion) VALUES (?, ?)",
#                 (user_input, emotion)
#             )
#             conn.commit()
#             conn.close()
#         except Exception as e:
#             print(f"Database error: {e}")

#         # Get emotion-specific response
#         emotion_message = EMOTION_RESPONSES.get(emotion, "Tell me more!")

#         return jsonify({
#             "response": response,
#             "emotion_response": emotion_message,
#             "detected_language": lang,
#             "emotion": emotion,
#             "emotion_detection_time": emotion_detection_time,
#             "generation_time": generation_time
#         })

#     except Exception as e:
#         return jsonify({
#             "error": "Invalid request",
#             "details": str(e)
#         }), 400

# @app.route("/userdata", methods=['GET'])
# def get_user_data():
#     """Endpoint to retrieve collected user data."""
#     try:
#         conn = sqlite3.connect(DATABASE)
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM user_data ORDER BY timestamp DESC LIMIT 100")
#         columns = [description[0] for description in cursor.description]
#         rows = cursor.fetchall()
#         data = [dict(zip(columns, row)) for row in rows]
#         conn.close()
        
#         return jsonify({
#             "user_data": data,
#             "count": len(data)
#         })
#     except Exception as e:
#         return jsonify({
#             "error": "Failed to retrieve user data",
#             "details": str(e)
#         }), 500

# @app.errorhandler(404)
# def not_found(e):
#     """Handle 404 errors."""
#     return jsonify({
#         "error": "Not found",
#         "message": "The requested resource was not found on this server."
#     }), 404

# @app.errorhandler(405)
# def method_not_allowed(e):
#     """Handle 405 errors."""
#     return jsonify({
#         "error": "Method not allowed",
#         "message": "The requested method is not allowed for this endpoint."
#     }), 405

# @app.errorhandler(500)
# def server_error(e):
#     """Handle 500 errors."""
#     return jsonify({
#         "error": "Internal server error",
#         "message": "An unexpected error occurred. Please try again later."
#     }), 500

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=False)
from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSequenceClassification, pipeline
from flask_cors import CORS
from langdetect import detect
import sqlite3
import time

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load pre-trained language model and tokenizer
MODEL_NAME = "bigscience/bloom-560m"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# Load pre-trained emotion detection model
emotion_model_name = "j-hartmann/emotion-english-distilroberta-base"
emotion_tokenizer = AutoTokenizer.from_pretrained(emotion_model_name)
emotion_model = AutoModelForSequenceClassification.from_pretrained(emotion_model_name)
emotion_classifier = pipeline("text-classification", model=emotion_model, tokenizer=emotion_tokenizer)

# Initialize text generation pipeline
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

# SQLite database setup
DATABASE = "user_data.db"

def init_db():
    """Initialize the SQLite database with required tables."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        message TEXT,
        emotion TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

init_db()

# Emotion response templates
EMOTION_RESPONSES = {
    "joy": "I'm glad you're feeling happy! 😊",
    "sadness": "I'm here to help. Things will get better. 🌈",
    "anger": "I'm sorry if something upset you. Let's solve it together. 🤝",
    "fear": "It's okay to feel afraid. We're here for you. 🤗",
    "love": "It's nice to feel loved! 💖",
    "surprise": "Wow, that's surprising! 😲",
    "neutral": "I hear you. Please tell me more about that."
}

# Fallback responses for each emotion
FALLBACK_RESPONSES = {
    "sadness": "I understand you're feeling sad. Remember that it's okay to feel this way, and these feelings won't last forever. Consider talking to someone you trust, doing something you enjoy, or practicing self-care activities. Would you like to talk more about what's bothering you?",
    "joy": "That's wonderful! I'm happy to hear you're feeling good. What made your day special?",
    "anger": "I can see that you're frustrated. Let's take a moment to breathe and think about this together. Would you like to talk about what's bothering you?",
    "fear": "It's natural to feel scared sometimes. You're not alone in this. Let's think about what we can do to help you feel safer and more secure.",
    "love": "Those are beautiful feelings you're expressing. It's wonderful to experience such positive emotions!",
    "surprise": "That's quite unexpected! Would you like to talk more about how this makes you feel?",
    "neutral": "I'm here to listen and help. Could you tell me more about what's on your mind?"
}

def detect_emotion(text):
    """Detect emotion in text using emotion classification pipeline."""
    try:
        result = emotion_classifier(text)
        if result:
            return result[0]['label'].lower()
    except Exception as e:
        print(f"Error detecting emotion: {e}")
        return "neutral"

def generate_response(user_input, emotion):
    """Generate a contextual and appropriate response using the language model."""
    try:
        # Create emotion-specific prompts
        emotion_prompts = {
            "sadness": "User is feeling sad and needs compassionate advice. Be gentle and supportive.",
            "joy": "User is happy. Share their joy and encourage them.",
            "anger": "User is angry. Help them process their emotions calmly.",
            "fear": "User is afraid. Provide reassurance and practical support.",
            "love": "User is expressing love or affection. Respond warmly.",
            "surprise": "User is surprised. Help them process the unexpected.",
            "neutral": "Provide a helpful and engaged response."
        }

        # Create a more specific prompt based on emotion
        emotion_context = emotion_prompts.get(emotion, emotion_prompts["neutral"])
        
        prompt = f"""Context: {emotion_context}
User: {user_input}
Assistant: Let me help you with that. Remember that your feelings are valid and temporary. Here are some suggestions that might help:"""
        
        response = generator(
            prompt,
            max_length=200,
            min_length=50,
            num_return_sequences=1,
            pad_token_id=tokenizer.eos_token_id,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            repetition_penalty=1.2
        )[0]['generated_text']
        
        # Extract only the assistant's response
        response_parts = response.split("Assistant:")
        if len(response_parts) > 1:
            response = response_parts[-1].strip()
            
            # Clean up the response
            response = response.replace("User:", "").replace("Assistant:", "")
            response = response.replace(prompt, "")
            
            # Validate response quality
            if len(response.split()) < 10 or "I am not" in response or "I am a" in response:
                response = FALLBACK_RESPONSES.get(emotion, FALLBACK_RESPONSES["neutral"])
        else:
            response = FALLBACK_RESPONSES.get(emotion, FALLBACK_RESPONSES["neutral"])
            
        return response

    except Exception as e:
        print(f"Error generating response: {e}")
        return FALLBACK_RESPONSES.get(emotion, FALLBACK_RESPONSES["neutral"])

@app.route('/', methods=['GET'])
def hello():
    """Root endpoint to verify the API is running."""
    return jsonify({
        "message": "Welcome to Richatt Chatbot!",
        "status": "online",
        "version": "2.0"
    })

@app.route("/chat", methods=['GET', 'POST'])
def chat():
    """Main chat endpoint handling both GET and POST requests."""
    try:
        if request.method == 'GET':
            return jsonify({"message": "Chat endpoint is working. Use POST to send messages."})
        
        data = request.get_json(force=True)
        user_input = data.get("message", "")

        if not user_input:
            return jsonify({"error": "No message provided"}), 400

        try:
            lang = detect(user_input)
        except:
            lang = 'en'

        start_time = time.time()
        emotion = detect_emotion(user_input)
        emotion_detection_time = time.time() - start_time

        start_time = time.time()
        response = generate_response(user_input, emotion)
        generation_time = time.time() - start_time

        try:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO user_data (message, emotion) VALUES (?, ?)",
                (user_input, emotion)
            )
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Database error: {e}")

        emotion_message = EMOTION_RESPONSES.get(emotion, "Tell me more!")

        return jsonify({
            "response": response,
            "emotion_response": emotion_message,
            "detected_language": lang,
            "emotion": emotion,
            "emotion_detection_time": emotion_detection_time,
            "generation_time": generation_time
        })

    except Exception as e:
        return jsonify({
            "error": "Invalid request",
            "details": str(e)
        }), 400

@app.route("/userdata", methods=['GET'])
def get_user_data():
    """Endpoint to retrieve collected user data."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_data ORDER BY timestamp DESC LIMIT 100")
        columns = [description[0] for description in cursor.description]
        rows = cursor.fetchall()
        data = [dict(zip(columns, row)) for row in rows]
        conn.close()
        
        return jsonify({
            "user_data": data,
            "count": len(data)
        })
    except Exception as e:
        return jsonify({
            "error": "Failed to retrieve user data",
            "details": str(e)
        }), 500

@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors."""
    return jsonify({
        "error": "Not found",
        "message": "The requested resource was not found on this server."
    }), 404

@app.errorhandler(405)
def method_not_allowed(e):
    """Handle 405 errors."""
    return jsonify({
        "error": "Method not allowed",
        "message": "The requested method is not allowed for this endpoint."
    }), 405

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors."""
    return jsonify({
        "error": "Internal server error",
        "message": "An unexpected error occurred. Please try again later."
    }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)