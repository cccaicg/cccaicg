/**
 * 返回指定长度随机数字组成的字符串
 * 
 * @param length
 *            指定长度
 * @return 随机字符串
 */
public static String captchaNumber(int length){
    StringBuilder sb = new StringBuilder();
    Random rand = new Random();
    for (int i = 0; i < length; i++) {
        sb.append(rand.nextInt(10));
    }
    return sb.toString();
}