/** Gets be called on the following structure:
 * <tag>characters</tag> */
@Override
	public void characters(char ch[], int start, int length) 
{
    if (inElement) {
        String value = new String(ch, start, length);
        if (value.trim().length() > 0)
            elementValue = value;
    }
}	