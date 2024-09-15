/**
 * Defines which drawable to use in the default error activity image.
 * Set this if you want to use an image other than the default one.
 * The default is R.drawable.customactivityoncrash_error_image (a cute upside-down bug).
 */
@NonNull
public Builder errorDrawable(@Nullable @DrawableRes Integer errorDrawable) 
{
    this.errorDrawable = errorDrawable;
    return this;
}   