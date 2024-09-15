/**
 * Opens the dialog and waits for user to input the data.
 * 
 * @return the entered text or null in case of cancel.
 */
public String open(String text, String okButtonText) 
{
    if (text != null)
    {
        textArea.setText(text);
    }

    if (okButtonText != null)
    {
        okButton.setText(okButtonText);
    }

    setVisible(true);

    return textArea.getText();
}   