import tensorflow as tf

def test_tensorflow_import_and_version():
    """
    Tests that tensorflow can be imported and its version can be retrieved.
    """
    print(f"TensorFlow version: {tf.__version__}")
    assert tf.__version__ is not None
    assert tf.__version__ != ""
