from emotion_detection.emotion_detector import emotion_detector

# Define test cases
test_cases = [
    {"text": "I am so happy that I passed the exam.", "expected": "joy"},
    {"text": "I am really mad about this service.", "expected": "anger"},
    {"text": "I am terrified of the dark.", "expected": "fear"},
    {"text": " ", "expected": None}  # Testing the 400 Bad Request handler
]

print("🧪 Starting Verification Tests...\n")

for i, case in enumerate(test_cases, 1):
    input_text = case["text"]
    expected_emotion = case["expected"]

    print(f"--- Test Case {i} ---")
    print(f"Input: '{input_text}'")

    # Call the function
    result = emotion_detector(input_text)

    # Check the result
    actual_emotion = result['dominant_emotion']

    print(f"Result: {result}")

    if actual_emotion == expected_emotion:
        print(f"✅ PASS: Dominant emotion is '{actual_emotion}'")
    else:
        print(f"❌ FAIL: Expected '{expected_emotion}' but got '{actual_emotion}'")

    print("\n")

print("🏁 Verification Complete.")