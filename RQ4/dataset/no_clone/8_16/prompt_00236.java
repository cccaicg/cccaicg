// Get album art for specified album. This method will not try to
// fall back to getting artwork directly from the file, nor will
// it attempt to repair the database.









private static Bitmap getArtworkQuick(Context context, int album_id, int w, int h) 
{
    Bitmap bm = null;
    try {
        final Uri sArtworkUri = Uri.parse("content://media/external/audio/albumart/" + album_id);
        Uri uri = ContentUris.withAppendedId(sArtworkUri, album_id);
        ParcelFileDescriptor pfd = context.getContentResolver().openFileDescriptor(uri, "r");
        if (pfd != null) {
            FileDescriptor fd = pfd.getFileDescriptor();
            bm = BitmapFactory.decodeFileDescriptor(fd, null, new BitmapFactory.Options());
            pfd = null;
        }
    } catch (Exception e) {
    }
    if (bm != null) {
        bm = ThumbnailUtils.extractThumbnail(bm, w, h);
    } else {
        bm = getArtwork(context, album_id, w, h, true);
    }
    return bm;
}   