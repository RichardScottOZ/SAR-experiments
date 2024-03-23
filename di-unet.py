import tensorflow as tf

def encoder_block(inputs, filters):
    conv1 = tf.keras.layers.Conv2D(filters, 3, activation='relu', padding='same')(inputs)
    conv2 = tf.keras.layers.Conv2D(filters, 3, activation='relu', padding='same')(conv1)
    pool = tf.keras.layers.MaxPooling2D()(conv2)
    return pool

def decoder_block(inputs, skip, filters):
    upsample = tf.keras.layers.Conv2DTranspose(filters, 2, strides=(2, 2), padding='same')(inputs)
    concat = tf.keras.layers.Concatenate()([upsample, skip])
    conv1 = tf.keras.layers.Conv2D(filters, 3, activation='relu', padding='same')(concat)
    conv2 = tf.keras.layers.Conv2D(filters, 3, activation='relu', padding='same')(conv1)
    return conv2

def dual_input_unet(input_shape=(128, 128, 23)):
    inputs1 = tf.keras.layers.Input(input_shape)
    inputs2 = tf.keras.layers.Input(input_shape)
    
    # Encoder pathway for input branch 1
    enc1_1 = encoder_block(inputs1, 64)
    enc1_2 = encoder_block(enc1_1, 128)
    enc1_3 = encoder_block(enc1_2, 256)
    enc1_4 = encoder_block(enc1_3, 512)
    
    # Encoder pathway for input branch 2
    enc2_1 = encoder_block(inputs2, 64)
    enc2_2 = encoder_block(enc2_1, 128)
    enc2_3 = encoder_block(enc2_2, 256)
    enc2_4 = encoder_block(enc2_3, 512)
    
    # Bottleneck
    bottleneck = tf.keras.layers.Conv2D(1024, 3, activation='relu', padding='same')(enc1_4)
    
    # Decoder pathway
    dec4 = decoder_block(bottleneck, enc1_4, 512)
    dec3 = decoder_block(dec4, enc1_3, 256)
    dec2 = decoder_block(dec3, enc1_2, 128)
    dec1 = decoder_block(dec2, enc1_1, 64)
    
    # Final convolution
    outputs = tf.keras.layers.Conv2D(1, 1, activation='sigmoid')(dec1)
    
    model = tf.keras.Model(inputs=[inputs1, inputs2], outputs=outputs)
    return model

# Creating an instance of the model
model = dual_input_unet()
model.summary()
