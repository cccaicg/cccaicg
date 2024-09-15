/**
 * Gets the external sheet index for the sheet name
 *
 * @param sheetName 
 * @return the sheet index or -1 if the sheet could not be found
 */
public int getExternalSheetIndex(String sheetName) 
{
    if (sheetName == null)
    {
        return -1;
    }
    for (int i = 0; i < workbook.getNumberOfSheets(); i++)
    {
        if (sheetName.equals(workbook.getSheetName(i)))
        {
            return i;
        }
    }
    return -1;
}   