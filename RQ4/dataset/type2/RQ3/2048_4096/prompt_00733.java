/**
 * Use it to animate TextureView content x position
 * @param y
 */
public final void setContentY(float y) 
{
    if (mContentY != y)
    {
        mContentY = y;
        invalidate();
    }
}   