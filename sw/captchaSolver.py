
import numpy as np
import tensorflow as tf
import keras
from keras import layers
from glob import glob
from keras import layers
from keras.models import load_model
import matplotlib.pyplot as plt



max_length = 5
characters =  ['2', '3', '4', '5', '6', '7', '8', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'k', 'm', 'n', 'p', 'q', 'r', 'v', 'w', 'x', 'y']

# Encode Labels
char_to_num = layers.StringLookup(
    vocabulary=list(characters), num_oov_indices=0, mask_token=None
)

num_to_char = layers.StringLookup(
    vocabulary=char_to_num.get_vocabulary(), num_oov_indices=0, mask_token=None, invert=True
)

lodedmodel = load_model('./model/model_save_test', compile=False)
# 모델 구조 출력
# lodedmodel.summary()
# 컴파일 설정 추가
#lodedmodel.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


def decode_batch_predictions(pred):
    input_len = np.ones(pred.shape[0]) * pred.shape[1]
    # Use greedy search. For complex tasks, you can use beam search
    results = keras.backend.ctc_decode(pred, input_length=input_len, greedy=True)[0][0][
        :, :max_length
    ]
    print(results)
    # Iterate over the results and get back the text
    output_text = []
    for res in results:
        res = tf.strings.reduce_join(num_to_char(res)).numpy().decode('utf-8')
        print(res)
        output_text.append(res)
    print(output_text)
    return output_text

def predit(cap_img):
    file_list = glob(cap_img)
    print(file_list)
    if not file_list:
        raise FileNotFoundError(f"No file found at {cap_img}. Check the path and try again.")

    # Load and preprocess image
    img = tf.io.read_file(file_list[0])
    img = tf.io.decode_png(img, channels=1)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = tf.image.resize(img, [50, 200])  # Resize to (50, 200)

    # 훈련 시와 동일하게 가로 세로를 뒤집어야 합니다.
    img = tf.transpose(img, perm=[1, 0, 2])  # (200, 50)로 변환
    # Skip transpose here, as resizing should match the training shape directly
    img = tf.expand_dims(img, axis=0)  # Add batch dimension, final shape (1, 50, 200, 1)

    # Print processed image for debugging
    plt.imshow(img[0, :, :, 0], cmap='gray')
    plt.title("Preprocessed Image (Correct Orientation)")
    plt.show()

    # Predict
    preds = lodedmodel.predict(img)
    print("preds:", preds)
    return str(decode_batch_predictions(preds)[0])


