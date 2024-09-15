/**
 * Request to fill a SensorMatrix with last capture.
 * @param matrix  - to be filled
 */
final public synchronized void copyVisionImage(SensorMatrix matrix) 
{
    if (visionImage != null)
    {
        visionImage.copyTo(matrix);
    }
}   