import numpy as np
import tensorflow as tf
from keras import layers
from keras.models import load_model
import matplotlib.pyplot as plt
from glob import glob
import keras
import os
from sklearn.metrics import accuracy_score

# GPU 사용 안 함 설정
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# Define constants and character mappings
max_length = 5
characters = ['2', '3', '4', '5', '6', '7', '8', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'k', 'm', 'n', 'p', 'q', 'r', 'v', 'w', 'x', 'y']

# Encode Labels
char_to_num = layers.StringLookup(vocabulary=list(characters), num_oov_indices=0, mask_token=None)
num_to_char = layers.StringLookup(vocabulary=char_to_num.get_vocabulary(), num_oov_indices=0, mask_token=None, invert=True)

# Load the model
lodedmodel = load_model('./model/model_save_test', compile=False)
lodedmodel.summary()

# Decode predictions
def decode_batch_predictions(pred):
    input_len = np.ones(pred.shape[0]) * pred.shape[1]
    results = keras.backend.ctc_decode(pred, input_length=input_len, greedy=True)[0][0][:, :max_length]
    output_text = []
    for res in results:
        res = tf.strings.reduce_join(num_to_char(res)).numpy().decode('utf-8')
        output_text.append(res)
    return output_text

# Prediction function
def predit(cap_img):
    file_list = glob(cap_img)
    if not file_list:
        raise FileNotFoundError(f"No file found at {cap_img}. Check the path and try again.")

    # Load and preprocess image
    img = tf.io.read_file(file_list[0])
    img = tf.io.decode_png(img, channels=1)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = tf.image.resize(img, [50, 200])
    img = tf.transpose(img, perm=[1, 0, 2])
    img = tf.expand_dims(img, axis=0)

    print(f"Image shape after preprocessing: {img.shape}")

    # Predict
    preds = lodedmodel.predict(img)
    return decode_batch_predictions(preds)[0]

x_test = ["C:/python/RPA/sw/capImg.png", "C:/python/RPA/sw/capImg1.png"]
y_test = ["h8aw8", "8e2g3"]


# 예측 수행 및 정확도 계산
predictions = []
for img_path, true_label in zip(x_test, y_test):
    pred_label = predit(img_path).strip()  # 양 끝 공백 제거
    predictions.append(pred_label)

# 실제 라벨도 동일하게 공백을 제거한 상태로 비교
y_test = [label.strip() for label in y_test]

# 정확도 계산
accuracy = accuracy_score(y_test, predictions)
print(f"예측 정확도: {accuracy * 100:.2f}%")

# 예측과 실제 라벨 출력
for i, (pred, actual) in enumerate(zip(predictions, y_test)):
    print(f"Sample {i}: Predicted = '{pred}', Actual = '{actual}'")

predictions = [str(pred).strip() for pred in predictions]
y_test = [str(label).strip() for label in y_test]

