/**
 * Called to execute the actual scanning process.
 * @param scanningResults the scanning results, which are available
 * @param filter optional (can be null) - determines results for saving or skipping
 */
public void process(ScanningResultList scanningResults, ScanningResultFilter filter) 
{
    if (scanningResults != null)
    {
        for (ScanningResult result : scanningResults)
        {
            if (filter == null || filter.matches(result))
            {
                save(result);
            }
        }
    }
}   