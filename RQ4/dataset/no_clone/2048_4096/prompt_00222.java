/**
 * 构造器
 *
 * @param context 上下文
 * @param layoutResource 自定义DayView的layout资源
 */
public CustomDayView(Context context, int layoutResource) 
{
    super(context, layoutResource);
    this.context = context;
    this.layoutResource = layoutResource;
    init();
}   