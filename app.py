import whisper

# Initialize the LLM model
llm = whisper.load_model("small")

# Create a Whisper client
client = whisper.Client()

# Function to handle incoming calls from other users
async def handle_call(call_id, audio):
    # Extract audio frames from the call
    frames = await client.extract_audio_frames(call_id, audio)

    # Use the LLM model to process the extracted audio frames
    responses = llm(frames)

    # Return the processed responses as a string
    return "\n".join(responses)

# Create a Flask app to serve the web UI
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/call", methods=["POST"])
def handle_call_request():
    call_id = request.json["call_id"]
    audio = request.json["audio"]

    # Handle the incoming call using the function above
    response = handle_call(call_id, audio)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
