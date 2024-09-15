/**
 * Send a broadcast meaning a file was changed
 *
 * @param file FILE_*
 * @param uin  0 for a common file
 * @param what 0 for unspecified
 */
public static void onFileChanged(int file, long uin, int what) 
{
    if (file == FILE_COMMON)
    {
        if (uin == 0)
        {
            if (what == 0)
            {
                // Common file changed
                // Do something
            }
        }
    }
}   