import tensorflow as tf

print("Num GPUs Available: \n", len(tf.config.list_physical_devices('GPU')))

# if tf.test.gpu_device_name():
#     print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
# else:
#     print("Please install GPU version of TF")