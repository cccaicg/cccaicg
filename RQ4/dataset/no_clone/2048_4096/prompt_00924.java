/**
 * Create a segment with the specified status.
 * 
 * @param the
 *          segment's paths
 * @param the
 *          status of the record, ignored if redirect is true
 * @param whether
 *          we're doing a redirect as well
 */
protected void createSegment(Path segment, byte status, boolean redirect)
    throws Exception 
{
    if (redirect)
    {
        status = HttpConstants.STATUS_FOUND;
    }

    SegmentDescriptor desc = new SegmentDescriptor(segment, status, redirect);
    segments.add(desc);
}   