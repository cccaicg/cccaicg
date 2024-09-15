/**
 * Set the negative button text and it's listener
 * @param negativeButtonText
 * @param listener
 * @return
 */
public Builder setNegativeButton(String negativeButtonText,
        DialogInterface.OnClickListener listener) 
{
    P.negativeButtonText = negativeButtonText;
    P.negativeButtonListener = listener;
    return this;
}       