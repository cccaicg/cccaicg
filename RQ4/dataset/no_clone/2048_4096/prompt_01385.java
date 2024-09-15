/**
 * 按照相对应的规则查找所有匹配类
 *
 * @param packages    包名
 * @param typeFilters 匹配规则
 * @param consumer    consumer lambda
 */
public static void scannerPackage(String[] packages, TypeFilter[] typeFilters, Consumer<Class<?>> consumer) 
{
    if (packages == null || packages.length == 0)
    {
        return;
    }
    for (String basePackage : packages)
    {
        scannerPackage(basePackage, typeFilters, consumer);
    }
}   