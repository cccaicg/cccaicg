// xss跨站脚本检测
public static boolean xssInspect(String value) 
{
    if (value == null || value.isEmpty()) {
        return false;
    }
    String valueLower = value.toLowerCase();
    if (valueLower.contains("<script>") || valueLower.contains("</script>")) {
        return true;
    }
    return false;
}   