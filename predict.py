import numpy as np
from fastapi import HTTPException, status
from tensorflow.keras.preprocessing.sequence import pad_sequences
from config import LABEL_DESCRIPTIONS, MAX_SEQUENCE_LENGTH, PADDING_TYPE, TRUNC_TYPE
from preprocessing import preprocess_text
    
def predict_something(data: str, model, tokenizer) -> str:
    # Mengecek apakah model dan tokenizer telah dimuat
    if not model or not tokenizer:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="ML Model or Tokenizer is not loaded on the server."
        )
    
    processed_text = preprocess_text(data)

    # Periksa jika teks yang diproses kosong
    if not processed_text:
        num_classes = len(LABEL_DESCRIPTIONS)
        default_probs = np.zeros(num_classes)
        if 0 in LABEL_DESCRIPTIONS : default_probs[0] = 1.0

    # Di bawah ini adalah contoh proses prediksi data teks. Anda dapat menyesuaikannya sesuai kebutuhan. 
    try:
        sequences = tokenizer.texts_to_sequences([processed_text])
        padded_input = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH, padding=PADDING_TYPE, truncating=TRUNC_TYPE)
        
        prediction = model.predict(padded_input)
        predicted_class_index = np.argmax(prediction[0])

        return LABEL_DESCRIPTIONS.get(predicted_class_index, "Unknown")
        
    except Exception as e:
        # ERROR HANDLING 2: Prediction crashed (e.g., shape mismatch)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Prediction failed: {str(e)}"
        )