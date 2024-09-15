/**
 * Checks the merged segment and removes the stuff again.
 * 
 * @param the
 *          test directory
 * @param the
 *          merged segment
 * @return the final status
 */
protected byte checkMergedSegment(Path testDir, Path mergedSegment)
    throws Exception 
{
    // check the merged segment
    byte status = checkSegment(testDir, mergedSegment);

    // remove the merged segment
    FileUtil.fullyDelete(mergedSegment.toFile());

    return status;
}   