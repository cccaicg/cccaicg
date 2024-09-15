/**
 * @return the previously marked position or -1 if no mark has been set.
 *
 * @throws IllegalStateException if called with automatic marking disabled.
 */
public int getMarkedPosition(){
    if (!mMarking) {
        throw new IllegalStateException("getMarkedPosition() called without automatic marking support.");
    }
    return mMarkedPosition;
}