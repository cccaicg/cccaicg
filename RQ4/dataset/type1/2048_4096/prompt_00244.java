/**
 * 字符串转数组
 * @param str
 * @return
 */
public static byte[] hexStrToByteArray(String str) 
{
    if (str == null) {
        return null;
    }
    if (str.length() == 0) {
        return new byte[0];
    }
    byte[] byteArray = new byte[str.length() / 2];
    for (int i = 0; i < byteArray.length; i++) {
        String subStr = str.substring(2 * i, 2 * i + 2);
        byteArray[i] = ((byte) Integer.parseInt(subStr, 16));
    }
    return byteArray;
}   