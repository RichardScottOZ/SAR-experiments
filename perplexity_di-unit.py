import tensorflow as tf

# Define the input branches for each incidence angle
input_branch1 = tf.keras.layers.Input(shape=(128, 128, 23))
input_branch2 = tf.keras.layers.Input(shape=(128, 128, 23))

# Encoder pathway for each input branch
def encoder_block(inputs):
    x = tf.keras.layers.Conv2D(filters=64, kernel_size=(3, 3), padding='same')(inputs)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Activation('relu')(x)
    x = tf.keras.layers.Conv2D(filters=64, kernel_size=(3, 3), padding='same')(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Activation('relu')(x)
    encoded = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(x)
    return encoded

encoded_branch1 = encoder_block(input_branch1)
encoded_branch2 = encoder_block(input_branch2)

# Bottleneck layer
bottleneck = tf.keras.layers.Concatenate()([encoded_branch1, encoded_branch2])

# Decoder pathway
def decoder_block(inputs):
    x = tf.keras.layers.Conv2D(filters=64, kernel_size=(3, 3), padding='same')(inputs)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Activation('relu')(x)
    x = tf.keras.layers.Conv2D(filters=64, kernel_size=(3, 3), padding='same')(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Activation('relu')(x)
    decoded = tf.keras.layers.UpSampling2D(size=(2, 2))(x)
    return decoded

decoded_block1 = decoder_block(encoded_branch1)
decoded_block2 = decoder_block(encoded_branch2)

# Combine features from encoder blocks
combined_features = tf.keras.layers.Concatenate()([decoded_block1, decoded_block2])

# Output layer
output_layer = tf.keras.layers.Conv2D(filters=1, kernel_size=(1, 1), activation='sigmoid')(combined_features)

# Create the model
model = tf.keras.models.Model(inputs=[input_branch1, input_branch2], outputs=output_layer)

# Compile the model and define loss and optimizer
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Display model summary
model.summary()