/**
 * 判断缓存的byte数据是否到期
 * 
 * @param data
 * @return true：到期了 false：还没有到期
 */
private static boolean isDue(byte[] data) 
{
    if (data.length == 0)
    {
        return true;
    }
    return data[0] == 0;
}   