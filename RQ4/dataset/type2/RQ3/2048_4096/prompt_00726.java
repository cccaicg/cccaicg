/**
 * Use it to animate TextureView content x position
 * @param x
 */
public final void setContentX(float x) 
{
    if (mContentX != x)
    {
        mContentX = x;
        invalidate();
    }
}   