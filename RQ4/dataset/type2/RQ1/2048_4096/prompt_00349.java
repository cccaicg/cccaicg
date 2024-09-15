/**
 * Update text size with animation
 */
public static void updateTextSize(final TextView textView, float fromSize, float toSize) 
{
    ValueAnimator animator = ValueAnimator.ofFloat(fromSize, toSize);
    animator.setDuration(300);
    animator.addUpdateListener(new ValueAnimator.AnimatorUpdateListener()
    {
        @Override
        public void onAnimationUpdate(ValueAnimator animation)
        {
            float animatedValue = (float) animation.getAnimatedValue();
            textView.setTextSize(TypedValue.COMPLEX_UNIT_PX, animatedValue);
        }
    });
    animator.start();
}   