import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPooling2D, BatchNormalization, ReLU, Concatenate, Conv2DTranspose

def encoder_block(input_tensor, filters, kernel_size=3, strides=1, padding='same'):
    x = Conv2D(filters, kernel_size, strides=strides, padding=padding)(input_tensor)
    x = BatchNormalization()(x)
    x = ReLU()(x)
    x = Conv2D(filters, kernel_size, strides=strides, padding=padding)(x)
    x = BatchNormalization()(x)
    x = ReLU()(x)
    return x

def decoder_block(input_tensor, filters, kernel_size=3, strides=1, padding='same'):
    x = Conv2DTranspose(filters, kernel_size, strides=strides, padding=padding)(input_tensor)
    x = BatchNormalization()(x)
    x = ReLU()(x)
    x = Conv2DTranspose(filters, kernel_size, strides=strides, padding=padding)(x)
    x = BatchNormalization()(x)
    x = ReLU()(x)
    return x

def build_model(input_shape=(128, 128, 23)):
    inputs = tf.keras.Input(shape=input_shape)
    
    # Ensure correct slicing of the input tensor
    # Assuming the input tensor has 23 channels, split it into two branches
    encoder1_input = inputs[:, :, :, :23] # First half of the channels
    encoder2_input = inputs[:, :, :, 23:] # Second half of the channels
    
    # Encoder pathways
    encoder1 = encoder_block(encoder1_input, 64)
    encoder2 = encoder_block(encoder2_input, 64)
    
    # Bottleneck
    bottleneck = Concatenate()([encoder1, encoder2])
    
    # Decoder pathways
    decoder1 = decoder_block(bottleneck, 64)
    decoder2 = decoder_block(bottleneck, 64)
    
    # Output
    output = Concatenate()([decoder1, decoder2])
    output = Conv2D(1, 1, activation='sigmoid')(output)
    
    model = tf.keras.Model(inputs=inputs, outputs=output)
    return model

model = build_model()
model.summary()
