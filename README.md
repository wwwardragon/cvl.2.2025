# cvl.2.2025

Using template matching, this code will try to match item without the use of external library (OpenCV, TensorFlow, PyTorch)
So with using Template Match we are measuring the similarity by computing the sum of squared differences (SSD).
The smaller the score, the better the match.
Returns the coordinates (x, y) where the best match occurs and the lowest difference value.

Accuracy is pretty high, changing the position of the object inside the image does not affect the accuracy of the code, still giving the right results.
The IoU score is 1.0, which means that the detected box perfectly overlaps with the ground truth bounding box.

But I haven't tested out the result with real-life pictures, so the results are still unknown about this one. Since real-life objects have slight differences in rotation, scale, or light that will affect the pixel intensity.
